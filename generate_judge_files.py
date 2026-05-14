"""
generate_judge_files.py
-----------------------
为 agents/ 下的每个智能体生成 LLM-AS-Judge 评测文件，保存到 agent_judge/。
使用 claude -p 非交互模式，每批 5 个并发执行。

用法：
    python generate_judge_files.py           # 全量运行
    python generate_judge_files.py --dry-run # 只打印命令，不执行
    python generate_judge_files.py --one workspace-x74fgmx0vyb8p5is  # 只跑一个
"""

import argparse
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ── 路径配置 ──────────────────────────────────────────────────────────────────
BASE_DIR     = Path(r"d:\python\VS_Code\天禧Claw虾质量验证")
AGENTS_DIR   = BASE_DIR / "agents"
OUTPUT_DIR   = BASE_DIR / "agent_judge"
MAPPING_FILE = AGENTS_DIR / "mapping.md"

MAX_WORKERS = 5
TIMEOUT     = 300  # 每个子进程最长等待秒数

# ── Prompt 模板 ───────────────────────────────────────────────────────────────
PROMPT_TEMPLATE = """\
你是一位专业的 AI 评测工程师，擅长为 AI 智能体设计高质量的 LLM-AS-Judge 评测方案。

## 任务
为 Agent 目录 {workspace_path} 生成评测文件，保存到 {output_path}。

---

## 工作流程（必须严格按顺序执行，不可跳步）

### Step 1：读取并理解 Agent 能力

依次读取以下文件（用 Read 工具）：
1. {workspace_path}/IDENTITY.md
2. {workspace_path}/SOUL.md
3. {workspace_path}/AGENTS.md
4. {workspace_path}/TOOLS.md
5. 列出 {workspace_path}/skills/ 目录，读取每个子目录下的 SKILL.md

读取完成后，在内部整理出以下四项（不需要输出，仅用于后续步骤）：
- **能力清单**：该 Agent 能做哪些具体的事（动词+宾语，如"生成 PRD"、"制定训练计划"）
- **标志性输出物**：该 Agent 最典型的交付物是什么（如 PRD 文档、数据报告、训练计划表）
- **能力边界**：该 Agent 明确不做什么（来自 SOUL.md 的 Boundaries 部分）
- **工作流程**：该 Agent 处理任务的标准步骤（来自 SKILL.md 的 workflow 部分）

### Step 2：构建用户画像

基于 Step 1 的理解，推断该 Agent 的真实用户：
- 他们是谁？（职业、背景、技术水平）
- 他们的核心痛点是什么？（为什么需要这个 Agent）
- 他们的典型使用场景是什么？（日常工作中的具体时刻）
- 他们对输出质量的期望是什么？

### Step 3：设计 5-10 条评测 Query

Query 必须覆盖以下四种类型（按比例分配）：
- **基础场景（2-3 条）**：典型用户的日常需求，直接触发 Agent 的核心能力
- **进阶场景（2-3 条）**：需要 Agent 展现专业深度，输出结构化的标志性交付物
- **边界场景（1-2 条）**：测试 Agent 如何处理超出能力范围的请求，或模糊/不完整的输入
- **综合场景（1 条）**：需要 Agent 调用多个能力，完成端到端的复杂任务

每条 Query 的写法要求：
- 用真实用户的口吻（口语化，有具体背景，不要技术化表述）
- 包含足够上下文（用户身份、当前处境、具体需求）
- 有明确的预期输出类型（让评测者知道该期待什么）

### Step 4：为每条 Query 设计打分标准

打分标准必须**基于该 Agent 的标志性输出物**定制，不能千篇一律。

对每条 Query：
1. 先想清楚"满分响应"应该包含哪些具体要素（引用 SKILL.md 中的模板结构）
2. 再从满分往下推导各档的缺失情况
3. 关键检查点必须是**可验证的具体项**（如"是否包含 RICE 评分矩阵"、"是否给出具体训练组数和休息时间"、"是否使用了情绪命名三步法"）

打分档位：
- **10 分**：描述理想输出的具体特征（列举 3-4 个必须包含的要素）
- **8 分**：高质量但有 1-2 处小瑕疵（具体说明是哪类瑕疵）
- **6 分**：基本满足需求但缺少关键要素（具体说明缺什么）
- **4 分**：部分相关但明显不足（具体说明不足在哪）
- **2 分**：严重偏离（具体说明偏离方向）
- **0 分**：完全失败（拒绝回答、答非所问、或触犯边界规则）

### Step 5：输出文件

将以下格式的内容用 Write 工具写入 {output_path}：

---

# {agent_name}（{workspace_id}）— LLM-AS-Judge 评测标准

## Agent 背景
[1-2 段，基于文件内容总结 Agent 的定位、核心能力和人设特点]

## 目标用户画像
| 维度 | 描述 |
|------|------|
| 职业/身份 | [具体职业或身份描述] |
| 核心需求 | [用户最迫切需要解决的问题] |
| 使用频率 | [日常/每周/按需，以及典型触发时机] |
| 专业水平 | [小白/中级/专家，以及对应的期望] |

## 核心使用场景
1. [场景名称]：[1-2 句描述，说明用户处境和需求]
2. ...（共 3-5 个）

## 评测 Query 与打分标准

### Query 1：[场景类型] — [场景标题]

**Query：**
> [用真实用户口吻写的完整提问，包含背景和具体需求，2-5 句话]

**打分标准（10 分制）：**

| 分数 | 标准描述 |
|------|---------|
| 10 | [列举 3-4 个必须包含的具体要素，引用 SKILL.md 中的模板结构] |
| 8  | [高质量但有具体瑕疵，说明是哪类瑕疵] |
| 6  | [基本满足但缺少具体关键要素，说明缺什么] |
| 4  | [部分相关但明显不足，说明不足在哪] |
| 2  | [严重偏离，说明偏离方向] |
| 0  | [完全失败的具体情形] |

**关键检查点：**
- [ ] [具体可验证的检查项 1]
- [ ] [具体可验证的检查项 2]
- [ ] [具体可验证的检查项 3]
（共 3-5 条）

---

[重复以上结构，共 5-10 条 Query]
"""

# ── 工具函数 ──────────────────────────────────────────────────────────────────

def parse_mapping(mapping_file: Path) -> list[tuple[str, str]]:
    """从 mapping.md 解析 [(workspace_id, agent_name), ...]"""
    agents = []
    pattern = re.compile(r'\|\s*(workspace-\S+)\s*\|\s*(.+?)\s*\|')
    for line in mapping_file.read_text(encoding="utf-8").splitlines():
        m = pattern.match(line)
        if m:
            agents.append((m.group(1), m.group(2).strip()))
    return agents


def run_one(workspace_id: str, agent_name: str, dry_run: bool = False) -> tuple[str, str, bool, str]:
    workspace_path = str(AGENTS_DIR / workspace_id)
    output_path    = str(OUTPUT_DIR / f"{workspace_id}.md")

    # 已存在则跳过
    if Path(output_path).exists():
        return workspace_id, agent_name, True, "skipped (already exists)"

    prompt = PROMPT_TEMPLATE.format(
        workspace_path=workspace_path,
        output_path=output_path,
        agent_name=agent_name,
        workspace_id=workspace_id,
    )

    cmd = [
        "claude.cmd", "-p", "-",
        "--dangerously-skip-permissions",
        "--model", "claude-opus-4-7",
        "--add-dir", workspace_path,
        "--add-dir", str(OUTPUT_DIR),
        "--allowedTools", "Read,Write,Glob",
    ]

    if dry_run:
        print(f"[DRY-RUN] {workspace_id}: {' '.join(cmd[:4])} ...")
        return workspace_id, agent_name, True, "dry-run"

    try:
        result = subprocess.run(
            cmd,
            input=prompt.encode("utf-8"),
            capture_output=True,
            timeout=TIMEOUT,
        )
        success = result.returncode == 0 and Path(output_path).exists()
        err_msg = result.stderr.decode("utf-8", errors="replace").strip()[-300:] if result.stderr else ""
        return workspace_id, agent_name, success, err_msg
    except subprocess.TimeoutExpired:
        return workspace_id, agent_name, False, f"timeout after {TIMEOUT}s"
    except Exception as e:
        return workspace_id, agent_name, False, str(e)


def run_batch(agents: list[tuple[str, str]], dry_run: bool = False) -> list[tuple[str, str, str]]:
    failed = []
    total  = len(agents)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(run_one, ws_id, name, dry_run): (ws_id, name)
            for ws_id, name in agents
        }
        for i, future in enumerate(as_completed(futures), 1):
            ws_id, name, ok, msg = future.result()
            status = "OK" if ok else "FAIL"
            print(f"[{i:02d}/{total}] {status} {ws_id}  ({name})")
            if not ok:
                print(f"         -> {msg}")
                failed.append((ws_id, name, msg))

    return failed


# ── 入口 ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate LLM-AS-Judge files for all agents")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing")
    parser.add_argument("--one", metavar="WORKSPACE_ID", help="Run for a single workspace ID only")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    agents = parse_mapping(MAPPING_FILE)
    if not agents:
        print("ERROR: No agents found in mapping.md", file=sys.stderr)
        sys.exit(1)

    if args.one:
        agents = [(ws, name) for ws, name in agents if ws == args.one]
        if not agents:
            print(f"ERROR: {args.one} not found in mapping.md", file=sys.stderr)
            sys.exit(1)

    print(f"Found {len(agents)} agents. Output dir: {OUTPUT_DIR}")
    print(f"Concurrency: {MAX_WORKERS}  |  Timeout: {TIMEOUT}s per agent\n")

    failed = run_batch(agents, dry_run=args.dry_run)

    # 失败重试（单线程）
    if failed and not args.dry_run:
        print(f"\n--- Retrying {len(failed)} failed agent(s) ---\n")
        retry_agents = [(ws, name) for ws, name, _ in failed]
        still_failed = run_batch(retry_agents, dry_run=False)
    else:
        still_failed = []

    # 汇总
    success_count = len(agents) - len(still_failed)
    print(f"\n{'='*50}")
    print(f"Done.  Success: {success_count}/{len(agents)}")
    if still_failed:
        print(f"Failed ({len(still_failed)}):")
        for ws_id, name, err in still_failed:
            print(f"  - {ws_id} ({name}): {err}")


if __name__ == "__main__":
    main()
