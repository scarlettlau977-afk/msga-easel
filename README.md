# MSGA 塞班 AI 智能体

MSGA 是基于 [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel) 的二次开发项目，面向企业员工提供统一的 AI 工作平台：把公司母内容转化为员工个人版本，适配不同平台，并逐步连接发布、互动识别、客户画像和跟进任务。

> 当前仓库仍处于持续开发阶段。真实平台发布、客户沟通和账号操作必须经过人工确认；未配置的第三方能力不会被伪装成已实现。

## 这是什么项目

MSGA 复用 Easel 已验证的 OpenClaw Agent、Skill、画像、内容归档和 Web 工作台基础，在此基础上增加企业业务闭环：

```text
公司母内容 → 员工个人版本 → 平台适配 → 人工审核
→ 发布任务 → 互动扫描 → 意向识别 → CRM → 跟进建议
```

当前已完成的换皮和基础改造包括：

- Web 工作台品牌改为“MSGA 塞班 AI 智能体”。
- 新增 MSGA 图标和蓝绿色企业视觉主题。
- 欢迎页改为企业内容与业务行动场景。
- 保留 Easel/OpenClaw 的 CLI、Skill、画像和内容库能力。
- 保留 OpenClaw 独立 profile 机制，避免覆盖用户已有配置。

## 与上游 Easel 的关系

上游项目：<https://github.com/ZJU-REAL/Easel>

上游项目作者与贡献者：ZJU-REAL / REAL Lab / OpenDCAI Lab 及 Easel 项目贡献者。MSGA 保留上游版权声明、`LICENSE` 和原始许可条件，并在本 README 中明确标注来源与修改范围。

本项目的修改主要位于：

- `web/frontend/`：MSGA 前端品牌、标题、欢迎页和视觉主题。
- `web/static/`：兼容静态入口与 MSGA 图标。
- `app/`、`skills/`、`docs/`：MSGA 业务模型、OpenClaw Skill 和企业工作流设计。

这不是 ZJU-REAL/Easel 的官方版本，也不代表上游团队对 MSGA 的背书。使用时请同时遵守本仓库 `LICENSE` 以及上游项目的 Apache License 2.0 条款。

## 快速开始

需要 Python 3.10+、Node.js、Git、FFmpeg 和 OpenClaw。Windows 用户可以在 PowerShell 中运行：

```powershell
git clone https://github.com/scarlettlau977-afk/msga-easel.git
cd msga-easel
.\setup.ps1
.\.venv\Scripts\easel.exe doctor
.\.venv\Scripts\easel.exe web
```

启动后访问 <http://localhost:7860>。如果你使用其他仓库名，请把上面 clone 地址替换为实际地址。

常用命令：

```powershell
.\.venv\Scripts\easel.exe doctor
.\.venv\Scripts\easel.exe ping
.\.venv\Scripts\easel.exe web
.\.venv\Scripts\easel.exe skill <skill-name> -i "你的需求"
```

模型密钥、平台 Cookie 和 Token 只允许写入本地 `.env` 或 OpenClaw profile，不得提交到 Git。真实平台登录、发布和客户消息必须人工确认。

## 开发状态

MSGA 按以下顺序推进：

1. 内容生成系统
2. 平台适配系统
3. 发布/执行任务状态机
4. Virtual Computer Agent 技术验证
5. Interaction Scanner
6. CRM / 客户画像
7. 跟进与提效自动化

每个模块都使用 Mock Provider 优先，并配套测试、错误处理和 README 更新；未验证的第三方 API 会明确标记为 TODO / NEEDS_VERIFICATION。

## 许可证与归属

本项目保留并遵守上游 [Apache License 2.0](LICENSE)。Apache 2.0 允许再发布和修改，但要求保留版权、许可证和 NOTICE（如有）信息，并明确标示修改内容。MSGA 的新增代码和文档按仓库中声明的许可证发布；第三方依赖和平台服务仍受其各自许可证与服务条款约束。

## 致谢

感谢 [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel) 提供 OpenClaw 社媒内容工作台基础，以及 OpenClaw 社区和所有上游贡献者。
