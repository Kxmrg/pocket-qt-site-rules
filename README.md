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

<table>
  <tr><td>1PTBA（壹PT吧）</td><td>AGSV</td><td>alingPT</td></tr>
  <tr><td>Audiences（观众）</td><td>BTSchool（比特校园）</td><td>CarPT（车站）</td></tr>
  <tr><td>CHDBits</td><td>CPT（我的PT）</td><td>CrabPT（蟹黄堡）</td></tr>
  <tr><td>CSPT（财神）</td><td>CyanBug（大青虫）</td><td>大香蕉</td></tr>
  <tr><td>Depth Studio</td><td>DiscFan</td><td>Dubhe（天枢）</td></tr>
  <tr><td>Farmm（农场）</td><td>GGPT</td><td>HDArea（高清视界）</td></tr>
  <tr><td>HDDolby（HD杜比）</td><td>HDFans（红豆饭）</td><td>HDHome（家园）</td></tr>
  <tr><td>HDSky（天空）</td><td>HDTIME</td><td>HDU</td></tr>
  <tr><td>HhanClub（憨憨）</td><td>HTPT（海棠）</td><td>HXPT（好学）</td></tr>
  <tr><td>KEEPFRDS（朋友）</td><td>Kelu</td><td>Lajidui（垃圾堆）</td></tr>
  <tr><td>LONGPT</td><td>March</td><td>Moment</td></tr>
  <tr><td>Musopia（音乐乌托邦）</td><td>NanyangPT（南洋）</td><td>NicePT</td></tr>
  <tr><td>NovaHD</td><td>OpenCD</td><td>OurBits（我堡）</td></tr>
  <tr><td>PigGo（猪猪）</td><td>PlayLet</td><td>PTCafe（咖啡）</td></tr>
  <tr><td>PTerClub（猫站）</td><td>PTFans</td><td>PTGTK</td></tr>
  <tr><td>PTHOME</td><td>PTLGS</td><td>PTSBAO（烧包）</td></tr>
  <tr><td>PTSKIT（拾刻）</td><td>PTT</td><td>PTzone</td></tr>
  <tr><td>QingWaPT（青蛙）</td><td>RailgunPT</td><td>SewerPT（下水道）</td></tr>
  <tr><td>SoulVoice（聆音）</td><td>SSD（春天）</td><td>TangPT（不可躺）</td></tr>
  <tr><td>TCCF / ET8</td><td>TJUPT（北洋园）</td><td>TLFBits</td></tr>
  <tr><td>TTG（听听歌）</td><td>U2</td><td>UBits</td></tr>
  <tr><td>VC-Lib</td><td>星湾</td><td>星陨阁</td></tr>
  <tr><td>修道院</td><td>XLoli</td><td>ZMPT（织梦）</td></tr>
</table>

### UNIT3D 站点（2 个）

<table>
  <tr><td>AsianCinema</td><td>Blutopia</td><td></td></tr>
</table>

### BtiTracker 站点（2 个）

<table>
  <tr><td>HD-Space</td><td>HD-Torrents</td><td></td></tr>
</table>

### 独立架构站点（15 个）

<table>
  <tr><td>BeyondHD</td><td>Cinemageddon</td><td>Cola（可乐）</td></tr>
  <tr><td>ExoticaZ</td><td>FileList</td><td>Haidan（海胆）</td></tr>
  <tr><td>HDBits</td><td>KG</td><td>M-Team（馒头）</td></tr>
  <tr><td>Rousi（肉丝）</td><td>SunnyPT（阳光）</td><td>TorrentLeech</td></tr>
  <tr><td>Yema（野马）</td><td>Ying（影）</td><td>ZhuQue（朱雀）</td></tr>
</table>

## 文件说明

- `global.json`：全量规则，含通用规则和站点补充规则。
- `manifest.json`：更新索引。
- [RULES.md](RULES.md)：全字段说明及单独配置站点规则的方法。
- [MIT License](LICENSE)

规则、索引和适配列表手动维护，不使用生成脚本。
