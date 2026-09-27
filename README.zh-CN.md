# Reflection Companion

**简体中文** | [English](README.md)

从已有的 AI 对话里，看见自己的变化、检查判断、发现新的自我探索方式，并让有用的理解在以后继续发挥作用。

**0.3.0 · 公开 Alpha · 一个 Codex 插件、一项 Skill · MIT**

## 五种可以直接使用的方式

| 你想做什么 | 可以直接这样说 |
| --- | --- |
| 看见变化 | “回顾最近的对话，我判断这个问题的标准有什么变化？” |
| 检查判断 | “我可能漏掉了什么？也考虑支持我当前想法的解释。” |
| 拓展视角 | “围绕这个问题，带我认识一个惯常思路之外的有用视角。” |
| 找自我探索的灵感 | “推荐几个不同的自我探索方式，今天轻松一点。” |
| 留下重要理解 | “把这个结论保存；之前那条理解不准确，以后用这个修正。” |

可以从一个问题、当前处境或可访问的历史对话开始。无需额外写日记、先设置保存或记住固定命令。日回顾、周回顾、主题讨论和睡前交谈都是可选节奏。

## 一段交谈会是什么样

*虚构教学示例，不是真实用户经历或测试结果。*

> **你：** 已经有三份报价，我还在继续要。我是不是用准备来推迟决定？
>
> **Companion：** 数量本身不能说明。如果遗漏重要成本，继续了解有意义；如果只重复回答同一个问题，价值可能很小。哪个未回答的问题会改变选择？
>
> **你：** 是否包含维护。
>
> **Companion：** 那就直接确认维护范围。目前证据支持补上具体信息，不能据此给你贴“拖延”的标签。

有用的理解应当允许修正；方向合理时也可以得到肯定。阅读[四个完整场景](docs/EXAMPLES.zh-CN.md)，或浏览[探索玩法库](https://github.com/zhenglimindesign-ing/reflection-companion/blob/main/docs/PROMPTS.zh-CN.md)。

## 开始使用

在 Codex 中说：

> 请从 https://github.com/zhenglimindesign-ing/reflection-companion 的 v0.3.0 版本安装 Reflection Companion。核对版本，避免同时启用旧版。暂不开启保存和定时。

使用 Codex CLI 时：

```sh
codex plugin marketplace add zhenglimindesign-ing/reflection-companion --ref v0.3.0
codex plugin add reflection-companion@reflection-companion
```

打开新 chat，按界面要求选择插件。说：**“用 Reflection Companion 推荐一个值得了解自己的问题。”** 也可以直接提出具体请求。

[完整指南](docs/USER_GUIDE.zh-CN.md)包含 ZIP 安装、升级、保存、纠正、定时和排错。也可以下载[固定版本安装包](https://github.com/zhenglimindesign-ing/reflection-companion/releases/tag/v0.3.0)。

## 探索可以持续带来新内容

内置 18 个原创双语玩法，覆盖变化、判断、价值、优势、可能性和轻松表达。它可以从库中推荐、结合当前上下文调整，或在你要求时搜索近期公开玩法。选中后在当前对话继续；也可以让它代选。“不符合我”“轻一点”“聊过了”“换个方向”都会影响后续回答。

近期分享和有证据的热门会分开标明。个人回答不会进入公共库。公共库更新随版本发布，见[维护与贡献说明](docs/MAINTAINING.zh-CN.md)。

## 使用条件

- 已验证的安装目标是 macOS 上的 Codex CLI/桌面环境；其他宿主与系统未获本版认证。只有可选本地保存程序需要 Python 3.10+。
- 历史回顾依赖宿主实际能读取的材料；安装不会解锁完整账号历史或其他平台内容。没有历史时，可以基于当前对话开展范围更窄的探索。
- 保存可选，位置由你选择。记录为本地明文，相关内容仍会按宿主政策由模型处理。本产品没有开发者服务器或自动回传。
- 定时另行开启并受宿主环境影响。设置成功与实际首次送达分别核验，不承诺设备关闭后的持续送达。
- 解释与决定属于你；你可以拒绝、纠正或删除保存的观察。

## 反馈与更新

作者已实际使用此前候选版，并接受公开试用。本次 Alpha 加入新的探索推荐流程；技术检查和虚构示例不能证明它对每位用户都有用。后续通过持续使用和自愿反馈改进。

[报告问题或建议](https://github.com/zhenglimindesign-ing/reflection-companion/issues/new/choose)时，提供版本、尝试的用法、预期与实际结果即可。公开 Issue 会对外可见，可以用虚构的小例子复现，无需提交私人聊天。另见[更新记录](CHANGELOG.zh-CN.md)、[贡献说明](docs/MAINTAINING.zh-CN.md)和[许可证](LICENSE)。
