# coding:utf-8
import logging
import os

env = os.getenv("lady_env")

# 默认开发环境
if env == "prod":
    # 已有的插件需要在这里注册
    plugins_map = {
        # 子域名
        "lijiejie": {
            "classname": "LijiejieSubDomainBrute",
            "plugin_absolute_path": "/data/cute/crontab/third_party/subDomainsBrute",
        },
        "sublist3r": {
            "classname": "Sublist3rSubDomainBrute",
            "plugin_absolute_path": "/data/cute/crontab/third_party/Sublist3r",
        },
        "feei": {
            "classname": "FeeiSubDomainBrute",
            "plugin_absolute_path": "/data/cute/crontab/third_party/ESD",
        },
        # 兄弟域名
        "icp": {
            "classname": "IcpBrotherDomain",
            "plugin_absolute_path": "",
        },
    }
    proxies = {}
    host = "https://139.199.206.110"
    header = {
        "Host": "cute.leveryd.top",
    }
else:
    debug = False
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        proxies = {"http": "127.0.0.1:8087"}
        host = "http://127.0.0.1:5000"
    else:
        proxies = {}
        host = "http://127.0.0.1:5000"
        header = {}

    # 已有的插件需要在这里注册
    plugins_map = {
        # 子域名
        "lijiejie": {
            "classname": "LijiejieSubDomainBrute",
            "plugin_absolute_path": "/Users/dongguangli/cute/crontab/third_party/subDomainsBrute",
        },
        "sublist3r": {
            "classname": "Sublist3rSubDomainBrute",
            "plugin_absolute_path": "/Users/dongguangli/cute/crontab/third_party/Sublist3r",
        },
        "feei": {
            "classname": "FeeiSubDomainBrute",
            "plugin_absolute_path": "/Users/dongguangli/cute/crontab/third_party/ESD",
        },
        # 兄弟域名
        "icp": {
            "classname": "IcpBrotherDomain",
            "plugin_absolute_path": "",
        },
    }

# mail
smtp_server = "smtp.163.com"
from_addr = "hackingforfun@163.com"
password = "woshishouquanma1"
to_addr = "1157599735@qq.com,524131829@qq.com"
new_brotherdomain_title = "厂商%s有新的域名啦"

# 轮训DNS服务器，确保服务可用，以及返回的结果全球化
dns_server = {
    # 'google': '8.8.8.8',
    '114': '114.114.114.144',
    'opendns': '208.67.222.222',
    # 'baidudns': '180.76.76.76',
    # 'v2ex dns': '199.91.73.222',
    # 'dyn dns': '216.146.35.35',
    # 'comodo dns': '8.26.56.26',
    # 'Neustar dns': '156.154.70.1',
    # 'norton dns': '199.85.126.10',
    # 'One dns': '112.124.47.27',
    # 'opener dns': '42.120.21.30',
    # 'alidns': '223.5.5.5',
    # 'unioncom': '123.125.81.6',
    # 'chinamobile': '218.30.118.6',
    # '10086_Guangdong': '203.156.201.157',
    # '10086_Shanghai': '211.139.163.6',
    # '10086_Beijing': '211.136.28.228',
    # '10000_Guangdong': '202.96.128.86',
    # '10000_Shanghai': '202.96.199.132',
    # '10000_Beijing': '202.96.0.133',
    # '10010_Beijing': '202.102.227.68',
    # '10010_Guangdong': '210.21.4.130',
    # '10010_Shanghai': '211.95.1.97',
    'esd': '223.6.6.6'
}

# 默认爆破一个子域名的时间,超过此时间爆破插件进程被kill
default_subprocess_call_timeout = 1000
feei_subprocess_call_timeout = 4000   # feei插件

# [兄弟域名配置]
# 待扫描的厂商信息
domain_corpname_subcorpname = [
    ("baidu.com", "百度", "百度"),
    ("diditaxi.com", "滴滴", "滴滴"),
    ("didichuxing.com",	"滴滴", "快的"),
    ("alipay.com", "阿里", "支付宝")
]
