# 选择入口与安装

**简体中文** | [English](PLATFORMS.md)

[回到概览](../README.zh-CN.md) · [手机体验](MOBILE.zh-CN.md) · [场景指南](USER_GUIDE.zh-CN.md)

当前公开候选 **v0.4.0-rc.1** 提供 Codex 插件和 Claude Code 项目 Skill。[下载对应平台包](https://github.com/zhenglimindesign-ing/reflection-companion/releases/tag/v0.4.0-rc.1)。Claude 网页版仍在验证，暂未提供公开下载。

## Claude Code 与 Claude 网页版区别

| | Claude Code | Claude 网页版 |
| --- | --- | --- |
| 适合谁 | 在电脑上使用项目、文件的用户；通常从终端进入。 | 想在网页聊天里使用 Skill 的用户。 |
| 怎么装 | 把 Skill 放在选定项目的 `.claude/skills/reflection-companion/`。 | 在 Customize → Skills 上传专用 ZIP，并启用所需代码执行能力。 |
| 怎么叫它 | `/reflection-companion`，或让 Claude 根据请求自动匹配。 | 开启 Skill 后自然描述需求，由宿主匹配；不假设同一个斜杠命令。 |
| 它能看什么 | 当前上下文及获准读取的项目/本地文件。 | 当前对话、主动上传的材料和实际提供的工具。 |
| 日记放哪里 | 获准的本地目录，可读回。 | 可生成可下载文件；不能据此声称已保存到你电脑或跨 chat 永久保留。 |
| 定时 | 取决于当前宿主提供的工具与运行条件。 | 同样需要检查账户工具，上传 Skill 不会创建任务。 |

区别涉及材料、权限与文件寿命，不只是叫它的方式。两种安装包从同一份核心 Skill 生成，不维护两套反思逻辑。说明依据 [Claude Code Skills](https://code.claude.com/docs/en/skills) 与 [Claude 自定义 Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

## Codex：当前公开版

在 Codex 中说：“从 https://github.com/zhenglimindesign-ing/reflection-companion 的 v0.4.0-rc.1 安装，核对版本，避免同时开启旧版；先不开启保存和定时。”安装后在新 chat 选择 Skill，直接提出一个场景请求。具体 CLI 和升级流程见[完整指南](USER_GUIDE.zh-CN.md)。v0.3.0 仍可选择，但不包含新的动态目录。

## Claude Code：已发布的候选包

下载 `reflection-companion-claude-code-0.4.0-rc.1.zip`，使用同一发布页的 `SHA256SUMS-claude-code.txt` 校验，在一个选定的个人项目中解压。应得到 `.claude/skills/reflection-companion/SKILL.md`；`.claude` 是隐藏目录。若该位置已有同名 Skill，先核对并保留旧版，不要直接覆盖。无需 clone 产品开发仓库。

从该项目启动 Claude Code，输入：

```text
/reflection-companion 陪我写今天的日记，一次问一个问题；仅用这段对话，先不保存。
```

没有出现 Skill 或仍显示旧描述时，先检查路径，再重新进入项目会话。核心对话不需要 Python；本地收获库及目录读取助手需要 Python 3.10+。保存和修改应返回真实记录位置与读回结果。历史权限不因安装而扩大。

## Claude 网页版：专用候选 ZIP

用 `reflection-companion-claude-web-0.4.0-rc.1.zip`，不要上传整个 Codex 分发包。ZIP 顶层是 `reflection-companion/`，里面有 `SKILL.md`、引用材料和脚本。在 Customize → Skills 按当前账户界面上传并启用；如果没有入口，检查官方要求与管理员设置，不凭空承诺可用。

新对话试：“用 Reflection Companion，帮我从今天的一件小事写日记，一次问一个问题；先不保存。”第一次可以只给一个虚构片段。网页实际上传、触发和下载仍待账户内实测；结构检查不能替代这一步。不能把浏览器内的临时路径当作本机存档位置。

## 兼容性边界

本候选的构建会核对 Claude 包内核心文件与源文件一致、入口格式、相对链接和 ZIP 完整性。Claude Code 的真实调用结果见随候选交付的验证记录。Claude 网页版与国内宿主没有实测前，不标为完整支持。手机文字入口可先体验，但其效果仍需用户在自己的应用验证。

个人记录放在自己选择的工作区；插件安装目录、公开仓库和开发仓库都不是必需的日记位置。安装不会给出整个账号聊天历史，也不会启用保存或定时。

## 实测范围（2026-09-29）

Claude Code 2.1.218 用虚构材料完成了：发现和调用 Skill、日记中区分事实与猜测、读取指定周记录并使用后续纠正、直接进入探索练习，以及通过包内脚本保存并读回记录。测试没有使用个人聊天或真实收获库。

一次包含初始化、保存、纠正和读回的组合请求在最终回复前超时；检查文件确认旧项已被替代，但不能把这次请求算作完整成功。随后较小的保存/读回请求完成。严格的命令权限导致多次重试，使用者仍需按宿主提示审查保存操作。尚未验证无人值守定时送达，也不保证每次模型执行都一致。

Claude 网页版的包格式已检查，上传和实际调用尚未完成，因此尚未发布。公开仓库 main 中的指南随验证更新；先前冻结的 Codex ZIP 内平台状态保留打包时的记录，以本页和发布说明为最新状态。
