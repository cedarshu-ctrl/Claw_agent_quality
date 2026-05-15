# SEO工具与优化检查器

---

## 关键词研究工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **5118** | 中文关键词挖掘、长尾词扩展 | https://www.5118.com |
| **千瓜数据** | 小红书关键词分析、热门话题 | https://www.qiangua.com |
| **巨量算数** | 抖音关键词趋势、热点追踪 | https://trendinsight.oceanengine.com |
| **Google Keyword Planner** | 海外SEO、搜索量数据 | Google Ads后台 |

## 关键词研究流程

```
种子关键词 → 扩展长尾词 → 搜索量分析 → 竞争度评估 → 选取目标词 → 植入内容
```

**选词原则：**
- 主关键词：搜索量高、与选题强相关，1-2个
- 长尾词：搜索量中等、竞争度低，3-5个
- 话题标签：平台热门话题，8-10个（小红书）/ 3-5个（抖音）

---

## SEO优化检查器

```python
import re

def seo_check(content: str, target_keywords: list, platform: str) -> dict:
    """SEO优化检查，返回各项指标和建议"""
    checks = {}
    issues = []

    lines = content.split('\n')
    title = lines[0].strip('#').strip() if lines else ''

    # 标题包含主关键词
    checks['title_keyword'] = any(kw in title for kw in target_keywords[:2])
    if not checks['title_keyword']:
        issues.append(f"⚠️ 标题未包含主关键词: {target_keywords[:2]}")

    # 关键词密度 (2%-5%)
    total_chars = len(content)
    keyword_count = sum(content.count(kw) for kw in target_keywords)
    density = keyword_count / total_chars * 100 if total_chars > 0 else 0
    checks['keyword_density'] = 2 <= density <= 5
    checks['density_value'] = f"{density:.1f}%"
    if not checks['keyword_density']:
        issues.append(f"⚠️ 关键词密度 {density:.1f}%，目标范围 2%-5%")

    # 前100字包含关键词
    checks['early_keyword'] = any(kw in content[:100] for kw in target_keywords)
    if not checks['early_keyword']:
        issues.append("⚠️ 前100字未出现关键词，建议提前植入")

    # 小标题包含关键词
    subtitles = [line for line in lines if line.startswith('#')]
    checks['subtitle_keywords'] = any(
        any(kw in sub for kw in target_keywords) for sub in subtitles
    )

    # 平台特定检查
    if platform == 'xiaohongshu':
        hashtag_count = content.count('#')
        checks['hashtags'] = hashtag_count >= 5
        checks['emoji'] = bool(re.search(r'[\U0001F300-\U0001F9FF]', content))
        if hashtag_count < 5:
            issues.append(f"⚠️ 话题标签仅 {hashtag_count} 个，建议8-10个")

    elif platform == 'douyin':
        hashtag_count = content.count('#')
        checks['hashtags'] = hashtag_count >= 3
        if hashtag_count < 3:
            issues.append(f"⚠️ 话题标签仅 {hashtag_count} 个，建议3-5个")

    score = sum(1 for v in checks.values() if v is True) / max(
        sum(1 for v in checks.values() if isinstance(v, bool)), 1
    ) * 100

    return {
        'score': round(score),
        'checks': checks,
        'issues': issues,
        'passed': score >= 80
    }
```

## SEO优化清单

在输出文案前，逐项确认：

- [ ] 标题前15字包含主关键词
- [ ] 正文前100字出现主关键词
- [ ] 至少一个小标题包含关键词
- [ ] 关键词密度在2%-5%之间
- [ ] 小红书：8-10个话题标签
- [ ] 抖音：3-5个热门话题
- [ ] 公众号：摘要包含核心关键词
