# coding:utf-8

import unittest
from model.data_pool import DataPool
import re
import json
import random
import string

class Common():
    def __init__(self,dataPool=DataPool):
        self.dataPool = dataPool
        self.testcase = unittest.TestCase

    "按层级获取返回结果-对象"
    def _get_target_value(self,key,object):
        # print 'type类型',type(object)
        # print (object)
        keys=[key]

        if '.'in key:
            keys=key.split('.')
        else:
            if not hasattr(object, key) :  # 对传入数据进行格式校验
                return '不存在这个属性或者格式错误'
        for i in range(len(keys)):
            if hasattr(object, keys[i]) :
                if (i+1)==len(keys) :
                    val=(getattr(object,keys[i]).encode('UTF-8'))
                else:
                    object =eval('object.'+keys[i])
            else:
                return '不存在这个属性 '
        return val

    def assertExp(self,expect,response):

            dic_key = []
            dic_val = []
            for key, values in expect.items():
                if (response is not None):
                    dic_key.append(self._get_target_value(key, response))
                else:
                    dic_key.append('接口返回值为空')
                dic_val.append(self.matches(values))

            self.testcase.assertEqual(dic_val,dic_key)




    def setEf(self,extract_Field,response):
        if(extract_Field is not None and response is not None):
            for key,values in extract_Field.items():
                # print key,values
                val=self._get_target_value(values,response)
                self.dataPool.set(key,val)
        else:
            return "返回值或者关联值为空"

    def setTestCase(self, testCase):
        self.testcase = testCase

    def matches(self,value):
        matches = re.findall('\$\{(.*?)\}', value)
        mset = set(matches)
        for item in mset:
            itemVal = str(self.dataPool.get(item)).encode('UTF-8')
            # print item,':',itemVal
            value = value.replace("${%s}" % item, itemVal)
            if itemVal == '':
                print ('变量{}没有设置值'.format(item))
        return value

    "按层级获取返回结果-json"
    def _get_target_dic(self,key,object):
        keys = [key]
        object=json.loads(object)
        if '.' in key:
            keys = key.split('.')
        else:
            if not isinstance(object, dict):  # 对传入数据进行格式校验
                return 'argv[1] not an dict or argv[-1] not an list '
        # if key
        # print keys
        for i in range(len(keys)):
            object=object[keys[i]]
        return object

    def assertExp_json(self,expect,response):

            dic_key = []
            dic_val = []
            for key, values in expect.items():
                if (response is not None):
                    dic_key.append(self._get_target_dic(key, response))
                else:
                    dic_key.append('接口返回值为空')
                dic_val.append(self.matches(values))

            self.testcase.assertEqual(dic_val,dic_key)

    def setEf_json(self,extract_Field,response):
        if(extract_Field is not None and response is not None):
            for key,values in extract_Field.items():
                # print key,values
                val=self._get_target_dic(values,response)
                self.dataPool.set(key,val)
        else:
            return "返回值或者关联值为空"

    def generate_random_str(self,randomlength=16):
        """
        生成一个指定长度的随机字符串，其中
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str



