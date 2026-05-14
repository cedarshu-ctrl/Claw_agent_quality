# ✍️ 文案大师 Skill —— 全场景文案 + SEO + 脚本

> **定位**：社媒内容生产的"写手引擎"，覆盖图文、短视频脚本、长文等全场景文案，内置 SEO 优化和品牌人设一致性。  
> **核心特性**：IDENTITY 人设（统一品牌语气），全场景模板 + SEO 关键词优化

---

## 一、完整工作流程

```
┌──────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ 选题输入  │───▶│  人设加载     │───▶│  文案生成     │───▶│  SEO优化      │───▶│  多版本输出   │
│(来自策划) │    │ (IDENTITY)   │    │ (场景模板)    │    │ (关键词+结构) │    │ (平台适配)   │
└──────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

### 1.1 流程详解

| 步骤 | 说明 | 输入 | 输出 |
|------|------|------|------|
| **① 选题输入** | 接收选题策划模块的排期选题 | 选题卡片 | 创作Brief |
| **② 人设加载** | 加载品牌 IDENTITY 配置（语气/用词/禁忌） | IDENTITY配置文件 | 风格约束 |
| **③ 文案生成** | 根据场景模板生成初版文案 | Brief + 风格约束 | 初版文案 |
| **④ SEO优化** | 植入关键词、优化标题、结构化内容 | 初版文案 + 关键词库 | SEO优化版 |
| **⑤ 多版本输出** | 适配不同平台格式和字数限制 | 优化版文案 | 各平台版本 |

---

## 二、推荐开源工具与 Skill

### 2.1 ALwrity —— 全流程 AI 内容平台（⭐ 首推）

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/AJaySi/AI-Writer |
| **语言** | Python (Streamlit) |
| **功能** | AI 写作 + SEO 关键词研究 + 内容生成 + 博客管理 + 社交媒体文案 |
| **AI模型** | 支持 OpenAI GPT、Google Gemini 等多模型 |
| **特点** | 内置 SEO 审计、竞品分析、多语言支持、防 AI 检测 |

**安装使用：**
```bash
git clone https://github.com/AJaySi/AI-Writer.git
cd AI-Writer
pip install -r requirements.txt
# 配置 .env 中的 API Key
streamlit run alwrity.py
```

**核心功能：**
- 关键词研究与 SEO 优化
- 多场景文案模板（博客、社媒、广告、邮件）
- AI 内容改写与润色
- 内容质量评分

### 2.2 GPT-Writer 类工具

| 工具 | GitHub | 用途 |
|------|--------|------|
| **gpt-researcher** | https://github.com/assafelovic/gpt-researcher | 深度研究后生成高质量长文 |
| **auto-gpt** | https://github.com/Significant-Gravitas/AutoGPT | 自主完成写作任务链 |
| **langchain** | https://github.com/langchain-ai/langchain | 构建自定义文案生成 Pipeline |

---

## 三、IDENTITY 品牌人设系统

### 3.1 IDENTITY 配置文件

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
  warmth: 7          # 1-10，10为最亲切
  formality: 4       # 1-10，10为最正式
  energy: 8          # 1-10，10为最有激情

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
  
  emoji_style: "适度使用，每段1-2个"
  
sentence_style:
  max_length: 25     # 每句最多字数
  rhythm: "短长交替"  # 句式节奏
  
content_rules:
  - "永远先说结论，再说原因"
  - "每300字必须有一个金句"
  - "禁止使用'小编'自称"
  - "数据必须标注来源"
  
platform_adaptations:
  xiaohongshu:
    tone_adjustment: "+温暖 +闺蜜感"
    emoji_density: "高"
    title_style: "数字+痛点"
  douyin:
    tone_adjustment: "+节奏感 +口语化"
    sentence_length: 15
    hook: "前3秒必须制造冲突"
  weixin:
    tone_adjustment: "+深度 +专业"
    sentence_length: 30
    structure: "总分总"
```

### 3.2 人设一致性检查器

```python
import re
from typing import Dict, List

class IdentityChecker:
    """检查文案是否符合品牌人设"""
    
    def __init__(self, identity_config: Dict):
        self.config = identity_config
    
    def check(self, content: str, platform: str) -> Dict:
        issues = []
        score = 100
        
        # 检查禁用词
        for word in self.config['vocabulary']['avoided']:
            if word in content:
                issues.append(f"❌ 使用了禁用词: '{word}'")
                score -= 10
        
        # 检查句子长度
        max_len = self.config.get('platform_adaptations', {}).get(
            platform, {}
        ).get('sentence_length', self.config['sentence_style']['max_length'])
        
        sentences = re.split(r'[。！？\n]', content)
        for i, s in enumerate(sentences):
            if len(s.strip()) > max_len:
                issues.append(f"⚠️ 第{i+1}句过长({len(s.strip())}字，限{max_len}字)")
                score -= 5
        
        # 检查内容规则
        if "结论" not in content[:100] and "答案" not in content[:100]:
            issues.append("⚠️ 开头未先说结论")
            score -= 5
        
        return {
            'score': max(score, 0),
            'issues': issues,
            'passed': score >= 80
        }
```

---

## 四、全场景文案模板

### 4.1 小红书图文模板

```markdown
## 小红书爆款文案结构

【标题公式】数字 + 痛点/好奇 + 解决方案
示例: "5个让皮肤变好的习惯｜坚持30天效果惊人"

【正文结构】
Hook: 1句话戳中痛点 (带emoji)
├── 要点1: 小标题 + 2-3句说明
├── 要点2: 小标题 + 2-3句说明  
├── 要点3: 小标题 + 2-3句说明
├── (可选) 要点4-5
└── 总结: 金句 + CTA(收藏/关注)

【字数控制】800-1500字为佳
【标签】5-10个相关话题标签
```

### 4.2 抖音/短视频脚本模板

```markdown
## 短视频脚本模板（60秒内）

【Hook (0-3秒)】—— 留住观众
类型: 冲突/反常/提问/数字冲击
示例: "月薪3千和月薪3万的人，区别就在这一点"

【转折 (3-10秒)】—— 建立期待
"但99%的人都不知道..."
"直到我发现了这个方法..."

【干货 (10-45秒)】—— 交付价值
- 方法1: 一句话+演示
- 方法2: 一句话+演示
- 方法3: 一句话+演示

【金句 (45-55秒)】—— 情绪高潮
"记住：___不是___，而是___"

【CTA (55-60秒)】—— 行动号召
"觉得有用的话双击❤️收藏起来"
"关注我，教你更多___"
```

### 4.3 公众号长文模板

```markdown
## 公众号深度文章结构

【标题】悬念/数字/对比 (不超过28字)
【摘要】1-2句提炼核心价值

【开头 (200字)】
├── 场景描述/痛点引入
└── 抛出核心论点

【第一部分 (500字)】
├── 小标题
├── 论点 → 论据 → 案例
└── 小结金句

【第二部分 (500字)】
├── 小标题  
├── 论点 → 论据 → 案例
└── 小结金句

【第三部分 (500字)】
├── 小标题
├── 论点 → 论据 → 案例
└── 小结金句

【结尾 (200字)】
├── 总结升华
├── 金句收尾
└── CTA (关注/转发/留言)
```

---

## 五、SEO 优化模块

### 5.1 关键词研究流程

```
种子关键词 → 扩展长尾词 → 搜索量分析 → 竞争度评估 → 选取目标词 → 植入内容
```

### 5.2 SEO 关键词工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **5118** | 中文关键词挖掘 | https://www.5118.com |
| **千瓜数据** | 小红书关键词分析 | https://www.qiangua.com |
| **巨量算数** | 抖音关键词趋势 | https://trendinsight.oceanengine.com |
| **Google Keyword Planner** | 海外SEO | Google Ads |

### 5.3 SEO 优化检查清单

```python
def seo_check(content: str, target_keywords: list, platform: str) -> dict:
    """SEO优化检查"""
    checks = {}
    
    # 标题包含主关键词
    title = content.split('\n')[0]
    checks['title_keyword'] = any(kw in title for kw in target_keywords[:2])
    
    # 关键词密度 (2%-5%)
    total_words = len(content)
    keyword_count = sum(content.count(kw) for kw in target_keywords)
    density = keyword_count / total_words * 100
    checks['keyword_density'] = 2 <= density <= 5
    checks['density_value'] = f"{density:.1f}%"
    
    # 前100字包含关键词
    checks['early_keyword'] = any(kw in content[:100] for kw in target_keywords)
    
    # 小标题包含关键词
    subtitles = [line for line in content.split('\n') if line.startswith('#')]
    checks['subtitle_keywords'] = any(
        any(kw in sub for kw in target_keywords) for sub in subtitles
    )
    
    # 平台特定检查
    if platform == 'xiaohongshu':
        checks['hashtags'] = content.count('#') >= 5
        checks['emoji'] = bool(re.search(r'[\U0001F300-\U0001F9FF]', content))
    
    return checks
```

---

## 六、文案生成 AI Prompt 库

### 6.1 小红书文案生成

```
你是一位小红书爆款文案写手，请按以下要求创作：

【品牌人设】{从identity.yaml加载}
【选题】{选题标题}
【目标关键词】{关键词1, 关键词2, 关键词3}
【参考爆款】{爆款标题和结构}

输出要求：
1. 标题：3个备选，使用数字+痛点公式
2. 正文：800-1200字，段落清晰，emoji适度
3. 标签：8-10个相关话题标签
4. 关键词密度：主关键词出现3-5次
```

### 6.2 短视频脚本生成

```
你是一位短视频脚本策划大师，请为以下选题撰写60秒脚本：

【选题】{选题标题}
【目标受众】{受众画像}
【核心卖点】{1-3个核心信息}

输出格式：
| 时间 | 画面描述 | 文案/台词 | 字幕 | 音效/BGM |
按此表格输出完整脚本，确保：
- 前3秒有强钩子
- 信息密度适中，每10秒一个节奏点
- 结尾有明确CTA
```

---

## 七、快速启动清单

| 序号 | 步骤 | 预计时间 |
|------|------|----------|
| 1 | 填写 IDENTITY 品牌人设配置文件 | 30 分钟 |
| 2 | 部署 ALwrity 或配置 AI 写作环境 | 20 分钟 |
| 3 | 整理各平台文案模板库 | 30 分钟 |
| 4 | 建立 SEO 关键词库 | 30 分钟 |
| 5 | 用模板+AI 生成第一批文案 | 30 分钟 |
| 6 | 用人设检查器验证一致性 | 10 分钟 |

---

> **使用本 Skill 时的提示词模板**：  
> "请加载以下品牌人设：[粘贴identity.yaml]。为选题'[选题标题]'生成[平台]文案。目标关键词：[词1, 词2]。参考这个爆款结构：[爆款链接/结构描述]。请输出3个标题备选和完整正文。"
