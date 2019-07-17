# -*- coding: UTF-8 -*-
import json
import logging
import sys
import unittest
from ddt import ddt, data
from model.data_pool import DataPool
import datetime
import random

import time


reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("../../")

from common.integretion import HTMLTestRunner
from common.service.excel_util import ExcelUtil
from common.common import Common
from common.service import excel_case_facade_rpc
from common.service import http_util


excel = ExcelUtil('../data/input/test_sms_data.xlsx')


@ddt
class Test_Sms_Template(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global caseNum
        caseNum = 0
        cls.sheet_index = 0
        cls.dataPool = DataPool()
        cls.com = Common(dataPool=cls.dataPool)
        cls.excel_facade = excel_case_facade_rpc.GetExcelCaseData()
        cls.http_util=http_util.HttpUtil()


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """
        获取本类的类名，用来找到数据池里的数据文件
        :return:
        """
        self.com.setTestCase(self)

        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        name = 'cs' + datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S') + str(random.randint(000, 999))
        name1 = 'cs' + datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S') + str(random.randint(000, 999))
        self.dataPool.set('accountName', name)
        self.dataPool.set('businessSrcToken', order_id)
        self.dataPool.set('rechargeOrderNo', order_id)
        self.dataPool.set('consumeOrderNo', order_id)
        self.dataPool.set('correctOrderNo', order_id)
        self.dataPool.set('organizationId', '8')
        datenow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
        datenownew = datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S')
        refunddatenow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        self.dataPool.set('operatorId', '123456')
        #权益2.0
        self.dataPool.set('requestTime', datenow)
        self.dataPool.set('refundrequestTime', refunddatenow)
        self.dataPool.set('rechargeNo', order_id)
        self.dataPool.set('orderNo', order_id)
        self.dataPool.set('refundOrderNo', order_id)
        self.dataPool.set('withdrawOrder', order_id)
        self.dataPool.set('transferOrderNo', order_id)
        #self.dataPool.set('correctOrderNo', order_id)
        #权益1.0
        self.dataPool.set('transTime', datenownew)
        self.dataPool.set('transDate', datenow)
        #查询充值列表的起止时间
        self.dataPool.set('beginTransDate', datenow)
        self.dataPool.set('endTransDate', datenow)

        datenow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')

        rad=datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S') + str(random.randint(000, 999))
        self.dataPool.set('datetime', time.strftime("%Y%m%d%H%M%S", time.localtime()))

        self.dataPool.set('date', datenow)
        self.dataPool.set('random', rad)
        self.dataPool.set('tax_order', self.com.generate_random_str(32))
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('order_id', order_id)




    def tearDown(self):
        # self.dataPool.set('order_id1', self.dataPool.get(order_id))
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")


    @data(*excel.next())
    def test_Sms(self,data):
        print data
        print data['TestScene']
        '获取excel中的值'
        service = data['service']
        # ServiceName = data['ServiceName'].split('/')
        # expect = eval(data['Expect'])
        input = data['Input'].decode('utf-8').replace("'", "\"")
        typeName = data['type']

        if '$' in input:
            '先匹配替换变量'
            input = eval(self.com.matches(input))
        else:
            input = json.loads(input,encoding="utf-8")
        # print(input)

        self.dataPool = DataPool(**input)
        #
        # datalist=[service,ServiceName[0],ServiceName[1],ServiceName[2],ServiceName[3],input]
        # response=self.excel_facade.get_case_data1(*datalist)
        # print 'response:',response

        '断言期望值'
        expect = eval(data['Expect'])
        # self.com.assertExp(expect, response)
        #
        # '将返回的以后用到的set到dataPool'
        # if data['Extract Field'] is not None and len(data['Extract Field']) > 0:
        #     extract_Field = eval(data['Extract Field'])
        #     self.com.setEf(extract_Field, response)

        self.dataPool = DataPool(**input)
        if("grpc"==typeName):
            ServiceName = data['ServiceName'].split('/')
            datalist=[service,ServiceName[0],ServiceName[1],ServiceName[2],ServiceName[3],input]
            response=self.excel_facade.get_case_data1(*datalist)
            print 'response:', response
            "断言期望值"
            self.com.assertExp(expect, response)
            '将返回的以后用到的set到dataPool'
            if data['Extract Field'] is not None and len(data['Extract Field']) > 0:
                extract_Field = eval(data['Extract Field'])
                self.com.setEf(extract_Field, response)
        elif("post"==typeName):
            ServiceName = data['Path']
            response=self.http_util.http_post(service,ServiceName,input)
            print 'response:', response
            "断言期望值"
            self.com.assertExp_json(expect, response)
            '将返回的以后用到的set到dataPool'
            if data['Extract Field'] is not None and len(data['Extract Field']) > 0:
                extract_Field = eval(data['Extract Field'])
                self.com.setEf_json(extract_Field, response)




if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Sms_Template)
    stream = open("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
