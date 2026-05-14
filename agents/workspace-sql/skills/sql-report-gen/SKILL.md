---
name: sql-report-gen
description: " SQL自动生成与报表工具。不会写SQL？用自然语言描述需求自动生成查询语句 This skill should be used when the user asks about  SQL自动生成与报表工具. Keywords: 查数据, 写SQL, 生成报表."
---

#  SQL自动生成与报表工具

> 不会写SQL？用自然语言描述需求自动生成查询语句

## 前置依赖

```bash
pip install pandas openpyxl
```

## 核心能力

### 能力1：理解我的数据查询需求

用 `read_file` 读取数据库结构文件，根据用户需求自动生成SQL查询语句；用 `execute_command` 运行SQL生成报表数据。

### 能力2：自动生成 SQL 语句（含注释）

用 `write_to_file` 生成文件。

### 能力3：执行 SQL（execute_command）并展示结果

用 `read_file` 读取数据库结构文件，根据用户需求自动生成SQL查询语句；用 `execute_command` 运行SQL生成报表数据。

### 能力4：将结果导出为 Excel 报表

用 `read_file` 读取数据库结构文件，根据用户需求自动生成SQL查询语句；用 `execute_command` 运行SQL生成报表数据。

### 能力5：提供 SQL 优化建议

用 `read_file` 读取数据库结构文件，根据用户需求自动生成SQL查询语句；用 `execute_command` 运行SQL生成报表数据。

## 使用流程

### 步骤 1：收集用户需求

向用户确认以下信息（如果未主动提供）：
- 数据库类型（MySQL/PostgreSQL/SQLite/其他）
- 数据表结构（提供DDL或描述）
- 需要什么样的报表？（日报/周报/月报/自定义）
- 关注哪些指标？

### 步骤 2：运行脚本处理数据

```bash
python3 scripts/sql_report_gen_tool.py run \
  --input "用户提供的输入" \
  --output "/path/to/output_file"
```

读取脚本输出的结果，确认数据处理成功。

### 步骤 3：生成最终产出

基于脚本输出和搜索到的资源，用 `write_to_file` 生成以下文件：

- **SQL 语句文件**
- **Excel 数据报表**

输出格式要求：SQL 语句 + 查询结果表格 + Excel 文件

### 步骤 4：汇总交付

向用户展示：
1. 生成的文件路径和内容摘要
2. 搜集到的资源链接列表
3. 关键发现和建议

## 输出格式

```markdown
# 📋  SQL自动生成与报表工具 — 执行报告

**生成时间**: YYYY-MM-DD HH:MM
**目标用户**: 运营人员、产品经理、数据分析师

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

- ✅ SQL 语法正确
- ✅ 查询结果准确
- ✅ Excel 报表可用
- ✅ 附优化建议

## 场景化适配

根据数据库类型（MySQL/PostgreSQL/SQLite）调整语法


## 依赖 Skills

本 Skill 参考以下已有 Skill 的能力进行增强：
- **db-assistant**

## 注意事项

- 所有数据必须来自 `web_search` / `web_fetch` 的真实搜索结果，**严禁编造数据**
- 数据缺失时标注"数据不可用"而非猜测
- 报告必须保存为文件（`write_to_file`），不能只在对话中输出
- 建议结合人工判断使用，AI 分析仅供参考
