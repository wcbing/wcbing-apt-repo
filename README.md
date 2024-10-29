# wcbing（APT）软件源/仓库

供 Debian 系发行版用户使用的软件源，收集一些国内常用软件的二进制包。

收录的软件说明：
- 发布的是已打包的文件 ~~，不接受第三方自行打包~~。
- 有固定的更新地址，如官网、官方仓库或 Github Releases。
- 本仓库对于国内网络下载不受限的软件不提供文件托管服务，仅提供链接重定向功能，最终效果类似 winget。
- 现只收录了 x86_64，如有需要请参考最后一节自行建立仓库。

## 使用现有仓库

```sh
sudo curl -o /etc/apt/keyrings/wcbing.gpg https://packages.wcbing.top/wcbing.gpg

echo "deb [signed-by=/etc/apt/keyrings/wcbing.gpg] https://packages.wcbing.top/deb /" | sudo tee /etc/apt/sources.list.d/wcbing.list
```

接下来执行 `sudo apt update` 更新即可。


## 现有软件

可在 [这里](https://packages.wcbing.top/deb/version.txt) 查看具体版本。

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

### 合并自官方 repo

|软件仓库|包名|
|-|-|
|Mozilla Firefox|firefox<br />firefox_beta<br />firefox_devedition<br />firefox_esr<br />firefox_nightly|
|Google Chrome|google-chrome-stable<br />google-chrome-beta<br />google-chrome-unstable|
|Microsoft Edge|microsoft-edge-stable<br />microsoft-edge-beta<br />microsoft-edge-dev|
|Visual Studio Code|code<br />code-insiders<br />code-exploration|
|termius|termius-app<br />termius-beta|
|Sublime Text<br />Sublime Merge|sublime-text<br />sublime-merge|
|Steam|steam-launcher<br />steam-libs-amd64|
|Tailscale|tailscale<br />tailscale-nginx-auth|
|[black-desk 打包](https://github.com/black-desk/debs)|app.typst.typst<br />dev.neovide.neovide<br />dev.zed.zed<br />dev.zed.zed-pre<br />io.github.black-desk.debian-tweak<br />io.neovim.neovim<br />io.neovim.neovim-nightly<br />one.metacubex.clash-meta<br />org.pimalaya.himalaya|


## 自建仓库

[参见 Wiki](https://github.com/wcbing/wcbing-apt-repo/wiki/self-hosting)
