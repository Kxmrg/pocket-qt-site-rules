# Pocket Evo App 站点规则官方更新源

提供 Pocket Evo App 的完整全局站点规则，包含通用规则与站点补充规则。

| 规则版本 | 更新时间（北京时间） | 已测试站点 |
| --- | --- | --- |
| version 24 | 2026-10-18 20:54:51 | 88 个 |

**更新源：** https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json

**官网：** https://kxmrg.com/

**浏览器插件：** https://github.com/Kxmrg/pocket-evo-extension

**Telegram：** https://t.me/pocket_qt

使用微信扫描下方二维码加入内测群。二维码有效期至 2026 年 10 月 20 日。

<img src="images/beta-group-qr.jpg" alt="Pocket Evo 内测群微信二维码" width="360" />

## 已测试完美适配站点

- **已测试站点**：下表 88 个站点均已测试并完美适配。
- **其他 NP 站点**：预计约 99% 可直接使用。未经单独适配的站点会在加载列表时自动获取标签 ID（tag_id），因此标签筛选项可能暂不完整，后续加载会继续补充。
- **适配进度**：GZ 架构正在适配中；UNIT3D 已接入，使用清单模式。
- **规则更新**：NP、UNIT3D 与 BtiTracker 使用本仓库的通用规则和站点补充规则；独立架构站点适配随 App 更新。
- **特殊站点**：部分改动较大的 NP 站点可能无法直接适配，遇到问题请联系我。

### NexusPHP 站点（69 个）

| 站点 | 站点 | 站点 | 站点 | 站点 |
| --- | --- | --- | --- | --- |
| 1PTBA（壹PT吧） | AGSV | alingPT | Audiences（观众） | BTSchool（比特校园） |
| CarPT（车站） | CHDBits | CPT（我的PT） | CrabPT（蟹黄堡） | CSPT（财神） |
| CyanBug（大青虫） | 大香蕉 | Depth Studio | DiscFan | Dubhe（天枢） |
| Farmm（农场） | GGPT | HDArea（高清视界） | HDDolby（HD杜比） | HDFans（红豆饭） |
| HDHome（家园） | HDSky（天空） | HDTIME | HDU | HhanClub（憨憨） |
| HTPT（海棠） | HXPT（好学） | KEEPFRDS（朋友） | Kelu | Lajidui（垃圾堆） |
| LONGPT | March | Moment | Musopia（音乐乌托邦） | NanyangPT（南洋） |
| NicePT | NovaHD | OpenCD | OurBits（我堡） | PigGo（猪猪） |
| PlayLet | PTCafe（咖啡） | PTerClub（猫站） | PTFans | PTGTK |
| PTHOME | PTLGS | PTSBAO（烧包） | PTSKIT（拾刻） | PTT |
| PTzone | QingWaPT（青蛙） | RailgunPT | SewerPT（下水道） | SoulVoice（聆音） |
| SSD（春天） | TangPT（不可躺） | TCCF / ET8 | TJUPT（北洋园） | TLFBits |
| TTG（听听歌） | U2 | UBits | VC-Lib | 星湾 |
| 星陨阁 | 修道院 | XLoli | ZMPT（织梦） |  |

### UNIT3D 站点（2 个）

| 站点 | 站点 | 站点 | 站点 | 站点 |
| --- | --- | --- | --- | --- |
| AsianCinema | Blutopia |  |  |  |

### BtiTracker 站点（2 个）

| 站点 | 站点 | 站点 | 站点 | 站点 |
| --- | --- | --- | --- | --- |
| HD-Space | HD-Torrents |  |  |  |

### 独立架构站点（15 个）

| 站点 | 站点 | 站点 | 站点 | 站点 |
| --- | --- | --- | --- | --- |
| BeyondHD | Cinemageddon | Cola（可乐） | ExoticaZ | FileList |
| Haidan（海胆） | HDBits | KG | M-Team（馒头） | Rousi（肉丝） |
| SunnyPT（阳光） | TorrentLeech | Yema（野马） | Ying（影） | ZhuQue（朱雀） |

## 文件说明

- `global.json`：全量规则，含通用规则和站点补充规则。
- `manifest.json`：更新索引。
- [RULES.md](RULES.md)：全字段说明及单独配置站点规则的方法。
- [MIT License](LICENSE)

规则、索引和适配列表手动维护，不使用生成脚本。
