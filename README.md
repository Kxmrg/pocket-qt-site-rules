# Pocket Evo App 站点规则官方更新源

提供 Pocket Evo App 的完整全局站点规则，包含通用规则与站点补充规则。

| 规则版本 | 更新时间（北京时间） | 已测试站点 |
| --- | --- | --- |
| version 17 | 2026-10-15 09:42:56 | 67 个 |

**更新源：** https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json

## 已测试适配站点

以下 67 个站点已有适配和测试记录，涵盖 NexusPHP 和独立 API 站点。

根据目前的适配经验，其他未单独适配的 NP 站点预计约 90% 可直接使用通用规则；改动较大的站点仍可能需要单独适配。

**标签筛选会随列表加载自动补充：** App 先使用规则中的标签映射，再从列表页面的真实标签链接和筛选表单中识别标签 ID 及请求参数。后续翻页发现的新标签会继续加入；同一标签的 ID 发生变化时，以页面识别到的有效数据修正规则映射。因此，没有专属站点规则也有机会自动获得标签筛选。

卡片显示标签不等于站点支持标签筛选。如果页面只提供标签文字，没有可识别的服务端筛选参数，App 会保留卡片标签，但不会据此新增筛选项，也不会用本地过滤代替站点筛选。页面采用尚未支持的参数或结构时，仍需补充适配规则。

如果遇到无法适配的 NP 站点，请联系我反馈。

[官网](https://pocket.kxmrg.com/) · [Telegram 交流群](https://t.me/pocket_qt)

独立 API 站点适配随 App 更新，不由规则文件更新。

| 站点 | 架构 |
| --- | --- |
| HDTIME | NexusPHP |
| ZMPT | NexusPHP |
| 下水道 | NexusPHP |
| 蟹黄堡 | NexusPHP |
| 不可躺 | NexusPHP |
| HDDolby | NexusPHP |
| HDHome | NexusPHP |
| AGSV | NexusPHP |
| 海棠 | NexusPHP |
| 财神 | NexusPHP |
| PTT | NexusPHP |
| 憨憨 | NexusPHP |
| 观众 | NexusPHP |
| UBits | NexusPHP |
| 咖啡 | NexusPHP |
| 天枢 | NexusPHP |
| TTG | NexusPHP |
| 比特校园 | NexusPHP |
| 青蛙 | NexusPHP |
| HDFans | NexusPHP |
| 大青虫 | NexusPHP |
| 车站 CarPT | NexusPHP |
| 壹PT吧 | NexusPHP |
| PTHOME | NexusPHP |
| Farmm（农场） | NexusPHP |
| HDArea | NexusPHP |
| 聆音Club | NexusPHP |
| 好学 | NexusPHP |
| 猪猪 | NexusPHP |
| 北洋园 | NexusPHP |
| CHDBits | NexusPHP |
| 猫站 PTerClub | NexusPHP |
| HDSky | NexusPHP |
| KEEPFRDS | NexusPHP |
| OurBits | NexusPHP |
| Depth Studio | NexusPHP |
| alingPT | NexusPHP |
| 星湾 | NexusPHP |
| PTFans | NexusPHP |
| Moment | NexusPHP |
| 垃圾堆 | NexusPHP |
| PTGTK | NexusPHP |
| PTLGS | NexusPHP |
| CPT | NexusPHP |
| 拾刻 | NexusPHP |
| XLoli | NexusPHP |
| Kelu | NexusPHP |
| DiscFan | NexusPHP |
| March | NexusPHP |
| SSD | NexusPHP |
| OpenCD | NexusPHP |
| GGPT | NexusPHP |
| 音乐乌托邦 | NexusPHP |
| NovaHD | NexusPHP |
| TCCF / ET8 | NexusPHP |
| 南洋 PT | NexusPHP |
| TLFBits | NexusPHP |
| HDU | NexusPHP |
| U2 | NexusPHP |
| NicePT | NexusPHP |
| 烧包 | NexusPHP |
| 朱雀 | 独立架构站点 |
| M-Team（馒头） | 独立架构站点 |
| 海胆 | 独立架构站点 |
| SunnyPT（阳光） | 独立架构站点 |
| Rousi（肉丝） | 独立架构站点 |
| Yema（野马） | 独立架构站点 |

PTGTK 已完成 5 页采样，但部分服务器响应存在截断，缺失字段无法由规则恢复，尚不能视为全部字段验证通过。

## 文件说明

- `global.json`：全量规则，含通用规则和站点补充规则。
- `manifest.json`：更新索引。
- [rules.md](rules.md)：全字段说明及单独配置站点规则的方法。
- [MIT License](LICENSE)

规则、索引和适配列表手动维护，不使用生成脚本。
