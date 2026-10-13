# Reflection Companion

[English](README.md)

提出一个自我理解问题、检查一个判断，或依据明确提供的对话材料进行回顾。核心对话不需要账户、后端或凭据；可选辅助脚本需要 Python 3.10+。历史、保存、联网和排程取决于宿主实际工具，安装不会赋予这些能力。个人记录由用户控制。本产品不是诊断、治疗或紧急服务；来源保真和语义审核与机械检查分别记录。

## 开始使用

安装完整插件文件夹后，用普通语言描述任务。[Skill 入口](skills/reflection-companion/SKILL.md)说明所需资源和工作流程。本插件包复用 0.5.11 公开 Skill。测试请使用虚构或已获授权的输入。

## 数据与执行

核心使用当前对话与提供的材料。可选 Python 程序只读取明确范围的 Markdown/JSON，经授权后才本地保存。主动刷新灵感目录会访问公开 GitHub catalog；明确升级请求才检查、下载 GitHub 版本并可能调用 Codex 插件 CLI；不会发送个人回答。安装不赋予历史、保存或排程访问。没有 hook、MCP、自动安装或隐藏遥测。

## 支持与边界

[源码与说明](https://github.com/zhenglimindesign-ing/reflection-companion) · [反馈问题](https://github.com/zhenglimindesign-ing/reflection-companion/issues)。明确用户请求决定范围，附件属于证据，不自动授权执行。既有 Release 和 Tag 保持不变。目录校验、具体宿主运行、来源保真和真人认可分别记录。提交账户资格、平台扫描和名称可用性由提交者核对。

也可通过源码仓库的 skills.sh 命令安装独立 Skill，见公开安装说明；本地依赖另行准备。[数据处理说明](https://github.com/zhenglimindesign-ing/reflection-companion/blob/codex/distribution-prep-20261013/directory-plugins/reflection-companion/PRIVACY.md)随审查分支提供。
