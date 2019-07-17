# -*- coding: UTF-8 -*-

import logging
# import sys
import unittest
from ddt import ddt, data,unpack
import datetime
import random
from model.data_pool import DataPool



# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# sys.path.append("../../")

from common.integretion import HTMLTestRunner
from common.service.excel_util import ExcelUtil
from common.common import Common

from biz.test_equity_biz import TestEquityBiz

excel = ExcelUtil('../data/testdata/test_equity_data.xlsx',)

@ddt
class Test_Equity_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global caseNum
        caseNum = 0
        cls.sheet_index = 0

        cls.dataPool = DataPool()
        cls.equity_biz = TestEquityBiz(dataPool=cls.dataPool)
        cls.com = Common(dataPool=cls.dataPool)




    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """
        获取本类的类名，用来找到数据池里的数据文件
        :return:
        """

        self.com.setTestCase(self)
        self.equity_biz.setTestCase(self)

        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        name = 'cs' + datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S') + str(random.randint(000, 999))
        self.dataPool.set('accountName', name)
        self.dataPool.set('businessSrcToken', order_id)
        self.dataPool.set('rechargeOrderNo', order_id)
        self.dataPool.set('organizationId', '8')
        datenow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
        self.dataPool.set('transDate', datenow)
        self.dataPool.set('operatorId', '123456')






    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")



    @data(*excel.next())
    def test_Sms(self,data):


        print data['TestScene']
        '获取excel中的值'
        service = data['service']
        subName=data['MethodName']
        input=data['Input']
        expect=eval(data['Expect'])
        '先匹配替换变量'
        input1=eval(self.com.matches(input))
        self.dataPool = DataPool(**input1)

        '判断调用哪个方法'
        if(subName=='recharge'):
            response = self.equity_biz.Recharge_Send()
        elif(subName=='consume'):
            response = self.equity_biz.Consume_Send()
        elif (subName == 'correct'):
            response = self.equity_biz.Correct_Send()
        elif (subName == 'updateAccountOpen'):
            response = self.equity_biz.updateAccountOpen()
        elif (subName == 'open'):
            response = self.equity_biz.open()
        elif (subName == 'updateAccount'):
            response = self.equity_biz.updateAccount()

        '断言期望值'
        self.com.assertExp(expect,response)

        '将返回的以后用到的set到dataPool'
        if data['Extract Field'] is not None and len(data['Extract Field'])>0 :
            extract_Field = eval(data['Extract Field'])
            self.com.setEf(extract_Field,response)







if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Equity_Test)
    stream = open("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
