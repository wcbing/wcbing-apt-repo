# wcbing（APT）软件源/仓库

供 Debian 系发行版用户使用的软件源，收集一些国内常用软件的二进制包。

收录的软件说明：
- 发布的是已打包的文件，不接受源码和自行打包。
- 有固定的更新地址，如官网和 Github Releases。
- 现只收录了 x86_64。

## 使用现有仓库

```sh
sudo curl -o /etc/apt/keyrings/wcbing.gpg https://deb.wcbing.top/wcbing.gpg

echo "deb [signed-by=/etc/apt/keyrings/wcbing.gpg] https://deb.wcbing.top /" | sudo tee /etc/apt/sources.list.d/wcbing.list
```

接下来执行 `sudo apt update` 更新即可。
