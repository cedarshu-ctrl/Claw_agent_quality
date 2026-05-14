# CompetitorSmart — AI 竞品深度分析 Agent

> 基于 LangGraph ReAct Agent 的开源竞品情报工具，自动搜索、抓取、推理，生成 11 模块深度 Markdown 竞品分析报告。专为产品经理 / 跨境电商运营设计。

---

## 来源

- **小红书笔记**：@0xtomoon「制作并开源了一个竞品分析agent」
- **GitHub**：https://github.com/t0moon/competitorsmart
- **作者**：t0moon

---

## 这个 Skill 解决什么问题？

跨境电商在进入新品类、调整竞争策略时，需要一份覆盖市场、竞品、商业模式、增长策略的**深度分析报告**。传统做法需要人工搜索几十个网页、整理表格、写 PPT，耗时 2-3 天。

CompetitorSmart 用一条命令，让 AI Agent 自动完成「搜索 → 抓取 → 推理 → 成文」全流程，15-30 分钟输出一份专业级 11 模块报告。

---

## 技术架构

```
输入（竞品名称/JSON）
        ↓
┌────────────────────────────┐
│   LangGraph ReAct Agent    │
│                            │
│  ┌──────────┐ ┌─────────┐ │
│  │DuckDuckGo│→│Web Scraper│ │
│  │  搜索    │ │ 网页抓取 │ │
│  └────┬─────┘ └────┬─────┘ │
│       └──────┬─────┘       │
│              ↓             │
│     ┌────────────────┐     │
│     │  智谱 GLM-4.7  │     │
│     │  推理 & 成文   │     │
│     └────────────────┘     │
└────────────┬───────────────┘
             ↓
   outputs/agent/*.md
   （11模块深度报告）
```

**核心组件：**
| 组件 | 技术 | 说明 |
|:---|:---|:---|
| Agent 框架 | LangGraph ReAct | 搜索→抓取→推理循环，自主决定下一步 |
| 搜索引擎 | DuckDuckGo | 免费，无需额外 API Key |
| AI 模型 | 智谱 GLM-4.7 | OpenAI 兼容接口，中英文能力强 |
| 网页抓取 | 内置 Scraper | 自动提取网页正文内容 |

**关键依赖：**
- `langgraph` — Agent 编排
- `langchain-openai` — 模型调用
- `duckduckgo-search` — 搜索接口

---

## 报告包含的 11 个分析模块

这是 CompetitorSmart 最核心的价值。每份报告固定包含以下 11 个章节（定义在 `src/agent/graph.py` 的 SYSTEM_PROMPT 中），关键结论都附带来源 URL：

| # | 模块 | 内容 | 跨境电商用途 |
|:---:|:---|:---|:---|
| 1 | **报告概述** | 全局摘要、核心发现 | 快速给团队/老板汇报 |
| 2 | **市场与赛道分析** | 市场规模、增长趋势、赛道格局 | 判断品类天花板，决定是否进入 |
| 3 | **竞品选择与分层** | 直接/间接/替代竞品分级 | 明确谁是真正对手 |
| 4 | **核心能力拆解** | 每个竞品单独分析（产品/技术/体验） | 学习对手强项、找借鉴点 |
| 5 | **商业模式分析** | 收入模式、定价策略、成本结构 | 制定自己的定价和盈利模型 |
| 6 | **增长与分发策略** | 获客渠道、营销打法、增长飞轮 | 学习流量策略、找差异化获客 |
| 7 | **用户与场景分析** | 用户画像、使用场景、购买旅程 | 精准定位目标人群，优化卖点 |
| 8 | **优劣势对比** | SWOT 矩阵、功能对比表 | 找到竞品弱点作为切入点 |
| 9 | **关键差异与壁垒** | 技术壁垒、品牌壁垒、网络效应 | 评估进入难度、规划长期策略 |
| 10 | **机会点与策略建议** | 市场空白、未满足需求、行动建议 | 直接指导选品和差异化方向 |
| 11 | **数据附录** | 来源 URL 列表、引用数据 | 报告可追溯，支持深挖 |

---

## 安装与配置

### 环境要求

- Python 3.10+
- 智谱 AI API Key（免费注册：https://open.bigmodel.cn/）

### 安装步骤

```bash
# 1. 克隆仓库
git clone https://github.com/t0moon/competitorsmart.git
cd competitorsmart

# 2. 安装依赖
pip install -r requirements.txt

# 如果只需核心依赖：
pip install langgraph langchain-openai duckduckgo-search

# 3. 配置环境变量
cp .env.example .env
```

### 环境变量配置（.env）

```env
# 必填：至少填一个（支持 KEY_1 到 KEY_4 做负载均衡）
ZHIPU_API_KEY_1=your_api_key_here

# 可选：自定义 API 地址
# ZHIPU_API_BASE_URL=https://open.bigmodel.cn/api/paas/v4/
```

### 项目文件结构

```
competitorsmart/
├── main.py                      # 入口文件
├── competitors_input.json       # 竞品输入（JSON格式）
├── requirements.txt             # 依赖列表
├── .env.example                 # 环境变量模板
├── src/
│   ├── constants.py             # 模型名称和 API Base
│   ├── config.py                # Config 类，加载输入
│   └── agent/
│       └── graph.py             # ReAct Agent 核心 + 11模块 Prompt
└── outputs/
    └── agent/                   # 报告输出目录
```

---

## 使用方法

### 方式一：命令行快速运行

```bash
# 逗号分隔竞品名 + 赛道描述
python main.py --competitors "BlendJet 2,NutriBullet Go,Hamilton Beach" --market "便携式搅拌杯"
```

### 方式二：JSON 输入文件（推荐，上下文更丰富）

编辑 `competitors_input.json`：

```json
{
  "market": "便携式个人搅拌杯",
  "product_category": "小家电 / 厨房电器",
  "geography": "美国",
  "our_product": {
    "name": "MyBlender Pro",
    "description": "20oz便携搅拌杯，Type-C充电，IP68防水",
    "website": "https://myblender.com"
  },
  "competitors": [
    {
      "name": "BlendJet 2",
      "category": "direct",
      "website": "https://blendjet.com",
      "website_copy": "The Original Portable Blender...",
      "sales_notes": "Amazon BSR#1, 月销10万+"
    },
    {
      "name": "NutriBullet Go",
      "category": "direct",
      "website": "https://nutribullet.com/go"
    },
    {
      "name": "Hamilton Beach Personal Blender",
      "category": "indirect",
      "website": "https://hamiltonbeach.com"
    }
  ]
}
```

运行：

```bash
python main.py --input competitors_input.json
```

### 方式三：验证配置（不调用 API）

```bash
python main.py --dry-run
```

---

## 输出示例

报告自动保存到 `outputs/agent/` 目录，Markdown 格式：

```markdown
# 竞品分析报告：便携式搅拌杯市场

## 1. 报告概述
便携式搅拌杯市场在2025年达到$8.2亿规模，年增长率12%...
→ [来源: Grand View Research](https://...)

## 2. 市场与赛道分析
### 市场规模
全球便携式搅拌杯 TAM 约$12亿，其中北美占比38%...

## 3. 竞品选择与分层
| 竞品 | 分层 | 市场份额 |
|---|---|---|
| BlendJet 2 | 直接竞品 | ~25% |
| NutriBullet Go | 直接竞品 | ~15% |

## 4. 核心能力拆解
### BlendJet 2
- 产品力：6刀片设计，470ml，USB-C充电
- 差异化：自清洁功能，DTC品牌故事
...

## 5-10. [商业模式/增长策略/用户场景/SWOT/壁垒/机会]
...

## 11. 数据附录
1. [Grand View Research - Portable Blender Market](https://...)
2. [Amazon Best Sellers - Portable Blenders](https://...)
...
```

---

## 跨境电商实战场景

### 场景 A：新品类进入决策

```
"我想做宠物智能喂食器，帮我分析美国市场的竞争格局"

python main.py --competitors "PetSafe,WOPET,PETLIBRO,Catit" --market "智能宠物喂食器"

→ 输出：市场规模/竞品分层/定价分析/进入壁垒/机会点
→ 决策：是否进入 + 差异化方向
```

### 场景 B：竞品策略调整

```
"我的搅拌杯销量下滑，分析一下竞品最近做了什么"

# 在 JSON 中添加 sales_notes 字段提供上下文
"sales_notes": "最近3个月BSR从#5跌到#15，主要竞品在做大促"

→ 输出：竞品增长策略变化/新品上架分析/定价调整/建议对策
```

### 场景 C：融资/汇报用竞品报告

```
"我需要给投资人看一份专业的竞品分析"

# 用完整 JSON 输入，提供尽可能多的 website_copy 和 sales_notes
→ 输出：11模块完整报告，带来源URL，可直接作为附件
```

---

## 安全注意事项

1. **不要将 `.env` 提交到 Git**（仓库已配置 `.gitignore`）
2. 可启用预提交钩子防止误提交密钥：
   ```bash
   git config core.hooksPath githooks
   ```
3. API Key 支持 1-4 个轮换，减少单 Key 限频风险
4. DuckDuckGo 搜索无需 API Key，但有频率限制，大批量分析建议间隔运行

---

## 与 ClawHub Skills 的协同

| 阶段 | 用 CompetitorSmart | 用 ClawHub Skill |
|:---|:---|:---|
| 进入新品类 | ✅ 生成11模块深度报告 | — |
| 日常快速对比 | — | ✅ `competitive-analysis` |
| 价格持续监控 | — | ✅ `price-tracker` |
| 竞品动态追踪 | — | ✅ `competitor-monitoring` |
| Amazon ASIN 分析 | — | ✅ `amazon-competitor-analyzer` |

**最佳实践**：CompetitorSmart 做「入场前深度调研」，ClawHub Skills 做「入场后持续监控」。
