# 品牌人设系统

品牌人设配置文件格式与一致性检查器。

---

## identity.yaml 配置模板

```yaml
# identity.yaml —— 品牌人设配置
brand:
  name: "你的品牌名"
  slogan: "品牌口号"

persona:
  role: "专业且亲和的行业导师"
  age_feel: "28-35岁的成熟感"

tone:
  primary: "专业自信"
  secondary: "轻松幽默"
  warmth: 7       # 1-10，10为最亲切
  formality: 4    # 1-10，10为最正式
  energy: 8       # 1-10，10为最有激情

vocabulary:
  preferred:
    - "搞定"
    - "宝藏"
    - "硬核"
    - "实测"
  avoided:
    - "非常好"      # 太普通
    - "众所周知"    # 太套路
    - "不得不说"    # 太油腻
    - "小编"        # 禁止自称

emoji_style: "适度使用，每段1-2个"

sentence_style:
  max_length: 25    # 每句最多字数（默认）
  rhythm: "短长交替"

content_rules:
  - "永远先说结论，再说原因"
  - "每300字必须有一个金句"
  - "数据必须标注来源"

platform_adaptations:
  xiaohongshu:
    tone_adjustment: "+温暖 +闺蜜感"
    emoji_density: "高"
    sentence_length: 20
    title_style: "数字+痛点"
  douyin:
    tone_adjustment: "+节奏感 +口语化"
    sentence_length: 15
    hook: "前3秒必须制造冲突"
  weixin:
    tone_adjustment: "+深度 +专业"
    sentence_length: 30
    structure: "总分总"
  weibo:
    tone_adjustment: "+话题感 +短平快"
    sentence_length: 20
    max_total: 140
```

---

## IdentityChecker 人设一致性检查器

```python
import re
from typing import Dict, List

class IdentityChecker:
    """检查文案是否符合品牌人设，返回得分和问题清单"""

    def __init__(self, identity_config: Dict):
        self.config = identity_config

    def check(self, content: str, platform: str) -> Dict:
        issues = []
        score = 100

        vocab = self.config.get('vocabulary', {})

        # 检查禁用词
        for word in vocab.get('avoided', []):
            if word in content:
                issues.append(f"❌ 禁用词: '{word}'")
                score -= 10

        # 检查句子长度
        platform_cfg = self.config.get('platform_adaptations', {}).get(platform, {})
        max_len = platform_cfg.get(
            'sentence_length',
            self.config.get('sentence_style', {}).get('max_length', 25)
        )
        sentences = re.split(r'[。！？\n]', content)
        long_sentences = [
            (i + 1, len(s.strip()))
            for i, s in enumerate(sentences)
            if len(s.strip()) > max_len
        ]
        if long_sentences:
            for idx, length in long_sentences[:3]:  # 最多报3条
                issues.append(f"⚠️ 第{idx}句过长（{length}字，限{max_len}字）")
                score -= 3

        # 检查结论前置
        first_100 = content[:100]
        conclusion_words = ['是', '就是', '关键是', '答案是', '原因是', '方法是']
        if not any(w in first_100 for w in conclusion_words):
            issues.append("⚠️ 开头未明确给出结论，建议结论前置")
            score -= 5

        # 检查金句密度（每300字至少1个）
        total_chars = len(content)
        expected_quotes = total_chars // 300
        # 用感叹号和短句作为金句的粗略代理
        exclamations = content.count('！') + content.count('!')
        if exclamations < expected_quotes:
            issues.append(f"⚠️ 金句密度不足（每300字至少1个有力表达）")
            score -= 5

        # 平台特定检查
        if platform == 'xiaohongshu':
            hashtag_count = content.count('#')
            if hashtag_count < 5:
                issues.append(f"⚠️ 话题标签仅{hashtag_count}个，建议8-10个")
                score -= 5
            if not re.search(r'[\U0001F300-\U0001F9FF]', content):
                issues.append("⚠️ 小红书文案建议添加emoji增强亲和力")
                score -= 3

        return {
            'score': max(score, 0),
            'issues': issues,
            'passed': score >= 80,
            'summary': f"人设得分：{max(score, 0)}/100 {'✅ 通过' if score >= 80 else '❌ 需修改'}"
        }
```

---

## 使用方式

```python
import yaml

# 加载人设配置
with open('identity.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

checker = IdentityChecker(config)

# 检查文案
result = checker.check(content="你的文案内容", platform="xiaohongshu")
print(result['summary'])
for issue in result['issues']:
    print(issue)
```
