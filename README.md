# Pocket Evo App 站点规则官方更新源

提供 Pocket Evo App 的完整全局站点规则，包含通用规则与站点补充规则。

| 规则版本 | 更新时间（北京时间） | 已测试站点 |
| --- | --- | --- |
| version 23 | 2026-10-18 16:55:06 | 79 个 |

**更新源：** https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json

**官网：** https://kxmrg.com/

**浏览器插件：** https://github.com/Kxmrg/pocket-evo-extension

**Telegram：** https://t.me/pocket_qt

使用微信扫描下方二维码加入内测群。二维码有效期至 2026 年 10 月 20 日。

<img src="images/beta-group-qr.jpg" alt="Pocket Evo 内测群微信二维码" width="360" />

## 已测试完美适配站点

- **已测试站点**：下表 79 个站点均已测试并完美适配。
- **其他 NP 站点**：预计约 99% 可直接使用。未经单独适配的站点会在加载列表时自动获取标签 ID（tag_id），因此标签筛选项可能暂不完整，后续加载会继续补充。
- **适配进度**：GZ 架构正在适配中；UNIT3D 已接入，使用清单模式。
- **规则更新**：NP 与 UNIT3D 使用本仓库的通用规则和站点补充规则；独立架构站点适配随 App 更新。
- **特殊站点**：部分改动较大的 NP 站点可能无法直接适配，遇到问题请联系我。

### NexusPHP 站点（69 个）

| 站点 | 架构 |
| --- | --- |
| 1PTBA（壹PT吧） | NexusPHP |
| AGSV | NexusPHP |
| alingPT | NexusPHP |
| Audiences（观众） | NexusPHP |
| BTSchool（比特校园） | NexusPHP |
| CarPT（车站） | NexusPHP |
| CHDBits | NexusPHP |
| CPT（我的PT） | NexusPHP |
| CrabPT（蟹黄堡） | NexusPHP |
| CSPT（财神） | NexusPHP |
| CyanBug（大青虫） | NexusPHP |
| 大香蕉 | NexusPHP |
| Depth Studio | NexusPHP |
| DiscFan | NexusPHP |
| Dubhe（天枢） | NexusPHP |
| Farmm（农场） | NexusPHP |
| GGPT | NexusPHP |
| HDArea（高清视界） | NexusPHP |
| HDDolby（HD杜比） | NexusPHP |
| HDFans（红豆饭） | NexusPHP |
| HDHome（家园） | NexusPHP |
| HDSky（天空） | NexusPHP |
| HDTIME | NexusPHP |
| HDU | NexusPHP |
| HhanClub（憨憨） | NexusPHP |
| HTPT（海棠） | NexusPHP |
| HXPT（好学） | NexusPHP |
| KEEPFRDS（朋友） | NexusPHP |
| Kelu | NexusPHP |
| Lajidui（垃圾堆） | NexusPHP |
| LONGPT | NexusPHP |
| March | NexusPHP |
| Moment | NexusPHP |
| Musopia（音乐乌托邦） | NexusPHP |
| NanyangPT（南洋） | NexusPHP |
| NicePT | NexusPHP |
| NovaHD | NexusPHP |
| OpenCD | NexusPHP |
| OurBits（我堡） | NexusPHP |
| PigGo（猪猪） | NexusPHP |
| PlayLet | NexusPHP |
| PTCafe（咖啡） | NexusPHP |
| PTerClub（猫站） | NexusPHP |
| PTFans | NexusPHP |
| PTGTK | NexusPHP |
| PTHOME | NexusPHP |
| PTLGS | NexusPHP |
| PTSBAO（烧包） | NexusPHP |
| PTSKIT（拾刻） | NexusPHP |
| PTT | NexusPHP |
| PTzone | NexusPHP |
| QingWaPT（青蛙） | NexusPHP |
| RailgunPT | NexusPHP |
| SewerPT（下水道） | NexusPHP |
| SoulVoice（聆音） | NexusPHP |
| SSD（春天） | NexusPHP |
| TangPT（不可躺） | NexusPHP |
| TCCF / ET8 | NexusPHP |
| TJUPT（北洋园） | NexusPHP |
| TLFBits | NexusPHP |
| TTG（听听歌） | NexusPHP |
| U2 | NexusPHP |
| UBits | NexusPHP |
| VC-Lib | NexusPHP |
| 星湾 | NexusPHP |
| 星陨阁 | NexusPHP |
| 修道院 | NexusPHP |
| XLoli | NexusPHP |
| ZMPT（织梦） | NexusPHP |

### UNIT3D 站点（2 个）

| 站点 | 架构 |
| --- | --- |
| AsianCinema | UNIT3D |
| Blutopia | UNIT3D |

### 独立架构站点（8 个）

| 站点 | 架构 |
| --- | --- |
| BeyondHD | 独立架构站点 |
| Cola（可乐） | 独立架构站点 |
| Haidan（海胆） | 独立架构站点 |
| M-Team（馒头） | 独立架构站点 |
| Rousi（肉丝） | 独立架构站点 |
| SunnyPT（阳光） | 独立架构站点 |
| Yema（野马） | 独立架构站点 |
| ZhuQue（朱雀） | 独立架构站点 |

## 文件说明

- `global.json`：全量规则，含通用规则和站点补充规则。
- `manifest.json`：更新索引。
- [RULES.md](RULES.md)：全字段说明及单独配置站点规则的方法。
- [MIT License](LICENSE)

规则、索引和适配列表手动维护，不使用生成脚本。
