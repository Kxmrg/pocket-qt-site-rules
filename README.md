# Pocket Evo App 站点规则官方更新源

提供 Pocket Evo App 的完整全局站点规则，包含通用规则与站点补充规则。

| 规则版本 | 更新时间（北京时间） | 已测试站点 |
| --- | --- | --- |
| version 20 | 2026-10-15 16:18:03 | 67 个 |

**更新源：** https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json

**官网：** https://kxmrg.com/

**浏览器插件：** https://github.com/Kxmrg/pocket-evo-extension

**Telegram：** https://t.me/pocket_qt

使用微信扫描下方二维码加入内测群。二维码有效期至 2026 年 10 月 20 日。

<img src="images/beta-group-qr.jpg" alt="Pocket Evo 内测群微信二维码" width="360" />

## 已测试完美适配站点

- **已测试站点**：下表 67 个站点均已测试并完美适配。
- **其他 NP 站点**：预计约 99% 可直接使用。未经单独适配的站点会在加载列表时自动获取标签 ID（tag_id），因此标签筛选项可能暂不完整，后续加载会继续补充。
- **适配进度**：GZ、U3D 架构正在适配中。
- **特殊站点**：部分改动较大的 NP 站点可能无法直接适配，遇到问题请联系我。

独立架构站点适配随 App 更新，不由规则文件更新。

### NexusPHP 站点（61 个）

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

### 独立架构站点（6 个）

| 站点 | 架构 |
| --- | --- |
| 朱雀 | 独立架构站点 |
| M-Team（馒头） | 独立架构站点 |
| 海胆 | 独立架构站点 |
| SunnyPT（阳光） | 独立架构站点 |
| Rousi（肉丝） | 独立架构站点 |
| Yema（野马） | 独立架构站点 |

## 文件说明

- `global.json`：全量规则，含通用规则和站点补充规则。
- `manifest.json`：更新索引。
- [RULES.md](RULES.md)：全字段说明及单独配置站点规则的方法。
- [MIT License](LICENSE)

规则、索引和适配列表手动维护，不使用生成脚本。
