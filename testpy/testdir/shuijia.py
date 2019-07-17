# -*- coding: utf-8 -*-

import chardet
__author__ = 'wy'
US_VS_CN = 6.77

str_value = input("请输入带单位的水质信息: ")
# dw_str_value = str_value[-2:]
dw_str_value = str_value[-2:]
if dw_str_value == 'cn':
    sz_str_value =str_value[:-2]
    cn_value = eval('sz_str_value')
    us_value = cn_value / US_VS_CN
    print("请输入对应的水价信息:",us_value)
elif dw_str_value == 'us':
    sz_str_value = str_value[:-2]
    us_value = eval('sz_str_value')
    cn_value = us_value * US_VS_CN
    print("请输入相应的水价信息：",cn_value)
else:
    print("目前不支持该种货币！")