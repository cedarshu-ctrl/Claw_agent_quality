# TOOLS.md - Local Notes

## 工具链

| 工具 | 用途 |
|------|------|
| `web_search` | 搜索历年真题、备考APP、考试大纲 |
| `web_fetch` | 抓取资料页面，提取链接和内容 |
| `exec (python3)` | 运行 study_planner_tool.py 生成/更新/报告 |
| `write_to_file` | 保存 Excel 计划表、Markdown 学习指南 |
| `cron` | 创建每日学习提醒定时任务 |

## ⚠️ 重要映射：automation_update → cron

SKILL.md 中的 `automation_update` 在 OpenClaw 中对应 `cron` 工具。
使用格式示例：
```json
cron { "action": "add", "schedule": { "kind": "cron", "expr": "0 8 * * *" }, "payload": { "kind": "systemEvent", "text": "检查今日学习计划进度" }, "sessionTarget": "isolated", "enabled": true }
```

## study_planner_tool.py 用法

```bash
cd skills/study-planner
python3 scripts/study_planner_tool.py generate \
  --subject "考试名" --days 7 --hours-per-day 3 \
  --output "/path/to/study_plan.xlsx"

python3 scripts/study_planner_tool.py track \
  --date "2026-04-10" --completed 5 --file "/path/to/study_plan.xlsx"

python3 scripts/study_planner_tool.py report \
  --file "/path/to/study_plan.xlsx" --output "weekly_report.md"
```

子命令：generate / track / report / status / export

## 搜索模板

```
web_search("[考试名] 历年真题 下载")
web_search("[考试名] 备考APP推荐 2024")
web_search("[考试名] 考试大纲 重点章节")
```

## 工作流

1. 读取 SKILL.md
2. 收集需求：考试/技能 + 目标时间 + 每日时长 + 当前水平
3. web_search 搜索真题/APP/大纲
4. web_fetch 抓取资料页面
5. python3 study_planner_tool.py generate 生成 Excel 计划表
6. cron 创建每日提醒（早8点）
7. write_to_file 保存 Markdown 学习指南
8. 交付文件 + 更新 USER.md
9. 定期：track 更新进度 → report 生成周报

## ⚠️ 关键规则
- 严禁编造真题/APP！全部来自真实搜索
- Excel 文件必须 write_to_file 保存
- 计划要切实可行，结合用户实际可学时数
- 定期跟进，动态调整计划
