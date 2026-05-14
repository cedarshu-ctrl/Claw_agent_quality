# TOOLS.md - Local Notes

## Tool Chain

| Tool | Purpose |
|------|---------|
| web_search | Search papers by arXiv ID / keyword |
| web_fetch | Fetch paper page, extract title/abstract/method/results |
| exec (python3) | Run data processing scripts |
| write | Save reading notes + comparison Markdown |

## Paper Search

```bash
# Search arXiv by keyword
web_search("LLM paper arXiv 2024")

# Search for survey papers
web_search("research survey NLP arXiv")
```

## arXiv Paper Page

```
https://arxiv.org/abs/{paper_id}
https://arxiv.org/pdf/{paper_id}.pdf
```

## Script Usage

```bash
python3 scripts/arxiv_speed_reader_tool.py run \
  --input "user input (paper link/ID/keyword)" \
  --output "/path/to/output_file.md"
```

## Output Format

```markdown
# 📚 AI论文速读 — 执行报告

## 执行摘要
[一段话摘要]

## 详细结果
### 📄 论文核心提炼
### 🔬 方法论解读
### 📊 实验结果
### ⚠️ 局限性分析

## 对比分析表（如适用）
| 论文 | 方法 | 核心贡献 | 优缺点 |

## 行动建议
[下一步研究建议]
```

## Key Rules

- All data must come from real web_search / web_fetch
- Write output to file, not just chat
- Mark unavailable data as "数据不可用"
