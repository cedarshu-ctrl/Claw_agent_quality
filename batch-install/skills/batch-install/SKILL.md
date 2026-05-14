---
name: batch-install
description: 批量安装 59 个智能体到 openclaw。从 GitHub 仓库下载 ZIP 包，解压并注册到 openclaw 系统中。运行此 skill 即可完成全部安装。
color: green
tools: Bash, Read
---

# 批量安装 59 个智能体

你是一个安装执行器。按以下步骤操作，不要遗漏任何一个 Agent。

## 安装清单（59 个）

所有 Agent 的 workspace 名称如下，必须逐个安装：

```
zimeitishujufenxi    自媒体数据分析专家
shichangzhuizong     市场追踪专家
liuxueguihua         留学规划顾问
backend              后端架构师
zimeitiredian        自媒体热点猎手
kuajingshemei        跨境社媒操盘手
frontend             前端开发者
geguzhenduang        个股诊断专家
douyin               抖音策略师
jingpindingsao       竞品盯梢探长
kucunyuce            库存预测专家
zhiduwenjian         制度文件撰写专家
ziliaozhengli        资料整理大师
gaokaozhiyuan        高考志愿填报顾问
guanggaochuangyi     广告创意策略师
lunbotu              轮播图增长引擎
mubiaochaijie        目标拆解教练
tengxunwenjuan       腾讯问卷设计专家
apitest              API 测试专家
zhaopin              招聘专家
tishici              提示词工程师
tiktok               TikTok策略师
gongzhonghao         公众号涨粉笔杆子
gaojixiangmu         高级项目经理
gaojishujufenxi      高级数据分析师
presales             售前工程师
xiaohongshu          小红书爆款操盘手
fapiaoguanli         发票管理专家
chihuocanmou         吃货参谋
xiaoshoujiaolian     销售教练
ppc                  PPC竞价策略师
mbti                 MBTI 配对师
roi                  ROI精算师
shenyepeiliao        深夜陪聊
xuexiguihua          学习规划师
qushiyanjiu          趋势研究员
hongguan             宏观经济专家
wenjiandubi          文件对比专家
hetongshenzha        合同审查专家
zimeitiwenang        自媒体文案生产专家
kuaishou             快手策略师
devops               DevOps自动化师
lanrenchuyou         懒人出游规划师
ailunwen             AI论文速读导师
jingpinqingbao       竞品情报特工
wps                  WPS表格美化整理师
jijinjuejin          基金掘金师
weibo                微博运营策略师
security             安全工程师
weixinxiaochengxu    微信小程序开发者
fankuifenxi          反馈分析师
sirenjianshen        私人健身教练
sql                  SQL代码助手
rizhiyichang         日志异常分析专家
pm                   产品经理
qqyouxiang           QQ邮箱管理专家
daima                代码文学家
jinrongfengkong      金融风控分析师
jixiaoguanli         绩效管理专家
```

## 安装步骤

**第 1 步**：确定目标目录。

使用 `echo $HOME` 或 `echo %USERPROFILE%` 获取用户目录，然后：
- 目标 workspace 目录：`~/.openclaw/workspace-{name}/`
- 目标 agent 目录：`~/.openclaw/agents/{name}/agent/`

其中 `{name}` 为清单中的 workspace 名称（如 `backend`、`douyin` 等）。

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
- 安装过程中定期打印进度，如 `[15/59] 已完成 抖音策略师`

## 快速验证

随机抽查 3 个已安装的 agent，运行 `openclaw agents list` 确认它们出现在列表中。
