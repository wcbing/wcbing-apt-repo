VERSION=$(curl -s https://innovfile.eastmoney.com/innovfile/prd/pcversionCfg.json | jq -r '.kylin')

# AMD64
AMD64_URL=https://choice-app.eastmoney.com/choice/OfflinePackage/ChoiceSetup_kylin_x86.deb
./check_downloader.py com.eastmoney.choice "$VERSION" "$AMD64_URL" amd64

# ARM64
ARM64_URL=https://choice-app.eastmoney.com/choice/OfflinePackage/ChoiceSetup_kylin_arm.deb
./check_downloader.py com.eastmoney.choice "$VERSION" "$ARM64_URL" arm64
