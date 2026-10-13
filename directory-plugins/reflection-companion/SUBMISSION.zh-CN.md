# reflection-companion 提交准备

[English](SUBMISSION.md)

这是 `codex/distribution-prep-20261013` 上的 0.5.11-distribution.2 审查候选包。现有 Release 和 Tag 未改动，发布前需维护者审查。生成式公开分发项目在下一次 Release 前应同步回 canonical 源码；本次不改写历史发布清单哈希。

## OpenAI

完整 ZIP 包含通用、Codex、Claude manifest、方形图标、三个启动提示、依赖与隐私说明。产品范围由 `skills/*/agents/openai.yaml` 声明。

对话入口限定为 CHAT 与 CODEX。Codex 来源笔记预览及已登录 Claude 的反例任务通过。历史检索核心能力保留，仍需用户明确来源范围及宿主能力。ChatGPT/Work 原生执行、云端保存与排程为 NOT VERIFIED。

提交账号须完成开发者身份验证并具备写权限。操作路径为 https://platform.openai.com/plugins → 上传新插件 → skills-only ZIP，检查转换和自动扫描结果并修复阻断项。当前草稿与扫描结果另见任务交接，本地包校验不构成这些状态的证明。正式送审和具有约束力的声明需账号持有人授权。

## Claude

来源：`zhenglimindesign-ing/reflection-companion`；路径：`directory-plugins/reflection-companion`；分支：`codex/distribution-prep-20261013`。操作路径为 https://claude.ai/directory/manage → Submit new → Plugin bundle → Validate。GitHub 写权限已确认，最终任务交接记录平台校验及保存草稿是否实际成功。本地 Claude 安装／发现及已登录小任务通过；目录内原生运行仍为 NOT VERIFIED。

manifest 指向[分支隐私说明](https://github.com/zhenglimindesign-ing/reflection-companion/blob/codex/distribution-prep-20261013/directory-plugins/reflection-companion/PRIVACY.md)。政策咨询由另一路处理，本次不因政策推测删除核心功能，也不把校验通过当作政策批准。联系邮箱、年龄范围、具有约束力的合规确认与正式送审仍需账号持有人决定。本任务未获正式送审或公开发布授权。

## skills.sh

仓库发现、完整复制和新会话加载已在关闭遥测下通过；双语公开 README 已补充验证过的命令。默认分支安装仍使用当前公开源码，提议的文档和指令修复经维护者审查后才进入默认分支。关键词／搜索收录是独立事项且为 NOT VERIFIED；本次未添加排行榜功能或发送安装遥测。
