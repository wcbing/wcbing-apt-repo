# wcbing（APT）软件源/仓库

供 Debian 系发行版用户使用的软件源，收集一些国内常用软件的二进制包。

本仓库对于下载不受限的软件不提供文件托管服务，仅提供链接重定向功能，致力于在不改动 APT 的情况下实现类似 WinGet、Homebrew Cask 等仅提供仓库索引的效果。

收录的软件说明：
- 官方打包发布的文件 ~~，不接受第三方自行打包~~。
- 不收录打包的 wine 应用、Android 应用。
- 不收录图标、主题、字体等包，以后可能单独建一个相关仓库。
- 有固定的更新地址，如官网、官方仓库或 Github Releases。
- 现只收录了 x86_64，如有需要请参考最后一节自行建立仓库。

## 使用现有仓库

添加本仓库：
```sh
curl -fsSL https://packages.wcbing.top/deb/add.sh | sudo sh
```

移除本仓库：
```sh
curl -fsSL https://packages.wcbing.top/deb/del.sh | sudo sh
```

## 已收录软件

### 自行收集

|软件名|包名|地址|
|-|-|-|
|QQ|linuxqq|[官网](https://im.qq.com/linuxqq/)|
|QQ音乐|qqmusic|[官网](https://y.qq.com/download/download.html)|
|腾讯会议|wemeet|[官网](https://meeting.tencent.com/download/)|
|WPS Office|wps-office|[官网](https://linux.wps.cn/)|
|百度网盘|baidunetdisk|[官网](https://pan.baidu.com/download)|
|钉钉|com.alibabainc.dingtalk|[官网](https://www.dingtalk.com/download/)|
|飞书|bytedance-feishu-stable|[官网](https://www.feishu.cn/download)|
|Xmind|xmind-vana|[官网](https://xmind.cn/download/)|
|uTools|utools|[官网](https://u.tools/download/)|
|360安全浏览器|browser360-cn-stable|[官网](https://browser.360.net/gc/)|
|滴答清单|dida|[官网](https://dida365.com/download)|
|向日葵|sunloginclient<br />提取自 Debian 12 的依赖：<br />gconf2-common<br />libgconf-2-4|[官网](https://sunlogin.oray.com/download/linux)|
|ToDesk|todesk|[官网](https://www.todesk.com/linux.html)|
|微信|wechat|[官网](https://linux.weixin.qq.com/)|

> 临时收录软件会在仓库首页通知。

### Github Releses

|软件名|包名|地址|
|-|-|-|
|Clash Verge Rev|clash-verge|[Github Releses](https://github.com/clash-verge-rev/clash-verge-rev/releases)|
|FlClash|flclash|[Github Releses](https://github.com/chen08209/FlClash/releases)|
|mihomo|mihomo|[Github Releases](https://github.com/MetaCubeX/mihomo/releases)|
|hugo|hugo|[Github Releases](https://github.com/gohugoio/hugo/releases)|
|RustDesk|rustdesk|[Github Releases](https://github.com/rustdesk/rustdesk/releases)|
|Obsidian|obsidian|[Github Releases](https://github.com/obsidianmd/obsidian-releases/releases)|
|draw.io|draw.io|[Github Releases](https://github.com/jgraph/drawio-desktop/releases)|
|Tabby|tabby-terminal|[Github Releases](https://github.com/Eugeny/tabby/releases)|
|Pandoc|pandoc|[Github Releases](https://github.com/jgm/pandoc/releases)|
|TinyGo|tinygo|[Github Releases](https://github.com/tinygo-org/tinygo/releases)|
|LocalSend|localsend|[Github Releases](https://github.com/localsend/localsend/releases)|
|Motrix|motrix|[Github Releases](https://github.com/agalwood/Motrix/releases)|
|PeaZip|peazip|[Github Releases](https://github.com/peazip/PeaZip/releases)|
|Neovim/Nvim|neovim|[Github Releases](https://github.com/neovim/neovim-releases/releases)|
|思源笔记|siyuan|[Github Releases](https://github.com/siyuan-note/siyuan/releases)|
|Hiddify|hiddify|[Github Releases](https://github.com/hiddify/hiddify-app/releases)|

### 合并自官方 repo

|软件仓库|包名|
|-|-|
|Mozilla Firefox|firefox<br />firefox_beta<br />firefox_devedition<br />firefox_esr<br />firefox_nightly<br />mozillavpn|
|Google Chrome|google-chrome-stable<br />google-chrome-beta<br />google-chrome-unstable|
|Microsoft Edge|microsoft-edge-stable<br />microsoft-edge-beta<br />microsoft-edge-dev|
|Visual Studio Code|code<br />code-insiders<br />code-exploration|
|termius|termius-app<br />termius-beta|
|Sublime Text<br />Sublime Merge|sublime-text<br />sublime-merge|
|Steam|steam-launcher<br />steam-libs-amd64|
|Tailscale|tailscale<br />tailscale-nginx-auth|
|[black-desk 打包](https://github.com/black-desk/debs)|app.typst.typst<br />dev.neovide.neovide<br />dev.zed.zed<br />dev.zed.zed-pre<br />io.github.black-desk.debian-tweak<br />io.neovim.neovim<br />io.neovim.neovim-nightly<br />one.metacubex.clash-meta<br />org.pimalaya.himalaya|
|Typora|typora|
|Zotero|zotero<br />zotero-beta<br />zotero6|
|Github CLI|gh|


## 自建仓库

[参见 Wiki](https://github.com/wcbing/wcbing-apt-repo/wiki/self-hosting)
