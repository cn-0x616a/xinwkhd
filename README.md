# w12scan-client
网络资产搜索发现引擎,大规模资产识别，毕业设计，w12scan 客户端程序

## 扫描器架构

![jiagou](doc/w12scan.jpg)

## 插件规范
参见 [https://github.com/boy-hack/airbug](https://github.com/boy-hack/airbug)队列。

## Todo List
- [x] 插件调用采用线程方式在多线程中扫描
- [x] 插件的规范规则
- [ ] 完成WEB类插件
    - [x] BODY类
        - WAF识别
        - wappalyer分析
        - title
    - [x] 敏感文件扫描 
    - [ ] 优化备份文件扫描
    - [x] WEB指纹分析
        - [x] 可以远程调用AIRBUG https://github.com/boy-hack/airbug
    - [ ] bug漏洞添加log信息详情
    - [ ] 后台目录扫描(自动识别语言后扫描)
- [ ] 完成IP类插件
- [x] ip地理位置查询服务使用geo数据库

## For mac

- brew install masscan
- brew install nmap

sudo运行程序

# IP数据库更新
- 网络上大部分ip接口都有频率限制，所以IP数据使用GEOIP数据，但不保证数据的时效性，可以通过下载最新数据库解决
- https://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz  
- 放到data/GeoLite2目录下