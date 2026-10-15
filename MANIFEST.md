# 更新索引契约 v1

入口：`https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json`

此契约为后续 App 在线更新准备，当前 App 尚未接入。索引格式与规则格式分别版本化，不能混用。

| 字段 | 含义 |
| --- | --- |
| schemaVersion | 索引结构版本，目前为 1；未知版本拒绝处理 |
| release | 固定发布标签，例如 rules-v17；禁止移动、覆盖标签 |
| publishedAt | 本次全局规则发布时间，Unix 秒 |
| global | 完整全局规则的下载元信息 |
| sites | 站点补充规则元信息数组，按 id 排序 |

每个文件条目包含 `id`、`schemaVersion`（规则格式）、`code`、`publishedAt`、`compatibility`、`path`、`url`、`size`、`sha256`。
站点条目另含 `architecture`、`domains`、`base`。`size` 单位是字节，摘要针对下载文件的完整 UTF-8 字节（包含末尾换行），使用小写 SHA-256 十六进制。

`path` 为仓库相对路径，`url` 固定到 `release` 标签，不能用 main 的实时文件代替。`global.json` 是完整包，包含所有站点补充，不是只包含通用规则。

后续客户端应先验证索引版本与字段，再比较相同 ID 的 code；下载后校验大小和 SHA-256，再用生产规则引擎检查 schemaVersion、compatibility、base、完整规则语义及同版本冲突。只在全部通过后原子替换。失败保留当前有效规则。

时间戳只显示，不决定新旧。站点规则独立存储，不写回全局。下载地址仅允许受信 HTTPS 仓库及规定路径；不从索引接受任意重定向或脚本。SHA-256 仅校验完整性，本版本未提供发布签名。

## 发布一致性

1. 修改 global.json，按变化递增全局、架构和站点 code；更新时间戳。
2. 在 Pocket Evo 项目用生产引擎验证和回归，再运行生成器、单测及 --check。
3. 提交全部文件，以全局 code 创建 rules-vN 标签。
4. 使用 `git push --atomic origin main rules-vN` 同时发布分支和标签。
5. 验证远端索引、标签与全局规则摘要。禁止复用已发布 code 修改内容。

README 与索引由脚本生成；修改 README 模板请编辑 scripts/generate.py 后重新生成。
