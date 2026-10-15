# 更新索引契约 v2

入口：`https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json`

索引仅描述一个完整全局规则文件，保留 6 个字段：

| 字段 | 含义 |
| --- | --- |
| schemaVersion | 索引结构版本，目前为 2；不是规则文件的结构版本 |
| code | 全局规则版本，与 global.json 的 code 一致 |
| publishedAt | 规则发布时间，Unix 秒，仅用于显示 |
| url | 固定发布标签下 global.json 的 HTTPS 下载地址 |
| size | 文件字节数 |
| sha256 | 完整文件字节的 SHA-256，小写十六进制 |

索引自动生成，不再重复规则 ID、相对路径、兼容性信息或发布标签字段，也没有 global 嵌套和站点单独下载索引。
App 在线更新尚未接入；后续只需实现 v2。规则文件自身的 schemaVersion 不随索引格式变化。

## 客户端处理

1. 验证索引版本与字段，比较全局 code 判断更新；时间不参与版本比较。
2. 仅允许受信 HTTPS 仓库及规定路径，下载 url 对应的文件，不使用 main 下实时文件替代。
3. 校验字节数和 SHA-256（包含末尾换行），并核对文件内 code、publishedAt 与索引一致。
4. 用生产规则引擎验证文件身份、schemaVersion、compatibility、base、规则语义及同版本冲突。
5. 全部通过后原子替换，失败保留当前有效规则。

SHA-256 用于完整性校验，不代替发布签名。

## 维护与发布

`global.json` 是唯一规则维护源。运行 `python3 scripts/generate.py` 更新索引和 README，再运行 `--check` 与单测。
规则改变时递增相关 code、更新时间戳，在 App 生产引擎完成回归后提交，并创建 rules-vN 标签（N 为全局 code）。
使用 `git push --atomic origin main rules-vN` 同时发布分支与标签，禁止移动或覆盖已发布标签。
只修改文档或分发结构、规则字节不变时，沿用已有规则标签和 code，直接推送 main。

## App 适配列表

`app-sites.json` 记录当前 App 已适配站点的名称和架构，包括没有专属补充规则的 NP 站点及独立 API 站点，不参与规则下载或解析。新增、移除 App 适配时同步更新此清单；README 由生成器读取该清单生成，不从补充规则数量推断 App 支持范围。生成器检查全局规则中的站点均已列入清单。
