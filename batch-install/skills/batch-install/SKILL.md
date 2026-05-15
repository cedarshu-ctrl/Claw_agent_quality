---
name: batch-install
description: 批量安装 57 个智能体到 openclaw。从 GitHub 仓库下载 ZIP 包，解压并注册到 openclaw 系统中。运行此 skill 即可完成全部安装。
color: green
tools: Bash, Read
---

# 批量安装 57 个智能体

你是一个安装执行器。按以下步骤操作，不要遗漏任何一个 Agent。

## 安装清单（57 个）

所有 Agent 的 workspace 名称如下，必须逐个安装：

```
agudingpan           A 股盯盘师
backend              后端架构师
ceshizhuanjia        测试专家
devops               DevOps 专家
douyinyunying        抖音运营专家
fapiaoguanli         发票管理专家
frontend             前端开发工程师
gaojishujufenxi      高级数据分析师
gaokaozhiyuan        高考志愿填报顾问
gongzhonghaozhubian  公众号主编
guanggaocelue        广告创意顾问
gupiaozhenduan       股票诊断师
hetongfawu           合同法务专家
hongguanfenxi        宏观经济分析师
jianshenguwen        私人健身顾问
jijinpeizhi          基金配置顾问
jingpinqingbao       竞品情报特工
jinrongfengkong      金融风控分析师
jishuwendang         技术文档专家
jixiaoguwen          绩效顾问
kuaishouyunying      快手运营专家
kuajingqingbao       跨境电商情报探长
kuajingyingxiao      跨境营销顾问
kucunguihua          库存规划师
liuxueguihua         留学规划顾问
lunwenjiedu          论文解读专家
lvxingguihua         旅行规划专家
meishituijian        美食推荐官
mubiaoguanli         目标管理教练
pm                   产品经理
quanmeiwenan         全媒体文案主编
rizhifenxi           日志分析工程师
roi                  ROI精算师
security             安全工程师
shejiaoshuju         社媒数据分析师
shenyejieya          深夜解压大师
shichangqushi        市场趋势研究员
shouqianfangan       售前方案顾问
sqlgongcheng         SQL代码工程师
tiktokyunying        TikTok 运营顾问
tishicisheji         提示词设计师
toufangyouhua        广告投放优化师
tuwenchuangyi        图文创意大师
weiboyunying         微博运营专家
wendangbidui         文档比对专家
wenjuansheji         问卷设计大师
xiangmujiaofu        项目交付顾问
xiaochengxuzhucheng  微信小程序主程
xiaohongshuguwen     小红书爆款顾问
xiaoshoujiaolian     销售教练
xinggefenxi          性格分析顾问
xuexiguihua          学习规划师
yonghufankui         用户反馈分析师
zhaopinguwen         招聘顾问
zhiduzhuanjia        制度撰写大师
ziliaodaren          资料整理达人
zimeitirelie         自媒体热点猎手
```

## 安装步骤

**第 1 步**：确定目标目录。

使用 `echo $HOME` 或 `echo %USERPROFILE%` 获取用户目录，然后：
- 目标 workspace 目录：`~/.openclaw/workspace-{name}/`
- 目标 agent 目录：`~/.openclaw/agents/{name}/agent/`

其中 `{name}` 为清单中的 workspace 名称（如 `backend`、`douyinyunying` 等）。

**第 2 步**：确保目标目录存在。

```bash
mkdir -p ~/.openclaw/
```

**第 3 步**：逐个安装。

对清单中的每个 workspace 名称，执行以下操作：

1. 下载 ZIP 文件：
   ```
   URL: https://github.com/cedarshu-ctrl/Claw_agent_quality/raw/master/Agent_zip/workspace-{name}.zip
   ```

2. 解压到目标 workspace 目录：
   ```bash
   mkdir -p ~/.openclaw/workspace-{name}
   # 解压 ZIP 内容到 ~/.openclaw/workspace-{name}/ 下（不要带 workspace 外层目录）
   unzip -o workspace-{name}.zip -d ~/.openclaw/workspace-{name}/
   ```

3. 确保 agent 目录存在：
   ```bash
   mkdir -p ~/.openclaw/agents/{name}/agent
   ```

4. 注册 agent：
   ```bash
   openclaw agents add {name} --workspace ~/.openclaw/workspace-{name} --non-interactive --agent-dir ~/.openclaw/agents/{name}/agent
   ```

**第 4 步**：安装完成后汇总。

输出安装结果摘要，包括成功数量和失败列表（如有）。

## 关键规则

- **不要跳过任何一个**，即使某个安装报错了也要继续尝试下一个
- 如果下载失败，重试一次，仍失败则记录并跳过
- 如果注册命令报错，记录错误信息，继续下一个
- 全部完成后输出统计：成功 X 个，失败 Y 个，列出失败项
- 安装过程中定期打印进度，如 `[15/57] 已完成 抖音运营专家`

## 快速验证

随机抽查 3 个已安装的 agent，运行 `openclaw agents list` 确认它们出现在列表中。
