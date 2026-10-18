# 规则文件字段与站点单独配置

本文对应当前 Pocket Evo 规则格式 `schemaVersion: 1`、引擎 `engine: 1`。全量文件为 `global.json`，当前已实现 `nexusphp` 与 `unit3d`；`gazelle` 保留扩展设计，尚未开放。独立架构站点（包括 BeyondHD）不使用此规则文件。

## 1. 全量文件

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| schemaVersion | 整数 | 必填，当前必须为 1；规则文件结构版本 |
| type | 字符串 | 必填，固定 global |
| id | 字符串 | 必填，固定 pocket-evo.web-rules |
| code | 整数 | 必填，整个文件的内容版本，范围 1–2147483647 |
| publishedAt | 整数 | 必填，Unix 秒时间戳，范围 0–253402300799；仅用于显示 |
| compatibility | 对象 | 必填，引擎兼容性，见下表 |
| architectures | 对象 | 必填，按架构 ID 分组的通用规则；当前支持 nexusphp、unit3d |
| sites | 数组 | 必填，站点补充规则，可为空；每个元素是第 3 节的完整站点文件结构 |

不允许增加 name、description、备注等未定义字段；JSON 不支持注释。不要把 Cookie、Passkey、API Key、账号或个人信息写入规则。

### compatibility

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| engine | 整数 | 必填，当前为 1，执行语义版本 |
| features | 字符串数组 | 必填，使用的额外能力；不需要时填写 [] |

当前支持的能力标识：

| 标识 | 用途 |
| --- | --- |
| semantic-table.v1 | 按表头、排序链接或单元格识别表格列 |
| label-value.v1 | 标签与值配对读取 |
| promotion-time.v1 | 优惠剩余时长 |
| resource-age.v1 | 资源存活时间 |
| following-content.v1 | 读取元素后同一行的内容 |
| leading-text.v1 | 读取首个换行前的内容 |
| promotion-end.v1 | 优惠结束时间 promotionEndsAt |
| tag-filter.v1 | 请求绑定 ID 和标签筛选映射 |
| tag-parameter.v1 | 不同标签使用不同参数名 |
| tag-key-suffix.v1 | 标签 ID 拼在参数名后面 |
| tag-search-token.v1 | 标签作为搜索词标记 |
| profile-page.v1 | 额外个人资料页 |
| map-merge.v1 | 对象浅合并补丁 |
| native-filter-controls.v1 | 从规则指定的原生控件识别标签请求参数与真实 ID |
| attribute-pagination.v1 | 从分页按钮属性读取页码，不执行 JavaScript |
| array-tag-parameter.v1 | 标签参数映射支持 resolutionIds[] 等数组键 |
| resource-link-identity.v1 | 资源详情和下载链接必须匹配当前资源 ID |
| hr-days.v1 | H&R 天数标签，例如 H&R 3DAY |

能力标识不代表可执行任意代码。站点新增能力应在自身 compatibility 中声明；编译时与通用规则能力合并。未知能力会被拒绝。v22 包含 `hr-days.v1`，旧版 App 如提示不支持规则能力，需要先更新 App；更新失败会保留原规则。

## 2. 通用架构规则

每个 `architectures.nexusphp` / `architectures.unit3d` 对象包含且只包含：

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| code | 整数 | 此架构通用规则的版本，独立于全局 code |
| publishedAt | 整数 | 此架构规则发布时间，Unix 秒 |
| compatibility | 对象 | engine 与 features，格式同上 |
| pages | 对象 | 页面请求与解析定义，详见第 5 节 |

全局 code 用于整包更新，架构 code 用于判断站点补充依赖，站点 code 用于同一站点的新旧选择，不能互相替代。

## 3. 单独站点文件

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| schemaVersion | 整数 | 必填，当前 1 |
| type | 字符串 | 必填，固定 site |
| id | 字符串 | 必填，稳定站点 ID；1–128 字符，首字符为小写字母或数字，后续允许小写字母、数字、下划线、点、连字符 |
| code | 整数 | 必填，该站点内容版本；同 ID 比较，范围同全局 |
| publishedAt | 整数 | 必填，该站点规则发布时间，Unix 秒 |
| architecture | 字符串 | 必填，nexusphp 或 unit3d |
| domains | 字符串数组 | 必填，1–32 个域名；不写协议、路径、端口或通配符；精确匹配，www 不自动等同根域名 |
| compatibility | 对象 | 必填，engine 与 features |
| base | 对象 | 必填，对应通用架构规则的版本要求 |
| base.minCode | 整数 | 必填，可兼容的最低架构 code，至少 1 |
| base.maxCode | 整数 | 可选；省略表示不限制最高架构 code。填写时不得小于 minCode，且不超过 2147483647；不能填 null |
| patches | 数组 | 必填，完整补丁集合，可为空，最多 256 项 |

**minCode 必填，maxCode 可省略。** 它们比较的是架构 code，不是全局 code 或 App 版本。省略上限仍会校验结构、引擎能力和补丁编译，不代表任意未来结构都兼容；如已知不兼容边界，可显式填写上限。此格式需使用已支持可选上限的新版 App，旧版可能拒绝导入。

domains 会规范化小写及国际化域名、去重；不同站点 ID 不能声明冲突域名。域名列表不授权跨域发送凭据。

### 补丁字段与操作

| 字段 | 含义 |
| --- | --- |
| op | replace、remove、prepend、merge、add 之一 |
| path | 从 /pages/ 开始的路径，最多 2048 字符；列表通过元素 id 定位，不使用数字下标 |
| value | 除 remove 外必填，类型按目标位置决定；remove 不允许带 value |

| op | 行为与限制 |
| --- | --- |
| replace | 整体替换已存在目标；数组和对象也整体替换 |
| remove | 删除已存在目标；不能删除编译后仍必需的内容 |
| prepend | 向已存在数组头部插入 value 数组；优先候选可用此操作 |
| merge | 对已存在对象做浅合并，同名键覆盖；不是递归合并；需要 map-merge.v1 |
| add | 当前只允许新增不存在的 /pages/profile；需要 profile-page.v1 |

例如 `/pages/list/request/query/resource-tag/map` 使用查询绑定的 id `resource-tag`，而不是 query/6/map。路径中键名的 `/` 写成 `~1`，`~` 写成 `~0`。
补丁按顺序应用，最后对整个结果重新编译校验；不是通用 JSON Patch，不支持任意路径或脚本。

## 4. 单独配置一个站点

1. 在 global.json 的 sites 中找到该站，将**整个站点对象**复制为一个独立 `.json` 文件。若没有该站，可按下面模板新建。
2. 已存在的站点保留 id；新站使用独立 ID。domains 必须包含当前使用的域名。域名已属于其他 ID 时不能冒用新 ID 绕过冲突。
3. 修改 patches，保留该站其他仍需要的补丁；新版是完整补充集合，不会与旧补充逐条叠加。
4. 递增该站 code、更新 publishedAt，填写经过验证的通用架构 code 范围。同 ID 同 code 不允许改内容。
5. 在 App「站点适配诊断 → 导入站点规则」导入，执行诊断并确认真实列表与筛选。全局文件则从「设置 → 站点规则」导入。

### 完整示例：覆盖真实标签 ID

以下为虚构的 example.org 示例，可在当前 NP 架构 version 17 下编译；域名、标签 ID 必须替换为目标站的真实数据。

```json
{
  "schemaVersion": 1,
  "type": "site",
  "id": "example",
  "code": 1,
  "publishedAt": 1792028576,
  "architecture": "nexusphp",
  "domains": ["example.org", "www.example.org"],
  "compatibility": {
    "engine": 1,
    "features": ["tag-filter.v1"]
  },
  "base": {"minCode": 17},
  "patches": [
    {
      "op": "replace",
      "path": "/pages/list/request/query/resource-tag/map",
      "value": {"dolby": 9, "chinese-subtitles": 6}
    }
  ]
}
```

replace 只保留列出的映射，避免误继承该站并不存在的通用 ID。若只是补充且确认其他默认映射仍正确，可改用 merge，并在 features 加入 map-merge.v1。不支持远端标签筛选时可以 replace 为 `{}`；卡片标签解析不受此映射控制。

App 也会从真实页面的筛选链接/表单发现并修正映射；不要用标签文字、显示顺序或其他站的 ID 猜测本站 ID。标签筛选单选且走站点请求，不做本地标签过滤。

### 更换读取方式

保留已有解析器/字段/候选 id，用 replace 修改它们的 read 或 candidates；增加优先读取方式可 prepend 到候选数组。
例如当前通用规则的账户解析器 id 为 panel，资源解析器 id 应直接查看 global.json。选择器应限定当前资源或用户信息区域，避免匹配页面导航、其他用户或大小列的 GB。

### 生效顺序

当前通用架构规则，加上至多一份匹配、兼容的站点补充。全局内补充与单独导入补充按同一 id 的 code 选择最高兼容版本，不叠加。导入站点文件不修改全局文件。
先选版本再判断该版本是否含当前域名；不能因新版删除域名而回退旧版补回。没有可用补充时走通用规则。删除单独导入文件后，重新依据全局规则选择。

## 5. pages：请求、状态、解析与分页

pages 必须有 account 和 list；可增加 profile。

| 页面 | 用途 |
| --- | --- |
| account | 账户数据 |
| list | 资源列表 |
| profile | 额外账户资料页，目标来自 accountUrl，需 profile-page.v1 |

每个页面允许以下字段：

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| request | 对象 | 必填，页面请求定义 |
| states | 对象 | 可选，页面状态检测 |
| parsers | 数组 | 必填，1–6 个解析器 |
| pagination | 数组 | 可选，列表分页提取方式 |

### request

| 字段 | 含义 |
| --- | --- |
| target | account/list 通常为 {"from":"entry"}，使用已配置入口；account 也可为不含查询参数的安全站内路径；profile 为 {"from":"accountUrl"} |
| query | 可选，请求参数绑定数组 |

query 每项允许：

| 字段 | 含义 |
| --- | --- |
| id | 可选，稳定绑定 ID，用于补丁定位；同一 query 中唯一，使用时声明 tag-filter.v1 |
| param | 必填，参数名；不允许 Cookie、Token、Passkey、authkey、password 等凭据参数 |
| input | 与 literal 二选一：query、page、pageSize、category、sort、direction、tag、promotion |
| literal | 固定字符串、数值或布尔值；不能同时使用 map、encoding、offset |
| map | 可选，输入语义到本站值的映射；最多 128 项；未匹配的输入不发送 |
| encoding | 可选，见下表；默认 scalar |
| offset | 可选，仅用于 page，取 -1、0、1；应用页码从 1 开始，NP 通常 -1 |

input：query 为搜索词，pageSize 为加载数量，sort 为 publishedAt/sizeBytes/seeders/leechers/completed，direction 为 asc/desc。category 当前保留入口的固定分类，不根据此绑定另加分类；promotion 在入口已有固定优惠参数时不覆盖。tag 只允许一条绑定，值必须来自真实站点映射。

| encoding | 含义 |
| --- | --- |
| scalar | 普通参数，如 tag_id=9 |
| repeat | 兼容的同名参数编码；当前单标签请求只发一个值，不代表支持多选 |
| brackets | 参数名加 []，如 tags[]=9 |
| keySuffix | 参数名加 ID、值为 1，如 tag9=1；需 tag-key-suffix.v1 |
| searchToken | 将 +标记 合并到搜索词；同 param 必须有 query 绑定，需 tag-search-token.v1 |
| parameter | map 值形如 HDR=1，不同标签映射到不同参数；需 tag-parameter.v1 |

标签映射 key 为 App 语义标识，不是显示文字：
`hot`、`pinned`、`official-release`、`original`、`premiere`、`mandarin`、`chinese-subtitles`、`bilingual-subtitles`、`cantonese`、`diy`、`dolby`、`hdr`、`4k`、`8k`、`hit-and-run`、`no-repost`、`ongoing`、`completed`、`episodic`、`disc`、`chinese-localized`、`short-drama`、`lossless`、`resident`、`pure-version`。
优惠使用 promotion 独立绑定；当前 NP 通用值为 normal、free、double-upload、double-free、half-download、double-half、thirty-percent，实际参数值按站点确认。

### states

允许 authRequired（登录）、challengeRequired（验证）、permissionDenied（权限）、unavailable（不可用）、empty（空结果）。每个状态为 1–8 个条件，条件字段为 css（必填选择器）、text（可选正则）。状态判断受现有解析器优先级控制，不应使用过宽的文字条件掩盖登录失败。

### parsers / layout

| 字段 | 含义 |
| --- | --- |
| id | 必填，同页面唯一的解析器 ID |
| scope | account/profile 必填，账户信息块的 CSS 选择器 |
| layout | list 必填，列表布局 |
| fields | 必填，字段名到读取定义的对象；list 必须有 resourceId、title |

layout.kind 可为 elements 或 table：

| 字段 | 含义 |
| --- | --- |
| kind | elements 为元素列表，table 为语义表格 |
| items | elements 必填，每项资源选择器 |
| root | table 必填，表格选择器 |
| rows | table 必填，行选择器 |
| columns | table 的语义列定义对象，key 自定并由 read.column 引用 |

每个 columns 项支持 headers（表头文字数组）、sortValues（排序值数组）、headerCss（表头图标等选择器）、cellCss（行内单元格选择器）。优先用唯一 cellCss，否则用唯一表头匹配位置；不使用固定数字列下标。表头排序链接支持 sort/order/order_by/sortField 参数。

### fields、candidates 与 read

字段定义只允许 candidates（必填，1–8 项）、strategy（可选，只有 tags 可用 collect）。默认依次选择首个有效候选；collect 汇总候选并去重。
每个候选含 id（必填，同字段唯一）、read（必填）、then（可选，最多 8 个转换）。

| read 字段 | 含义 |
| --- | --- |
| css | CSS 选择器；与 column、label 三选一 |
| column | layout.columns 中的语义列名 |
| label | 标签文本数组，1–32 项，用于标签值读取，必须同时有 within |
| within | 标签查找区域 CSS 选择器 |
| mode | css 读取方式，见下表 |
| attribute | attribute/attributes 模式必填，如 href、src、title |
| scope | 通常省略表示当前资源/账户块；page 仅允许账户字段使用；禁止 group |
| exclude | 可选，读取文本时剔除的子元素选择器数组 |

| mode | 输出 |
| --- | --- |
| text | 单个文本；匹配不同值时视为歧义，不随意取第一项 |
| texts | 文本数组 |
| attribute | 单个属性值 |
| attributes | 属性值数组 |
| exists | 是否存在，布尔值 |
| followingText | 元素后紧邻的连续文本节点 |
| followingContent | 同父元素内、下一个 br 前的后续内容，可排除装饰元素 |
| leadingText | 元素内首个 br 前的内容，需 leading-text.v1 |

### then：转换

转换按数组顺序执行；值缺失则停止当前候选。不支持 JavaScript、网络请求或任意表达式。

| 字符串操作 | 含义 |
| --- | --- |
| trim | 去除两端空白 |
| htmlText | HTML 片段转文本 |
| durationSeconds | 时长转整数秒 |
| integer | 转整数 |
| decimal | 转小数 |
| bytes | 带单位容量转字节整数 |
| ratio | 分享率转数值 |
| url | 相对地址解析为 URL |
| stringList | 转字符串列表 |
| identifier | 规范化标识文本 |

| 对象操作 | 字段与含义 |
| --- | --- |
| queryParam | {"queryParam":"id"}，取 URL 参数 |
| regex | {"regex":"表达式","group":1}，第一个匹配的分组，group 为 0–8 |
| lookup | {"lookup":{"原值":"新值"},"unknown":"missing"}，unknown 可为 missing 或 preserve |
| tagAliases | {"tagAliases":{"中字":"chinese-subtitles"}}，逐项映射标签，未命中保留 |
| date | {"date":{"formats":["yyyy-MM-dd HH:mm:ss"],"zone":"site"}}，站点时间；formats 为 1–8 项 |

date 不是任意时间格式执行器；当前实现只对支持的紧凑日期形式做规范化，其余文本继续交给现有日期处理，不会猜测站点时区。regex 最长 256 字符，禁止反向引用和风险嵌套重复；lookup/tagAliases 最多 128 项。

### 输出字段全集

账户和 profile 共用以下字段：

| 字段 | 输出类型与含义 |
| --- | --- |
| accountId | 字符串或整数，账户 ID |
| accountUrl | URL，个人资料页地址 |
| username | 文本，用户名 |
| level | 文本，等级 |
| uploadedBytes / downloadedBytes | 整数，上传/下载字节数 |
| ratio | 数值，分享率 |
| seeding / leeching | 整数，当前做种/下载数量 |
| bonus | 数值，积分 |

资源字段：

| 字段 | 输出类型与含义 |
| --- | --- |
| resourceId | 字符串或整数，资源 ID，必需 |
| title / subtitle | 文本，主标题/副标题；title 必需 |
| detailUrl / downloadUrl / cover | URL，详情/下载/封面 |
| sizeBytes | 整数，文件字节数 |
| seeders / leechers / completed | 整数，做种/下载/完成数量 |
| publishedAt | 文本，资源发布时间；与包元信息的整数时间戳不同 |
| publishedAge | 文本，页面提供的资源存活时长 |
| author / category | 文本，发布者/分类 |
| tags | 列表，卡片标签 |
| uploadFactor / downloadFactor | 数值，上传/下载倍率，例如 2 和 0 表示 2X FREE |
| promotionRemainingSeconds | 整数，优惠剩余秒数 |
| promotionEndsAt | 文本，优惠截止时间；需 promotion-end.v1 |
| pinned / hot / hitAndRun | 布尔值，置顶/热门/H&R |
| format / encoding / medium | 文本，格式/编码/介质 |

输出必须匹配类型，例如大小列先 bytes、做种数先 integer、链接先 url。可选字段没提供就缺失，不伪造零值或默认用户名。

### pagination

每项只有 kind（numberedLinks 或 nextLink）、selector（分页链接 CSS）、parameter（页码参数名，通常 page）。用真实链接判定下一页，不能只看资源数推断；解析器也会检查重复页及资源签名。

## 6. 限额与验证

全局文件最多 5 MiB，站点文件最多 1 MiB，JSON 深度最多 64；最多 32 种架构、2000 份站点规则、每站 32 个域名、256 个补丁、16 个能力标识。当前可用架构仍只有 nexusphp。CSS 最长 2048 字符，正则最长 256 字符；工作线程处理有超时限制。

编写后先用 App 导入检查结构与补丁编译，再运行适配诊断，核对账户、资源列表、标签和分页。真实适配还应验证多页、空结果和站点搜索，不能以文件能导入等同适配成功。

## 7. 更新索引 manifest.json

索引只有 6 个字段，与规则格式独立：schemaVersion（当前 2）、code（全局版本）、publishedAt（Unix 秒）、url（固定发布标签下的全量文件地址）、size（字节数）、sha256（完整文件字节的 SHA-256 小写摘要）。

发布规则时手动同步 code、时间、大小和摘要，修改全局/架构/站点内容时分别递增对应版本。以全局 code 创建 rules-vN 标签，分支与新标签同时推送；已发布标签禁止移动或覆盖。仅修改文档而规则字节不变时无需升级规则版本。

下载后先核对大小、摘要及文件内版本，再用生产引擎检查格式和兼容性，全部通过才替换。SHA-256 用于完整性校验，不是签名。当前 App 在线更新仍待接入。


## UNIT3D 通用规则与原生控件

UNIT3D 与 NP 使用同一规则库、版本选择、导入、在线更新和诊断链路。普通 HTTP 与增强浏览器得到的 HTML 使用同一份不可变规则快照。`architectures.unit3d` 包含账号、个人资料、资源清单、原生请求参数和分页规则；`sites` 内的 AsianCinema / Blutopia 补充只保存实测标签 ID 映射。清单视图固定 `view=list`，卡片/分组入口在保存和请求时统一转换。

新增声明式能力（旧 App 不识别时拒绝整包并保留原有效规则）：

- `pages.list.tagDiscovery`（最多32项，需 `native-filter-controls.v1`）：每项有唯一 `id`、容器 `selector`、容器内 `control`、请求键 `parameter`；`tag` 固定语义与 `labels` 文本→语义映射二选一；固定数字 `value` 与 `valueAttribute`（仅 value/data-value）二选一。标签文字按空白归一、去首尾空白和小写匹配。没有控件、非法值或同一标签多个冲突 ID 不产生筛选项。后续页面补充或修正已发现映射；只有显示文字不会生成筛选。
- `encoding=parameter` 的标签 map 可写 `"4k":"resolutionIds[]=1"`，数组键需 `array-tag-parameter.v1`。真实 ID 放站点补充或从控件读取，不写入通用规则。参数中禁止凭据名称。
- `pagination.kind=attributeNumber`（需 `attribute-pagination.v1`）：声明 `selector`、`attribute`、`pattern`（最多256字符）、`group`（0–8）。只读取属性中的下一页号码；忽略 disabled/aria-disabled。比如读取 `wire:click` 的 gotoPage 数字，再通过已声明的 GET page 参数分页，绝不执行页面脚本。
- `pages.list.recordIdentity`（需 `resource-link-identity.v1`）：`marker` 标记资源行；`detailUrl`、`downloadUrl` 可分别声明 `regex` 与 `group`，从同源链接路径提取 ID，必须与该行 resourceId 一致。详情身份不合法的行计入部分解析失败；下载身份不匹配则不返回下载地址。

多个普通 query 绑定可以引用同一个输入，例如 `promotion=double-free` 同时映射 `free[0]=100` 与 `doubleup=1`，无须在代码中写死优惠组合。资源显示标签使用字段 candidates/collect；4k、8k 也是有效规范标签标识。

运行时安全边界仍由 App 控制：同源、Cookie 隔离、超时、解析线程/执行预算、下载验证不由远程规则关闭。规则不能携带凭据或脚本，也不能将尚未实现的 Gazelle 架构声明为可用。
