# wcbing（APT）软件源/仓库

供 Debian 系发行版用户使用的软件源，收集一些国内常用软件的二进制包。

收录的软件说明：
- 发布的是已打包的文件，不接受第三方自行打包。
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

|软件名|包名|渠道|架构|
|-|-|-|-|
|QQ|linuxqq|[官网](https://im.qq.com/linuxqq/)|x86_64|
|QQ音乐|qqmusic|[官网](https://y.qq.com/download/download.html)|x86_64|
|腾讯会议|wemeet|[官网](https://meeting.tencent.com/download/)|x86_64|
|Clash Verge Rev|clash-verge|[Github Releses](https://github.com/clash-verge-rev/clash-verge-rev/releases)|x86_64|
|FlClash|flclash|[Github Releses](https://github.com/chen08209/FlClash/releases)|x86_64|
|mihomo|mihomo|[Github Releases](https://github.com/MetaCubeX/mihomo/releases)|x86_64|
|hugo|hugo|[Github Releases](https://github.com/gohugoio/hugo/releases)|x86_64|
|RustDesk|rustdesk|[Github Releases](https://github.com/rustdesk/rustdesk/releases)|x86_64|
|Visual Studio Code|code|[官网](https://code.visualstudio.com)|x86_64|
|Microsoft Edge|microsoft-edge-stable|[官网](https://www.microsoft.com/en-us/edge/download)|x86_64|
|Google Chrome|google-chrome-stable<br />google-chrome-beta<br />google-chrome-unstable|官方仓库|x86_64|
|Obsidian|obsidian|[Github Releases](https://github.com/obsidianmd/obsidian-releases/releases)|x86_64|
|WPS Office|wps-office|[官网](https://linux.wps.cn/)|x86_64|
|百度网盘|baidunetdisk|[官网](https://pan.baidu.com/download)|x86_64|
|钉钉|com.alibabainc.dingtalk|[官网](https://www.dingtalk.com/download/)|x86_64|
|飞书|bytedance-feishu-stable|[官网](https://www.feishu.cn/download)|x86_64|
|termius|termius-app<br />termius-beta|官方仓库|x86_64|
|Sublime Text<br />Sublime Merge|sublime-text<br />sublime-merge|官方仓库|x86_64, arm64|
|Xmind|xmind-vana|[官网](https://xmind.cn/download/)|x86_64|
|Mozilla Firefox|firefox<br />firefox_beta<br />firefox_devedition<br />firefox_esr<br />firefox_nightly<br />|官方仓库|x86_64|


## 自建仓库

[参见 Wiki](https://github.com/wcbing/wcbing-apt-repo/wiki/self-hosting)
