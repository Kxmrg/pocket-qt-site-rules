# Pocket Evo App 站点规则官方更新源

提供 Pocket Evo App 的完整全局站点规则，包含通用规则与站点补充规则。

| 规则版本 | 更新时间（北京时间） | 已测试站点 |
| --- | --- | --- |
| version 20 | 2026-10-15 16:18:03 | 76 个 |

**更新源：** https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json

**官网：** https://kxmrg.com/

**浏览器插件：** https://github.com/Kxmrg/pocket-evo-extension

**Telegram：** https://t.me/pocket_qt

使用微信扫描下方二维码加入内测群。二维码有效期至 2026 年 10 月 20 日。

<img src="images/beta-group-qr.jpg" alt="Pocket Evo 内测群微信二维码" width="360" />

## 已测试完美适配站点

- **已测试站点**：下表 76 个站点均已测试并完美适配。
- **其他 NP 站点**：预计约 99% 可直接使用。未经单独适配的站点会在加载列表时自动获取标签 ID（tag_id），因此标签筛选项可能暂不完整，后续加载会继续补充。
- **适配进度**：GZ、U3D 架构正在适配中。
- **独立架构站点**：适配随 App 更新，不由规则文件更新。
- **特殊站点**：部分改动较大的 NP 站点可能无法直接适配，遇到问题请联系我。

站点按名称首字母排序，中文名称按拼音排序。

### NexusPHP 站点（69 个）

| 站点 | 架构 |
| --- | --- |
| AGSV | NexusPHP |
| alingPT | NexusPHP |
| 北洋园 | NexusPHP |
| 比特校园 | NexusPHP |
| 不可躺 | NexusPHP |
| 财神 | NexusPHP |
| CHDBits | NexusPHP |
| 车站 CarPT | NexusPHP |
| CPT | NexusPHP |
| 大青虫 | NexusPHP |
| 大香蕉 | NexusPHP |
| Depth Studio | NexusPHP |
| DiscFan | NexusPHP |
| Farmm（农场） | NexusPHP |
| GGPT | NexusPHP |
| 观众 | NexusPHP |
| 海棠 | NexusPHP |
| 憨憨 | NexusPHP |
| 好学 | NexusPHP |
| HDArea | NexusPHP |
| HDDolby | NexusPHP |
| HDFans | NexusPHP |
| HDHome | NexusPHP |
| HDSky | NexusPHP |
| HDTIME | NexusPHP |
| HDU | NexusPHP |
| 咖啡 | NexusPHP |
| KEEPFRDS | NexusPHP |
| Kelu | NexusPHP |
| 垃圾堆 | NexusPHP |
| 聆音Club | NexusPHP |
| LONGPT | NexusPHP |
| 猫站 PTerClub | NexusPHP |
| March | NexusPHP |
| Moment | NexusPHP |
| 南洋 PT | NexusPHP |
| NicePT | NexusPHP |
| NovaHD | NexusPHP |
| OpenCD | NexusPHP |
| OurBits | NexusPHP |
| PlayLet | NexusPHP |
| PTFans | NexusPHP |
| PTGTK | NexusPHP |
| PTHOME | NexusPHP |
| PTLGS | NexusPHP |
| PTT | NexusPHP |
| PTzone | NexusPHP |
| 青蛙 | NexusPHP |
| RailgunPT | NexusPHP |
| 烧包 | NexusPHP |
| 拾刻 | NexusPHP |
| SSD | NexusPHP |
| TCCF / ET8 | NexusPHP |
| 天枢 | NexusPHP |
| TLFBits | NexusPHP |
| TTG | NexusPHP |
| U2 | NexusPHP |
| UBits | NexusPHP |
| VC-Lib | NexusPHP |
| 下水道 | NexusPHP |
| 蟹黄堡 | NexusPHP |
| 星湾 | NexusPHP |
| 星陨阁 | NexusPHP |
| 修道院 | NexusPHP |
| XLoli | NexusPHP |
| 音乐乌托邦 | NexusPHP |
| 壹PT吧 | NexusPHP |
| 猪猪 | NexusPHP |
| ZMPT | NexusPHP |

### 独立架构站点（7 个）

| 站点 | 架构 |
| --- | --- |
| 海胆 | 独立架构站点 |
| 可乐 | 独立架构站点 |
| M-Team（馒头） | 独立架构站点 |
| Rousi（肉丝） | 独立架构站点 |
| SunnyPT（阳光） | 独立架构站点 |
| Yema（野马） | 独立架构站点 |
| 朱雀 | 独立架构站点 |

## 文件说明

- `global.json`：全量规则，含通用规则和站点补充规则。
- `manifest.json`：更新索引。
- [RULES.md](RULES.md)：全字段说明及单独配置站点规则的方法。
- [MIT License](LICENSE)

规则、索引和适配列表手动维护，不使用生成脚本。
