# -*- coding: UTF-8 -*-
import json
import logging
import sys
import unittest
import datetime
import random
from model.data_pool import DataPool

# reload(sys)
# sys.setdefaultencoding('utf-8')

sys.path.append("../../")

from common.integretion import HTMLTestRunner
from biz.test_equity_biz import TestEquityBiz



class Test_Equity_Op_Service(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        global caseNum
        caseNum = 0
        cls.sheet_index = 0

        cls.dataPool = DataPool()

        cls.equity_biz = TestEquityBiz(dataPool=cls.dataPool)


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """
        获取本类的类名，用来找到数据池里的数据文件
        :return:
        """

        __file_name = 'test_euqity_grpc',
        self.file_name = "../data/%s.xlsx" % __file_name
        global caseNum
        caseNum += 1
        logging.info("-------------CASE" + str(caseNum) + " START---------------------")

        self.equity_biz.setTestCase(self)


    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")


    def test_Equity_01(self):
        "修改：资产账号不存在   --失败"
        self.dataPool.set('isAllowNegtive', 'Y')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', '6574692226')  # 资产账户
        self.dataPool.set('overdraftAmount', '11')  # 透支金额

        def assertCallbackFunc(testcase=self, response={}):
            print("response:", response.result.message)
            testcase.assertEqual('00115306', response.result.code)
        self.equity_biz.updateAccountOpen(assertCallbackFunc=assertCallbackFunc)
    
    def test_Equity_02(self):
        "原来是非透支的 修改成透支的，设置透支额度"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'Y')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', '6611356404135493640')  # 资产账户
        self.dataPool.set('overdraftAmount', '80')  # 透支金额

        def assertCallbackFunc(testcase=self, response={}):
            print("response:",response)
            print("response:", response.result.message)
        self.equity_biz.updateAccountOpen(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_03(self):
        "原来是非透支的 修改成透支的，不设置透支额度 --默认设置0"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'Y')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', '6601019852373098504')  # 资产账户
        self.dataPool.set('overdraftAmount', 'null')  # 透支金额
        self.dataPool.set('organizationId', '8')

        def assertCallbackFunc(testcase=self, response={}):
            print("response:",response)
            print("response:", response.result.message)
        self.equity_biz.updateAccountOpen(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_04(self):
        "修改成禁用状态"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'CLOSED')  # 账户状态
        self.dataPool.set('accountNo', '6590225723384922120')  # 资产账户
        self.dataPool.set('overdraftAmount', '10')  # 透支金额

        def assertCallbackFunc(testcase=self, response={}):
            print("response:",response)
            print("response:", response.result.message)
        self.equity_biz.updateAccountOpen(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_05(self):
        "修改成启用状态"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', '6590225723384922120')  # 资产账户
        self.dataPool.set('overdraftAmount', '0')  # 透支金额

        def assertCallbackFunc(testcase=self, response={}):
            print("response:", response)
            print("response:", response.result.message)

        self.equity_biz.updateAccountOpen(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_06(self):
        "原来是透支的 不欠钱，修改成非透支的"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', '6601019852373098504')  # 资产账户
        self.dataPool.set('overdraftAmount', '-1')  # 透支金额
        self.dataPool.set('organizationId', '8')

        def assertCallbackFunc(testcase=self, response={}):
            print ("response:",response)
            print("response:", response.result.message)
        self.equity_biz.updateAccountOpen(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_07(self):
        "非短信的不能修改成信用账户"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', '6572439963164475400')  # 资产账户
        self.dataPool.set('overdraftAmount', 'null')  # 透支金额

        def assertCallbackFunc(testcase=self, response={}):
            print("response:", response.result.message)
            testcase.assertEqual('00115306', response.result.code)
        self.equity_biz.updateAccountOpen(assertCallbackFunc=assertCallbackFunc)


if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Equity_Op_Service)
    stream = open("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
