# wcbing APT 软件源/仓库

适用于 Debian-based 发行版（Debian/Ubuntu/Mint/...）的 APT 软件源/仓库，收集一些常用软件的二进制包。

## 特色功能
- 本仓库仅提供链接重定向功能，在不改动 APT 的情况下实现了类似 WinGet、Homebrew Cask 等仅提供仓库索引的效果，确保了来源的安全可靠并规避了分发二进制文件可能导致的版权风险。
- 添加国内常用软件，更适合中国用户使用。
- 支持 AppStream（实验性），可以与你喜欢的图形软件商店（如 GNOME Software、KDE Plasma Discover）结合使用。


## 使用仓库

请点击 [现有仓库实例](https://packages.wcbing.top/deb/) 查看，里面有使用方法和[仓库内容列表](https://packages.wcbing.top/deb/list/)。


## 收录的软件说明
- 现主要服务 x86_64 用户，同时实验性支持 arm64。  
如有需要请参考最后一节自行建立仓库。
- 非开源、商业软件只收录官方打包发布的文件，不接受第三方自行打包的。
- 有固定的更新地址，如官网、官方仓库或 Github Releases。
- 不收录打包的 wine 应用、Android 应用。
- 不收录图标、主题、字体等包，这些单独建一个相关仓库。


## 部分已收录软件

### 部分自行收集软件

| 软件名 | 包名 | amd64 | arm64 |
| ----- | ---- | ----- | ----- |
| [QQ](https://im.qq.com/linuxqq/) | linuxqq | ✅ | ✅ |
| [QQ音乐](https://y.qq.com/download/download.html) | qqmusic | ✅ | |
| [腾讯会议](https://meeting.tencent.com/download/) | wemeet | ✅ | ✅ |
| [腾讯文档](https://docs.qq.com/home/download) | tdappdesktop | ✅ | ✅ |
| [WPS Office](https://linux.wps.cn/) | wps-office | ✅ | |
| [百度网盘](https://pan.baidu.com/download) | baidunetdisk | ✅ | |
| [钉钉](https://www.dingtalk.com/download/) | com.alibabainc.dingtalk | ✅ | ✅ |
| [飞书](https://www.feishu.cn/download) | bytedance-feishu-stable | ✅ | ✅ |
| [Xmind](https://xmind.cn/download/) | xmind-vana | ✅ | |
| [uTools](https://u.tools/download/) | utools | ✅ | |
| [360安全浏览器](https://browser.360.net/gc/) | browser360-cn-stable | ✅ | |
| [滴答清单](https://dida365.com/download) | dida | ✅ | ✅ |
| [向日葵](https://sunlogin.oray.com/download/linux) | sunloginclient<br />提取自 Debian 12 的依赖：<br />gconf2-common<br />libgconf-2-4 | ✅ | |
| [ToDesk](https://www.todesk.com/linux.html) | todesk | ✅ | |
| [微信](https://linux.weixin.qq.com/) | wechat | ✅ | ✅ |
| [欧路词典](https://www.eudic.net/v4/en/app/download) | eudic | ✅ | |


### Git Releses

收录使用 Github Releases 等分发 deb 包的软件。

现已迁移至独立仓库，直接利用 Github 服务器来高速下载、提取软件包的元信息。详见：https://github.com/wcbing-apt-repo/git-releases-to-apt-repo

### 合并自官方仓库

> 含部分官方承认的第三方仓库

| 软件仓库 | 包名 | amd64 | arm64 |
| ------ | ---- | ----- | ----- |
| [Mozilla Firefox](https://support.mozilla.org/zh-CN/kb/install-firefox-linux) | firefox<br />firefox_beta<br />firefox_devedition<br />firefox_nightly<br />firefox_esr<br />mozillavpn | ✅ | ✅ |
| Google Chrome | google-chrome-stable<br />google-chrome-beta<br />google-chrome-unstable | ✅ | |
| Google Earth | google-earth-pro-stable<br />google-earth-ec-stable | ✅ | |
| Chrome Remote Desktop | chrome-remote-desktop | ✅ | |
| Microsoft Edge | microsoft-edge-stable<br />microsoft-edge-beta<br />microsoft-edge-dev | ✅ | |
| Opera | opera-stable<br />opera-beta<br />opera-developer | ✅ | |
| Visual Studio Code | code<br />code-insiders<br />code-exploration | ✅ | ✅ |
| termius | termius-app<br />termius-beta | ✅ | |
| [Sublime Text<br />Sublime Merge](https://www.sublimetext.com/docs/linux_repositories.html) | sublime-text<br />sublime-merge | ✅ | ✅ |
| [Steam](https://repo.steampowered.com/steam/) | steam-launcher<br />steam-libs-amd64 | ✅ | |
| [Tailscale](https://pkgs.tailscale.com/stable/) | tailscale<br />tailscale-nginx-auth | ✅ | ✅ |
| [Typora](https://typora.io/#linux) | typora | ✅ | ✅ |
| [Zotero](https://zotero.retorque.re/file/apt-package-archive/index.html) | zotero<br />zotero-beta<br />zotero6 | ✅ | |
| [Github CLI](https://cli.github.com/) | gh | ✅ | ✅ |
| [NextTrace](https://github.com/nxtrace/nexttrace-debs) | nexttrace | ✅ | ✅ |
| [Gitea](https://gitlab.com/packaging/gitea)（[镜像](https://mirrors.ustc.edu.cn/help/packaging-gitea.html)） | gitea | ✅ | ✅ |
| [AnyDesk](https://deb.anydesk.com/howto.html) | anydesk | ✅ | ✅ |
| [Spotify](https://www.spotify.com/sg-zh/download/linux/) | spotify-client | ✅ | |
| [Free Download Manager](https://www.freedownloadmanager.org/zh/download-fdm-for-linux.htm) | freedownloadmanager | ✅ | |
| [WezTerm](https://wezterm.org/install/linux.html#using-the-apt-repo) | wezterm<br />wezterm-nightly | ✅ | ✅ |
| [Remote Desktop Manager](https://docs.devolutions.net/rdm/installation/client/?tab=linux) | remotedesktopmanager | ✅ | ✅ |
| [Discord](https://github.com/Javinator9889/Discord-PPA) 第三方仓库| discord | ✅ | |
| [Lutris](https://lutris.net/downloads) | lutris | ✅ | ✅ |


### 自行打包的开源软件

| 软件仓库 | 包名 | amd64 | arm64 |
| ------ | ---- | ----- | ----- |
| [Dufs](https://github.com/wcbing-build/dufs-debs) | dufs | ✅ | ✅ |
| [frp](https://github.com/wcbing-build/frp-debs) | frps<br />frpc | ✅ | ✅ |
| [Lazydocker](https://github.com/wcbing-build/lazydocker-debs) | lazydocker | ✅ | ✅ |
| [Lazygit](https://github.com/wcbing-build/lazygit-debs) | lazygit | ✅ | ✅ |
| [Neovide](https://github.com/wcbing-build/neovide-debs) | neovide | ✅ | |
| [Himalaya](https://github.com/wcbing-build/himalaya-debs) | himalaya | ✅ | ✅ |
| [File Browser](https://github.com/wcbing-build/filebrowser-debs) | filebrowser | ✅ | ✅ |
| [Microsoft Edit](https://github.com/wcbing-build/msedit-debs) | msedit | ✅ | ✅ |


## 自建仓库

[参见 Wiki](https://github.com/wcbing/wcbing-apt-repo/wiki/self-hosting)
