# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## 环境依赖

```bash
pip install pandas openpyxl
```

## 工具链

| 工具 | 用途 |
|------|------|
| `web_search` | 搜索目标实现的常见路径、最佳实践、参考资源 |
| `write_to_file` | 生成目标计划文件、进度追踪表、复盘报告 |
| `read_file` | 读取现有目标计划或历史打卡记录 |
| `exec` (python3) | 运行 goal_decomposer_tool.py 处理数据 |

## 脚本用法

```bash
python3 skills/goal-decomposer/scripts/goal_decomposer_tool.py run \
  --input "用户目标描述" \
  --output "/path/to/output_file"
```

## 目标拆解流程

```
大目标
  ↓ SMART 原则拆解
阶段里程碑（月/周）
  ↓
每周子任务（可执行、可衡量）
  ↓
每日任务（明天就能做）
  ↓
打卡追踪 → 周复盘 → 动态调整
```

## SMART 原则检查

| 维度 | 问题 |
|------|------|
| S - 具体 | 能用一句话说清楚要做什么吗？ |
| M - 可衡量 | 怎么知道自己做到了？有什么数字指标？ |
| A - 可达成 | 以你目前的情况，这个目标现实吗？ |
| R - 相关 | 这个目标真的重要吗？为什么要实现它？ |
| T - 时限 | 什么时候要完成？有明确截止日期吗？ |

## 打卡追踪指标

- 每日完成率（%）
- 连续打卡天数
- 本周 vs 上周对比
- 偏离度（计划 vs 实际）

---

Add whatever helps you do your job. This is your cheat sheet.
