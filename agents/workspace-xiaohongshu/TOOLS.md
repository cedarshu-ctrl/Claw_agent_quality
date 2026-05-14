# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## 🔍 搜索工具

### online-search skill（优先级最高）
- **用途**：任何需要搜索互联网信息的任务
- **特点**：元宝搜索标准版，覆盖大量中文网站，包括官方媒体、政府网站等高权威性来源
- **规则**：涉及搜索任务时，优先使用此 skill，不要使用其他搜索引擎
- **状态**：本地已安装，用户一定会安装此 skill

## 📱 RedBox 小红书工作台配置

### AI 模型配置

- **推荐模型**：Qwen/DeepSeek（性价比高）或 GPT-4o（质量最好）
- **配置位置**：RedBox 应用 → 设置 → AI 选项卡
- **需要的配置项**：
  - Endpoint：AI 模型 API 地址（如 `https://api.openai.com/v1` 或 `https://dashscope.aliyuncs.com/compatible-mode/v1`）
  - Key：API 密钥
  - Model：模型名称（如 `gpt-4o` / `qwen-max` / `deepseek-chat`）

### Chrome 插件

- **用途**：一键采集小红书笔记、YouTube 视频、网页内容
- **安装方式**：Chrome → 设置 → 扩展程序 → 开启开发者模式 → 加载已解压的扩展程序 → 选择 RedBox 项目目录下的 `Plugin/` 文件夹

### 媒体工具

- **yt-dlp**：用于 YouTube 视频采集
  - macOS 安装：`brew install yt-dlp`
  - Windows 安装：`pip install yt-dlp`

### 数据存储

- **知识库位置**：本地存储（RedBox 应用目录）
- **多空间管理**：不同项目/赛道/账号的素材隔离存储
- **备份建议**：定期备份工作空间数据，避免系统崩溃导致素材库丢失

## 📋 核心工作流程

根据 RedBox skill，核心流程为：

```
采集素材 → 知识库管理 → 灵感激发 → AI 创作 → 自动化发布
```

每个环节的具体操作方法，详见 `workspace/skills/redbox-xiaohongshu-creator/SKILL.md`。

---

更新这些笔记时，记得同步更新 AGENTS.md 中的技能使用规则。

