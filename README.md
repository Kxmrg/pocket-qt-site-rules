# Pocket Evo App 站点规则官方更新源

Pocket Evo 是 Pocket Qt 的完全重制版，在用户交互、站点适配、软件功能方面都进行了全面优化。之前如果站点修改了页面布局，Pocket Qt 就必须通过升级应用才能进行修复适配，Pocket Evo 开发了全新的适配引擎，可以通过在线更新适配规则直接修复，无需频繁更新应用。

| 规则版本 | 更新时间（北京时间） | 支持 PT 站点 | 已测试完美适配站点 |
| --- | --- | --- | --- |
| version 43 | 2026-10-20 23:50:10 | 200+ | 101 |

**在线更新源：** https://raw.githubusercontent.com/Kxmrg/pocket-qt-site-rules/main/manifest.json

**官网：** https://kxmrg.com/

**浏览器插件：** https://github.com/Kxmrg/pocket-evo-extension

**Telegram：** https://t.me/pocket_evo



## 适配清单

目前经测试已完美适配PT站点101个，NexusPHP、Gazelle、UNIT3D、BtiTracker 架构站点可以通过本仓库的通用规则和站点补充规则在线更新。独立架构站点适配跟随应用更新，无法在线修复。未测试的NexusPHP站点绝大部分都是可以直接导入使用的，因未测试无法获取完整的标签 ID（tag_id），Pocket Evo 会在加载资源列表的同时采集标签 ID，会造成无法筛选已加载资源列表中没有的标签。部分NexusPHP站点改动较大，如无法适配请联系我进行在线修复。


### NexusPHP 站点（71 个）

<table width="100%">
  <tr><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />1<wbr>P<wbr>T<wbr>B<wbr>A<wbr>（<wbr>壹<wbr>P<wbr>T<wbr>吧<wbr>）</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />A<wbr>G<wbr>S<wbr>V</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />a<wbr>l<wbr>i<wbr>n<wbr>g<wbr>P<wbr>T</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />A<wbr>u<wbr>d<wbr>i<wbr>e<wbr>n<wbr>c<wbr>e<wbr>s<wbr>（<wbr>观<wbr>众<wbr>）</td></tr>
  <tr><td width="25%">B<wbr>T<wbr>S<wbr>c<wbr>h<wbr>o<wbr>o<wbr>l<wbr>（<wbr>比<wbr>特<wbr>校<wbr>园<wbr>）</td><td width="25%">C<wbr>a<wbr>r<wbr>P<wbr>T<wbr>（<wbr>车<wbr>站<wbr>）</td><td width="25%">C<wbr>H<wbr>D<wbr>B<wbr>i<wbr>t<wbr>s</td><td width="25%">C<wbr>P<wbr>T<wbr>（<wbr>我<wbr>的<wbr>P<wbr>T<wbr>）</td></tr>
  <tr><td width="25%">C<wbr>r<wbr>a<wbr>b<wbr>P<wbr>T<wbr>（<wbr>蟹<wbr>黄<wbr>堡<wbr>）</td><td width="25%">C<wbr>S<wbr>P<wbr>T<wbr>（<wbr>财<wbr>神<wbr>）</td><td width="25%">C<wbr>y<wbr>a<wbr>n<wbr>B<wbr>u<wbr>g<wbr>（<wbr>大<wbr>青<wbr>虫<wbr>）</td><td width="25%">大<wbr>香<wbr>蕉</td></tr>
  <tr><td width="25%">D<wbr>e<wbr>p<wbr>t<wbr>h<wbr> <wbr>S<wbr>t<wbr>u<wbr>d<wbr>i<wbr>o</td><td width="25%">D<wbr>i<wbr>s<wbr>c<wbr>F<wbr>a<wbr>n</td><td width="25%">D<wbr>u<wbr>b<wbr>h<wbr>e<wbr>（<wbr>天<wbr>枢<wbr>）</td><td width="25%">F<wbr>a<wbr>r<wbr>m<wbr>m<wbr>（<wbr>农<wbr>场<wbr>）</td></tr>
  <tr><td width="25%">G<wbr>G<wbr>P<wbr>T</td><td width="25%">H<wbr>D<wbr>A<wbr>r<wbr>e<wbr>a<wbr>（<wbr>高<wbr>清<wbr>视<wbr>界<wbr>）</td><td width="25%">H<wbr>D<wbr>D<wbr>o<wbr>l<wbr>b<wbr>y<wbr>（<wbr>H<wbr>D<wbr>杜<wbr>比<wbr>）</td><td width="25%">H<wbr>D<wbr>F<wbr>a<wbr>n<wbr>s<wbr>（<wbr>红<wbr>豆<wbr>饭<wbr>）</td></tr>
  <tr><td width="25%">H<wbr>D<wbr>H<wbr>o<wbr>m<wbr>e<wbr>（<wbr>家<wbr>园<wbr>）</td><td width="25%">H<wbr>D<wbr>S<wbr>k<wbr>y<wbr>（<wbr>天<wbr>空<wbr>）</td><td width="25%">H<wbr>D<wbr>T<wbr>I<wbr>M<wbr>E</td><td width="25%">H<wbr>D<wbr>U</td></tr>
  <tr><td width="25%">H<wbr>D<wbr>W<wbr>i<wbr>n<wbr>g<wbr>（<wbr>瓷<wbr>）</td><td width="25%">H<wbr>h<wbr>a<wbr>n<wbr>C<wbr>l<wbr>u<wbr>b<wbr>（<wbr>憨<wbr>憨<wbr>）</td><td width="25%">H<wbr>T<wbr>P<wbr>T<wbr>（<wbr>海<wbr>棠<wbr>）</td><td width="25%">H<wbr>X<wbr>P<wbr>T<wbr>（<wbr>好<wbr>学<wbr>）</td></tr>
  <tr><td width="25%">K<wbr>E<wbr>E<wbr>P<wbr>F<wbr>R<wbr>D<wbr>S<wbr>（<wbr>朋<wbr>友<wbr>）</td><td width="25%">K<wbr>e<wbr>l<wbr>u</td><td width="25%">L<wbr>a<wbr>j<wbr>i<wbr>d<wbr>u<wbr>i<wbr>（<wbr>垃<wbr>圾<wbr>堆<wbr>）</td><td width="25%">L<wbr>O<wbr>N<wbr>G<wbr>P<wbr>T</td></tr>
  <tr><td width="25%">M<wbr>a<wbr>r<wbr>c<wbr>h</td><td width="25%">M<wbr>o<wbr>m<wbr>e<wbr>n<wbr>t</td><td width="25%">M<wbr>u<wbr>s<wbr>o<wbr>p<wbr>i<wbr>a<wbr>（<wbr>音<wbr>乐<wbr>乌<wbr>托<wbr>邦<wbr>）</td><td width="25%">N<wbr>a<wbr>n<wbr>y<wbr>a<wbr>n<wbr>g<wbr>P<wbr>T<wbr>（<wbr>南<wbr>洋<wbr>）</td></tr>
  <tr><td width="25%">N<wbr>i<wbr>c<wbr>e<wbr>P<wbr>T</td><td width="25%">N<wbr>o<wbr>v<wbr>a<wbr>H<wbr>D</td><td width="25%">O<wbr>p<wbr>e<wbr>n<wbr>C<wbr>D</td><td width="25%">O<wbr>u<wbr>r<wbr>B<wbr>i<wbr>t<wbr>s<wbr>（<wbr>我<wbr>堡<wbr>）</td></tr>
  <tr><td width="25%">P<wbr>i<wbr>g<wbr>G<wbr>o<wbr>（<wbr>猪<wbr>猪<wbr>）</td><td width="25%">P<wbr>l<wbr>a<wbr>y<wbr>L<wbr>e<wbr>t</td><td width="25%">P<wbr>T<wbr>C<wbr>a<wbr>f<wbr>e<wbr>（<wbr>咖<wbr>啡<wbr>）</td><td width="25%">P<wbr>T<wbr>e<wbr>r<wbr>C<wbr>l<wbr>u<wbr>b<wbr>（<wbr>猫<wbr>站<wbr>）</td></tr>
  <tr><td width="25%">P<wbr>T<wbr>F<wbr>a<wbr>n<wbr>s</td><td width="25%">P<wbr>T<wbr>G<wbr>T<wbr>K</td><td width="25%">P<wbr>T<wbr>H<wbr>O<wbr>M<wbr>E</td><td width="25%">P<wbr>T<wbr>L<wbr>G<wbr>S</td></tr>
  <tr><td width="25%">P<wbr>T<wbr>S<wbr>B<wbr>A<wbr>O<wbr>（<wbr>烧<wbr>包<wbr>）</td><td width="25%">P<wbr>T<wbr>S<wbr>K<wbr>I<wbr>T<wbr>（<wbr>拾<wbr>刻<wbr>）</td><td width="25%">P<wbr>T<wbr>T</td><td width="25%">P<wbr>T<wbr>z<wbr>o<wbr>n<wbr>e</td></tr>
  <tr><td width="25%">S<wbr>J<wbr>T<wbr>U<wbr>（<wbr>葡<wbr>萄<wbr>）</td><td width="25%">Q<wbr>i<wbr>n<wbr>g<wbr>W<wbr>a<wbr>P<wbr>T<wbr>（<wbr>青<wbr>蛙<wbr>）</td><td width="25%">R<wbr>a<wbr>i<wbr>l<wbr>g<wbr>u<wbr>n<wbr>P<wbr>T</td><td width="25%">S<wbr>e<wbr>w<wbr>e<wbr>r<wbr>P<wbr>T<wbr>（<wbr>下<wbr>水<wbr>道<wbr>）</td></tr>
  <tr><td width="25%">S<wbr>o<wbr>u<wbr>l<wbr>V<wbr>o<wbr>i<wbr>c<wbr>e<wbr>（<wbr>聆<wbr>音<wbr>）</td><td width="25%">S<wbr>S<wbr>D<wbr>（<wbr>春<wbr>天<wbr>）</td><td width="25%">T<wbr>a<wbr>n<wbr>g<wbr>P<wbr>T<wbr>（<wbr>不<wbr>可<wbr>躺<wbr>）</td><td width="25%">T<wbr>C<wbr>C<wbr>F<wbr> <wbr>/<wbr> <wbr>E<wbr>T<wbr>8</td></tr>
  <tr><td width="25%">T<wbr>J<wbr>U<wbr>P<wbr>T<wbr>（<wbr>北<wbr>洋<wbr>园<wbr>）</td><td width="25%">T<wbr>L<wbr>F<wbr>B<wbr>i<wbr>t<wbr>s</td><td width="25%">T<wbr>T<wbr>G<wbr>（<wbr>听<wbr>听<wbr>歌<wbr>）</td><td width="25%">U<wbr>2</td></tr>
  <tr><td width="25%">U<wbr>B<wbr>i<wbr>t<wbr>s</td><td width="25%">V<wbr>C<wbr>-<wbr>L<wbr>i<wbr>b</td><td width="25%">星<wbr>湾</td><td width="25%">星<wbr>陨<wbr>阁</td></tr>
  <tr><td width="25%">修<wbr>道<wbr>院</td><td width="25%">X<wbr>L<wbr>o<wbr>l<wbr>i</td><td width="25%">Z<wbr>M<wbr>P<wbr>T<wbr>（<wbr>织<wbr>梦<wbr>）</td><td width="25%"></td></tr>
</table>

### Gazelle 站点（11 个）

<table width="100%">
  <tr><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />A<wbr>l<wbr>p<wbr>h<wbr>a<wbr>R<wbr>a<wbr>t<wbr>i<wbr>o</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />A<wbr>n<wbr>t<wbr>h<wbr>e<wbr>l<wbr>i<wbr>o<wbr>n</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />B<wbr>r<wbr>o<wbr>a<wbr>d<wbr>c<wbr>a<wbr>s<wbr>T<wbr>h<wbr>e<wbr>N<wbr>e<wbr>t</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />B<wbr>r<wbr>o<wbr>k<wbr>e<wbr>n<wbr>S<wbr>t<wbr>o<wbr>n<wbr>e<wbr>s</td></tr>
  <tr><td width="25%">D<wbr>I<wbr>C<wbr>M<wbr>u<wbr>s<wbr>i<wbr>c</td><td width="25%">E<wbr>m<wbr>p<wbr>o<wbr>r<wbr>n<wbr>i<wbr>u<wbr>m</td><td width="25%">G<wbr>a<wbr>z<wbr>e<wbr>l<wbr>l<wbr>e<wbr>G<wbr>a<wbr>m<wbr>e<wbr>s</td><td width="25%">G<wbr>r<wbr>e<wbr>a<wbr>t<wbr> <wbr>P<wbr>o<wbr>s<wbr>t<wbr>e<wbr>r<wbr> <wbr>W<wbr>a<wbr>l<wbr>l</td></tr>
  <tr><td width="25%">H<wbr>D<wbr>-<wbr>F</td><td width="25%">P<wbr>a<wbr>s<wbr>s<wbr>T<wbr>h<wbr>e<wbr>P<wbr>o<wbr>p<wbr>c<wbr>o<wbr>r<wbr>n</td><td width="25%">R<wbr>e<wbr>d<wbr>a<wbr>c<wbr>t<wbr>e<wbr>d</td><td width="25%"></td></tr>
</table>

### UNIT3D 站点（2 个）

<table width="100%">
  <tr><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />A<wbr>s<wbr>i<wbr>a<wbr>n<wbr>C<wbr>i<wbr>n<wbr>e<wbr>m<wbr>a</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />B<wbr>l<wbr>u<wbr>t<wbr>o<wbr>p<wbr>i<wbr>a</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" /></td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" /></td></tr>
</table>

### BtiTracker 及其衍生 XBTIT 站点（2 个）

<table width="100%">
  <tr><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />H<wbr>D<wbr>-<wbr>S<wbr>p<wbr>a<wbr>c<wbr>e</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />H<wbr>D<wbr>-<wbr>T<wbr>o<wbr>r<wbr>r<wbr>e<wbr>n<wbr>t<wbr>s</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" /></td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" /></td></tr>
</table>

### 独立架构站点（15 个）

<table width="100%">
  <tr><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />B<wbr>e<wbr>y<wbr>o<wbr>n<wbr>d<wbr>H<wbr>D</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />C<wbr>i<wbr>n<wbr>e<wbr>m<wbr>a<wbr>g<wbr>e<wbr>d<wbr>d<wbr>o<wbr>n</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />C<wbr>o<wbr>l<wbr>a<wbr>（<wbr>可<wbr>乐<wbr>）</td><td width="25%"><img src="images/table-spacer.png" width="2000" height="0" align="right" alt="" />E<wbr>x<wbr>o<wbr>t<wbr>i<wbr>c<wbr>a<wbr>Z</td></tr>
  <tr><td width="25%">F<wbr>i<wbr>l<wbr>e<wbr>L<wbr>i<wbr>s<wbr>t</td><td width="25%">H<wbr>a<wbr>i<wbr>d<wbr>a<wbr>n<wbr>（<wbr>海<wbr>胆<wbr>）</td><td width="25%">H<wbr>D<wbr>B<wbr>i<wbr>t<wbr>s</td><td width="25%">K<wbr>G</td></tr>
  <tr><td width="25%">M<wbr>-<wbr>T<wbr>e<wbr>a<wbr>m<wbr>（<wbr>馒<wbr>头<wbr>）</td><td width="25%">R<wbr>o<wbr>u<wbr>s<wbr>i<wbr>（<wbr>肉<wbr>丝<wbr>）</td><td width="25%">S<wbr>u<wbr>n<wbr>n<wbr>y<wbr>P<wbr>T<wbr>（<wbr>阳<wbr>光<wbr>）</td><td width="25%">T<wbr>o<wbr>r<wbr>r<wbr>e<wbr>n<wbr>t<wbr>L<wbr>e<wbr>e<wbr>c<wbr>h</td></tr>
  <tr><td width="25%">Y<wbr>e<wbr>m<wbr>a<wbr>（<wbr>野<wbr>马<wbr>）</td><td width="25%">Y<wbr>i<wbr>n<wbr>g<wbr>（<wbr>影<wbr>）</td><td width="25%">Z<wbr>h<wbr>u<wbr>Q<wbr>u<wbr>e<wbr>（<wbr>朱<wbr>雀<wbr>）</td><td width="25%"></td></tr>
</table>

## 文件说明

- `global.json`：全量规则，含通用规则和站点补充规则。
- `manifest.json`：更新索引。
- [RULES.md](RULES.md)：全字段说明及单独配置站点规则的方法。
- [MIT License](LICENSE)

规则、索引和适配列表手动维护，不使用生成脚本。
