# coding:utf-8
import logging
import os
import inspect
import time

'''
Logging Config
'''
file_path = inspect.stack()[0][1]
cwd = os.path.split(file_path)[0]
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s '
           '%(filename)s '
           '%(funcName)s '
           '[line:%(lineno)d] '
           '%(levelname)s '
           ':%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="%s/log/%s.log" % (cwd, time.strftime("%y-%m-%d")),
    filemode='a'
)

'''
ENVIRONMENT CONFIG：http服务域名
'''
ENVIRONMENT_CONFIG = {
    "dohko": {
        "mendian": "http://dohko.api.mendianbao.hualala.com",
        "waimai": "http://dohko.api.transformer.hualala.com",
        "order": "http://dohko.shopapi.hualala.com/",
        # "order": "http://dohko.es.order.http.hualala.com/",
        # "order": "http://192.168.4.49:8081/",
        # "order": "http://192.168.4.93:80/",
        "wechat-old": "https://dohko.m.hualala.com/",
        'shopcenter': 'http://dohko.shop.hualala.com/',
        'login': 'http://dohko.login.hualala.com:31251/'
    },
    "pro": {
        "mendian": "http://api.mendianbao.hualala.com",
        "waimai": "http://api.transformer.hualala.com",
        "order": "http://shopapi.hualala.com/",
        "wechat-old": "https://m.hualala.com/",
    },
    "pro-ip": {
        "mendian": "http://api.mendianbao.hualala.com",
        "waimai": "http://api.transformer.hualala.com",
        "order": "http://shopapi.hualala.com/",
        # "order": "http://m.hualala.com/",
        "wechat-old": "https://m.hualala.com/",
    },

    # "dohko": "http://dohko.login.hualala.com:31251",
    "pre": {
        "mendian": "http://pre.api.mendianbao.hualala.com",
        "waimai": "http://pre.api.transformer.hualala.com"
    },
    "silu": "http://192.168.5.148:8092"
}

"""
ENVIRONMENT_GRPC_CONFIG：grpc服务域名
"""
ENVIRONMENT_GRPC_CONFIG = {
    "dohko": {
        "order": "dohko.order.service.hualala.com:31515",
        # "order": "etcd://172.16.3.204:8081/dohko/order-service",
        # "order": "localhost:6565",
        "order-mock": "172.16.32.141:6565",
        "pos": "dohko.pos.service.hualala.com:31530",
        "equity": "equity.core.service.hualala.com:31731",
        "dzfp": "dohko.service.tax.hualala.com:31517",
        # "sms": "dohko.message.sender.hualala.com:31722",
        # "sms":"https://etcd.dohko.xh.hualala.com:5443/api/v1/watch/namespaces/dohko/endpoints/message-channel-service",
        "sms":"etcd://dohko.xh.hualala.com:5443/api/v1/watch/namespaces/dohko/endpoints/message-channel-service",
        # 查询短信签名用的域名message-channel-service
        "smschannel":"dohko.message.channel.hualala.com:31781",
        "adapi":"dohko.advert.service.hualala.com:31826",
        "equity2":"dohko.equity.account2.hualala.com:31814",
        "smsdata":"dohko.data.statistical.query.hualala.com:31799",
        "semsms":"dohko.service.short.message.hualala.com:31524",
        "bop":"dohko.grpc.businessOperation.hualala.com:31806",
        "pay": "dohko.grpc.hualala.com:31827",
        "advert": "dohko.advert.service.hualala.com:31826",
        "host":"http://dohko.shop.hualala.com"


    },
    "pro": {
        "order": "",
        "pos": "pos.service.hualaladohko.equity.account2.hualala.com:31814.com:7084"
    },
    "pre": {
        "order": "",
        "pos": "pre.pos.service.hualala.com:31562",
        "sms": "pre.message.sender.hualala.com:31722",
        "dzfp": "pre.service.tax.hualala.com:31517",
        "equity": "pre.equity.core.service.hualala.com:31731"
    },
    "mu": {
        "order": "",
        "pos": "mu-pos-service.hualala.com:32283"
    },
    "local": {
        "order": "127.0.0.1:31515",
        "pos": "dohko.pos.service.hualala.com:31530"
    }
}

CASE_REFERENCE = {
    "testlink": "testlink.hualala.com",
    "excel": "excel"
}

EMAIL_CONFIG = {

}

TESTLINK_CONFIG = {
    "url": "http://testlink.hualala.com/testlink/lib/api/xmlrpc/v1/xmlrpc.php",
    "key": "00276ea6fb5bda36590156fe752013b5"
}

REQUEST_HEADER = {
    'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger Wechat/6.5.23 NetType/WIFI Language/zh_CN'
    # 'Cookie': 'access_token=dce1443d-706e-44a1-b2cb-1eff77314695; COOKIES_SESSION_ID=A0BECB1403F4A4D7E51EF1054B0D6EFF; JSESSIONID=1E5C576159B695005927842F279CBD96; gpsd=8896864ec77e67a28f396ab574ea322a'
}

MYSQL_CONFIG = {
    "dohko": {"host": "172.16.3.201",
              "user": "root",
              "passwd": "gozapdev",
              "port": 3400,
              "db": "db_mendian",
              'charset': 'utf8'},
    "pro": {},
}

BIZ_CONFIF = {"shop", "bargain", "internal", "marketing", "supply_chain"}
