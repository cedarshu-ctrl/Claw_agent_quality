# TOOLS.md - Local Notes

## 工具链

| 工具 | 用途 |
|------|------|
| `web_fetch` | 抓取链接页面正文和关键信息 |
| `web_search` | 补充搜索相关背景信息 |
| `read` | 读取本地文件内容（路径需绝对路径） |
| `write` | 写入/生成结构化 Markdown 文档 |
| `exec (python3)` | 运行 doc_organizer_tool.py |

## doc_organizer_tool.py 用法

```bash
cd skills/doc-organizer
python3 scripts/doc_organizer_tool.py run \
  --input "资料描述或关键词" \
  --output "/path/to/output_file.md"
```

子命令：run / status / export

## 输入方式优先级

1. **用户提供链接列表** → web_fetch 逐条抓取
2. **用户提供本地文件路径** → read 读取
3. **用户直接粘贴内容** → 直接处理

## 文档结构模板

```markdown
# 📂 [主题] 资料整理报告

## 📋 目录大纲
[自动生成的章节导航]

## 📰 分类整理
### [主题A]
- [内容摘要] — 来源：[链接/文件]
### [主题B]
- [内容摘要] — 来源：[链接/文件]

## 🔑 关键词索引
| 关键词 | 出现位置 | 频次 |
|--------|---------|------|
| | | |

## ⭐ 核心观点汇总
[提炼出的主要观点和关键数据]
```

## ⚠️ 关键规则
- 所有内容必须来自 web_fetch / read 真实获取
- 数据缺失标注"数据不可用"，不猜测
- 文档必须 write_to_file 保存
