# TOOLS.md - Local Notes

## Tool Chain

| Tool | Purpose |
|------|---------|
| exec (python3) | Run ROI/NPV/IRR financial calculation script |
| web_search | Search market rates, inflation, benchmark data |
| write | Save investment analysis report + calculation results |

## Script Usage

```bash
python3 scripts/roi_analyzer_tool.py run \
  --input "user input (investment details)" \
  --output "/path/to/output_file.md"
```

## Financial Metrics

| Metric | Description |
|--------|-------------|
| ROI | (收益 - 成本) / 成本 × 100% |
| NPV | Σ(收益_t / (1+r)^t) - 初始投资 |
| IRR | 使 NPV = 0 的折现率 |
| 回收期 | 累计收益 = 初始投资所需时间 |

## Report Output Format

```markdown
# 📊 ROI精算师 — 投资分析报告

## 执行摘要
[一段话结论]

## 参数输入
| 参数 | 值 |
|------|-----|
| 初始投资 | XX 万 |
| 预期年收益 | XX 万 |
| 投资周期 | X 年 |
| 折现率 | X% |

## 财务指标
| 指标 | 值 | 评价 |
|------|-----|------|
| ROI | XX% | [优/良/差] |
| NPV | XX 万 | [正值/负值] |
| IRR | XX% | [高于/低于折现率] |
| 回收期 | X 年 X 月 | [快/中/慢] |

## 敏感性分析
[变量±10%/±20% 情景]

## 多方案对比（如适用）
[对比表]

## 风险提示
[具体风险]
```

## Key Rules

- All data must come from user input or real market data
- Write output to file, not just chat
- Mark unavailable data as "数据不可用"
- Reference skill: roi-calculator
