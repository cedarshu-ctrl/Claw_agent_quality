# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## 环境依赖

```bash
pip install pandas openpyxl requests
```

## 工具链

| 工具 | 用途 |
|------|------|
| `web_search` | 搜索最新健身训练方法、动作教程、营养方案 |
| `write_to_file` | 生成运动计划文件、运动记录表 |
| `read_file` | 读取用户上传的体测数据或运动记录 |
| `execute_command` (python3) | 运行 fitness_planner_tool.py 处理数据 |
| `cron` / `automation_update` | 创建每日定时任务（定时推送明日训练计划） |

## 脚本用法

```bash
python3 scripts/fitness_planner_tool.py run \
  --input "用户信息" \
  --output "/path/to/output_file"
```

## 用户信息收集清单

| 项目 | 选项 |
|------|------|
| 健身目标 | 减脂 / 增肌 / 保持 / 康复 |
| 体能水平 | 小白 / 有基础 / 运动爱好者 |
| 可用器材 | 无器材 / 家用 / 健身房 |
| 每周可练天数 | 1-7天 |
| 每次时长 | 15/30/45/60分钟 |
| 伤病/禁忌 | 有 / 无（具体说明） |

## 定时任务配置

推荐每晚 21:00 推送次日训练计划：
- 任务名称：明日运动计划
- 触发时间：每天 21:00
- 内容：执行 fitness-planner skill 的每日计划生成流程

---

Add whatever helps you do your job. This is your cheat sheet.
