# **Quotes** 
获取国内、外实时行情;速度快，操作简单、数据稳定

![Travis](https://travis-ci.org/geatpy-dev/geatpy.svg?branch=master)
[![Package Status](https://img.shields.io/pypi/status/geatpy.svg)](https://pypi.org/project/geatpy/)
[![License](https://img.shields.io/pypi/l/geatpy.svg)](https://github.com/geatpy-dev/geatpy/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.6.svg)
![Pypi](https://img.shields.io/badge/pypi-2.2.3-blue.svg)

## 10s获取国内外实时行情(期货、现货)
* **配置文件**: Bin/Config.py
* **主文件** : Quotes.exe

## 配置文件
1.账号信息:

    account = 'TEST001'
    
2.配置发布方式
    
    publish = 0  # 0是打印;1是redis;2是socket;3是file

3.配置发布信息

    # 如果publish==1,需要配置redis
    redis = {'host': 'localhost',
             'port': 6379,
             'db': 0,
            'password': None
            }
    # 如果publish==2,需要配置socket
    socket = {'ip': '127.0.0.1',
              'port': 8080}

## 主文件
双击运行即可

## 行情获取实例

    {"lastprice":"47460",
    "jingdu":0,
    "perprice":"0.21",
    "prono":"CU1912",
    "tprice":0,
    "zhangdie":"100",
    "buyPrice":47460,
    "buyNums":2,
    "salePrice":47470,
    "saleNums":11,
    "priceMax":"47670",
    "priceMin":"47330",
    "openPrice":0,
    "closePrice":"0",
    "catid":14,
    "heightPrice":47670,
    "lowerPrice":47330,
    "preClosePrice":47460,
    "chicang":6,
    "preChicang":0,
    "preJiePrice":47360,
    "volume":69466,
    "zhangting":0,
    "dieting":0}

## 有任何问题可以随时联系我:QQ976308589