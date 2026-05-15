---
name: 数据分析
description: |
  社媒内容生产的数据复盘引擎，自动采集发布数据，生成日报/周报，拆解爆款因子，记忆历史趋势。
  触发词：数据分析、日报、周报、爆款复盘、趋势分析、报告生成、数据看板。
---

# 📊 数据分析 Skill —— 日报/周报与爆款复盘

> **定位**：社媒内容生产的"复盘引擎"，自动采集发布数据，生成日报/周报，拆解爆款因子，记忆历史趋势。  
> **核心特性**：记忆历史数据趋势 + 自动报告生成 + 爆款因子分析

---

## 一、完整工作流程

```
数据采集(各平台) → 数据清洗存储 → 指标计算 → 报告生成(日/周报) → 爆款复盘 → 策略优化
```

| 步骤 | 说明 | 输入 | 输出 |
|------|------|------|------|
| **① 数据采集** | 从各平台抓取发布后的互动数据 | 平台账号 | 原始数据 |
| **② 数据清洗** | 统一格式、去噪、入库 | 原始数据 | 结构化数据 |
| **③ 指标计算** | 计算互动率、完播率、涨粉等 | 结构化数据 | 指标表 |
| **④ 报告生成** | 自动生成日报/周报/月报 | 指标表 | 可视化报告 |
| **⑤ 爆款复盘** | 识别爆款、分析成功因子 | 历史数据 | 复盘洞察 |
| **⑥ 策略优化** | 反馈给选题策划，优化后续内容 | 洞察 | 策略调整 |

---

## 二、推荐开源工具

### 2.1 MediaCrawler —— 多平台数据采集

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/NanmiCoder/MediaCrawler |
| **用途** | 抓取自己账号和竞品的帖子数据（点赞/评论/转发/播放量） |

### 2.2 Grafana —— 数据可视化仪表盘

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/grafana/grafana |
| **用途** | 构建社媒数据看板，实时监控各平台表现 |

```bash
docker run -d -p 3000:3000 grafana/grafana
# 访问 http://localhost:3000 (admin/admin)
```

### 2.3 Metabase —— 简易 BI 分析

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/metabase/metabase |
| **功能** | 零代码 BI 工具，SQL 查询+可视化，适合非技术人员 |

```bash
docker run -d -p 3001:3000 metabase/metabase
```

---

## 三、核心数据指标体系

### 3.1 基础指标

| 指标 | 计算公式 | 优秀基准 |
|------|----------|----------|
| **互动率** | (点赞+评论+转发) / 曝光量 | >5% |
| **完播率** | 完整播放数 / 播放数 | >30% |
| **收藏率** | 收藏数 / 曝光量 | >3% |
| **涨粉率** | 新增粉丝 / 曝光量 | >0.5% |
| **转化率** | 点击链接数 / 曝光量 | >2% |

### 3.2 爆款识别规则

```python
def identify_viral(post_data: dict, history_avg: dict) -> bool:
    """爆款判定：互动量超过历史均值 3 倍"""
    engagement = (post_data['likes'] + post_data['comments'] * 2 
                  + post_data['shares'] * 3)
    avg_engagement = (history_avg['likes'] + history_avg['comments'] * 2 
                      + history_avg['shares'] * 3)
    return engagement > avg_engagement * 3
```

---

## 四、自动化报告生成

### 4.1 日报模板

```python
from datetime import datetime
import pandas as pd

def generate_daily_report(data: pd.DataFrame, date: str = None):
    date = date or datetime.now().strftime('%Y-%m-%d')
    today = data[data['date'] == date]
    
    report = f"""# 📊 社媒日报 | {date}

## 今日概览
| 指标 | 数值 | 环比昨日 |
|------|------|----------|
| 总曝光 | {today['views'].sum():,} | {_delta(today, data, 'views')} |
| 总互动 | {today['engagement'].sum():,} | {_delta(today, data, 'engagement')} |
| 新增粉丝 | {today['new_followers'].sum():,} | {_delta(today, data, 'new_followers')} |
| 发布内容 | {len(today)} 条 | — |

## 今日表现 TOP3
{_top3(today)}

## 待优化内容
{_low_performers(today)}

## 明日建议
- 基于今日数据，建议明日选题方向：{_suggest_topic(today)}
- 建议发布时间：{_suggest_time(data)}"
    return report
```

### 4.2 周报模板

```markdown
# 📊 社媒周报 | {start_date} ~ {end_date}

## 本周概览
| 指标 | 本周 | 上周 | 环比 |
|------|------|------|------|
| 总曝光 | X | Y | ±Z% |
| 总互动 | X | Y | ±Z% |
| 新增粉丝 | X | Y | ±Z% |
| 发布数量 | X条 | Y条 | — |
| 互动率 | X% | Y% | ±Z% |

## 本周 TOP5 内容
[按互动量排序的内容列表]

## 爆款分析
[爆款内容的成功因子拆解]

## 各平台表现对比
[按平台分组的数据对比]

## 下周优化建议
1. 选题方向：...
2. 发布时间：...
3. 内容格式：...
```

---

## 五、历史趋势记忆

### 5.1 数据存储方案

```python
import sqlite3
from datetime import datetime

class SocialMetricsDB:
    def __init__(self, db_path="social_metrics.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id TEXT PRIMARY KEY, platform TEXT, title TEXT, publish_time TIMESTAMP,
                views INTEGER DEFAULT 0, likes INTEGER DEFAULT 0, comments INTEGER DEFAULT 0,
                shares INTEGER DEFAULT 0, saves INTEGER DEFAULT 0, new_followers INTEGER DEFAULT 0,
                tags TEXT, content_type TEXT, updated_at TIMESTAMP
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS daily_summary (
                date TEXT, platform TEXT, total_views INTEGER, total_engagement INTEGER,
                total_followers INTEGER, post_count INTEGER, PRIMARY KEY (date, platform)
            )
        """)
    
    def upsert_post(self, post: dict):
        self.conn.execute("""
            INSERT OR REPLACE INTO posts 
            (id, platform, title, publish_time, views, likes, comments, 
             shares, saves, new_followers, tags, content_type, updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (post['id'], post['platform'], post['title'], 
              post['publish_time'], post['views'], post['likes'],
              post['comments'], post['shares'], post['saves'],
              post['new_followers'], ','.join(post.get('tags', [])),
              post['content_type'], datetime.now()))
        self.conn.commit()
    
    def get_trend(self, platform: str, metric: str, days: int = 30):
        return self.conn.execute(f"""
            SELECT date, {metric} FROM daily_summary 
            WHERE platform=? ORDER BY date DESC LIMIT ?
        """, (platform, days)).fetchall()
```

### 5.2 趋势分析

```python
def analyze_trend(metrics_db, platform, days=30):
    trend = metrics_db.get_trend(platform, 'total_views', days)
    if len(trend) < 7:
        return "数据不足"
    recent_7 = sum(v for _, v in trend[:7]) / 7
    prev_7 = sum(v for _, v in trend[7:14]) / 7 if len(trend) >= 14 else recent_7
    growth = (recent_7 - prev_7) / prev_7 * 100 if prev_7 > 0 else 0
    if growth > 20:   return f"📈 强势增长 (+{growth:.1f}%)，保持当前策略"
    elif growth > 0:  return f"📈 稳步增长 (+{growth:.1f}%)，可尝试加大发布频率"
    elif growth > -10: return f"📉 小幅下降 ({growth:.1f}%)，建议调整选题方向"
    else:             return f"📉 明显下降 ({growth:.1f}%)，需要复盘近期内容策略"
```

---

## 六、爆款复盘模板

```markdown
## 爆款复盘卡片

**内容**: [标题] | **平台**: [平台]
**数据**: 曝光 XX | 点赞 XX | 评论 XX | 收藏 XX | 分享 XX
**互动率**: XX% (日均 XX%)  **爆款倍数**: X.X倍

### 成功因子
1. **标题**: [分析标题吸引力]
2. **选题**: [话题热度/痛点精准度]
3. **发布时间**: [是否在黄金时段]
4. **内容格式**: [图文/视频/轮播]
5. **互动引导**: [CTA设计]

### 可复用经验
- 标题公式: [提取的标题模板]
- 内容结构: [可复用的结构]
- 发布策略: [时间/平台建议]

### 下次优化点
- [还能改进的地方]
```

---

## 七、快速启动清单

| 步骤 | 预计时间 |
|------|----------|
| 部署数据采集（MediaCrawler 或平台 API） | 30 分钟 |
| 创建 SQLite 数据库，配置数据入库 | 20 分钟 |
| 编写日报/周报生成脚本 | 30 分钟 |
| 部署 Grafana 可视化看板（可选） | 30 分钟 |
| 配置 Cron 每日自动生成报告 | 10 分钟 |
| 首次爆款复盘 | 20 分钟 |

---

> **提示词模板**：  
> "请基于以下数据生成本周社媒周报：[粘贴数据]。分析各平台表现、识别爆款内容并进行因子拆解，给出下周内容优化建议。同时对比上周数据给出趋势判断。"
