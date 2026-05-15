# TOOLS.md - Local Notes

## 工具链

| 工具 | 用途 |
|------|------|
| `web_search` | 搜索 MBTI 配对数据库，获取真实配对指数和相处建议 |
| `web_fetch` | 抓取权威 MBTI 分析网站内容 |
| `exec (python3)` | 运行 mbti_matcher_tool.py 生成报告模板 |
| `write_to_file` | 生成配对分析报告（Markdown）|

## mbti_matcher_tool.py 用法

```bash
cd skills/mbti-matcher
python3 scripts/mbti_matcher_tool.py run \
  --input "双方MBTI类型和分析场景" \
  --output "/path/to/output.md"
```

子命令：
- `run` — 执行主工作流，生成报告模板
- `status` — 查看当前 skill 状态
- `export` — 导出已有结果

## 工作流

1. 读取 SKILL.md
2. 询问双方 MBTI 类型 + 分析场景
3. web_search 搜索配对数据（严禁编造）
4. web_fetch 抓取详细内容
5. python3 mbti_matcher_tool.py run 生成报告模板
6. 基于真实数据填充报告内容
7. write_to_file 保存报告
8. 交付 + 更新 USER.md

## ⚠️ 关键规则
- 严禁编造数据！所有分析必须基于 web_search/web_fetch 真实结果
- 数据缺失时标注"数据不可用"
- 报告必须用 write_to_file 保存，不能仅在对话中输出
