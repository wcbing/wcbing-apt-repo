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

可在 [这里](https://packages.wcbing.top/deb/status.txt) 查看具体版本。

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


## 自行建立仓库

### 建立仓库

1. clone 本仓库，进入仓库目录。
2. 确认系统安装有 `Requests` Python 库，Debian 系应该自带。
2. 运行 `init_deb.py` 初始化。  
默认只新建 x86_64，需要其他架构请修改其中的SQL语句。
3. 创建一个**无密码**的 GPG 密钥对，导出 GPG 公钥文件待用。
4. 创建定时任务，定时运行 `update_gen.sh`  
crontab 样例：0 11,15,19 * * * cd [THIS_DIR] && ./update_gen.sh > ./deb/status.txt

### 发布与使用

这个仓库使用了[扁平仓库格式（Flat Repository Format）](https://wiki.debian.org/DebianRepository/Format#Flat_Repository_Format)。建立好后使用 Web 服务器将 `deb` 目录暴露出去即可。

使用时可参考前面已有的配置，先将第3部提到的 GPG 公钥导入，再新建软件源配置文件。

实际使用中官网提供的下载链接一般是 CDN 链接，为提升下载速度，减轻自建源压力，建议将这些请求重定向到官网上。而国内下载 Github 上的文件时比较慢，仍然从自建源下载。

nginx 配置参考：
```nginx
server {
    server_name packages.wcbing.top;
    autoindex on;
    autoindex_exact_size off;
    autoindex_localtime on;
    charset 'utf-8';
    location ~ ^/deb/https:/github.com {
        root /packages;
    }
    location ~ ^/deb/https:/(.+)$ {
        return 302 https://$1;
    }
    location / { 
        root /packages;
    }
}
```