---
name: bi-report-auto
description: "BI 数据报表自动生成。BI 数据报表自动生成 - 报表模板设计、数据自动刷新、定时发送 This skill should be used when the user asks about BI 数据报表自动生成. Keywords: 生成报表, BI报表, 数据报告."
---

# BI 数据报表自动生成

> BI 数据报表自动生成 - 报表模板设计、数据自动刷新、定时发送

## 前置依赖

```bash
pip install pandas openpyxl
```

## 核心能力

### 能力1：读取数据源文件（read_file，Excel/CSV）

用 `web_fetch` 抓取页面内容 / 用 `read_file` 读取文件。

### 能力2：按指定维度汇总计算（execute_command + Python/pandas）

运行脚本进行数据分析处理。

### 能力3：设计报表模板（表头/格式/图表）

用 `read_file` 读取数据文件和报表模板，用 `execute_command` 运行pandas进行数据聚合和统计分析。

### 能力4：生成格式化 Excel 报表（openpyxl）

用 `write_to_file` 生成文件。

### 能力5：支持定时刷新和发送

用 `automation_update` 创建定时任务。

## 使用流程

### 步骤 1：收集用户需求

向用户确认以下信息（如果未主动提供）：
- 数据源文件路径（CSV/Excel/数据库导出）
- 报表类型（日报/周报/月报/季报）
- 关键指标有哪些？
- 报表模板（如有，提供路径）
- 是否需要定时自动生成？

### 步骤 2：运行脚本处理数据

```bash
python3 scripts/bi_report_auto_tool.py run \
  --input "用户提供的输入" \
  --output "/path/to/output_file"
```

读取脚本输出的结果，确认数据处理成功。

### 步骤 3：生成最终产出

基于脚本输出和搜索到的资源，用 `write_to_file` 生成以下文件：

- **格式化 Excel 报表**
- **数据汇总文件**

输出格式要求：Excel 格式化报表 + 汇总数据

### 步骤 4：设置定时任务

用 `automation_update` 创建定时任务：
```
automation_update:
  name="BI 数据报表自动生成"
  rrule=FREQ=DAILY;BYHOUR=9;BYMINUTE=0
  prompt="执行BI 数据报表自动生成skill的定时任务"
```

### 步骤 5：汇总交付

向用户展示：
1. 生成的文件路径和内容摘要
2. 搜集到的资源链接列表
3. 关键发现和建议
4. 定时任务创建确认

## 输出格式

```markdown
# 📋 BI 数据报表自动生成 — 执行报告

**生成时间**: YYYY-MM-DD HH:MM
**目标用户**: 数据分析师、业务负责人、运营总监

## 执行摘要
[基于实际执行结果的一段话摘要]

## 详细结果

### 📊 生成的文件
| 文件名 | 类型 | 说明 |
|--------|------|------|
| [文件名] | [类型] | [说明] |

### 🔗 资源链接
| 名称 | 链接 | 说明 |
|------|------|------|
| [资源] | [URL] | [说明] |

## 行动建议
[具体的下一步建议]
```

## 验收标准

- ✅ 数据汇总准确
- ✅ 报表格式专业
- ✅ Excel 可用
- ✅ 支持复用

## 场景化适配

根据业务需求（日报/周报/月报）调整报表模板


## 依赖 Skills

本 Skill 参考以下已有 Skill 的能力进行增强：
- **bi-report**

## 注意事项

- 所有数据必须来自 `web_search` / `web_fetch` 的真实搜索结果，**严禁编造数据**
- 数据缺失时标注"数据不可用"而非猜测
- 报告必须保存为文件（`write_to_file`），不能只在对话中输出
- 建议结合人工判断使用，AI 分析仅供参考
