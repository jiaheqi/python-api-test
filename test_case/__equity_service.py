# -*- coding: UTF-8 -*-
import json
import logging
import sys
import unittest
import datetime
import random
from model.data_pool import DataPool


reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("../../")

from common.integretion import HTMLTestRunner
from biz.test_equity_biz import TestEquityBiz



class Test_Equity_Service(unittest.TestCase):

    datenow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')

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
        self.dataPool.set('transDate', self.datenow)  #


    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")


    def test_Equity_01(self):
        "充值：资产账号不存在   --失败"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '11')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('accountNo', '6574692226')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        def assertCallbackFunc(testcase=self, response={}):
            print "response:", response.result.message
            testcase.assertEqual('00116002', response.result.code)
        self.equity_biz.Recharge_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_02(self):
        " 正常账户充值"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '0')  # 订单数量
        self.dataPool.set('orderMoney', '70')  # 订单金额
        self.dataPool.set('accountNo', '6571945217308536836')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        def assertCallbackFunc(testcase=self, response={}):
            pass
        self.equity_biz.Recharge_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_03(self):
        " 信用账户为负，充值后为负"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '11')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('accountNo', '6590225723384922120')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        def assertCallbackFunc(testcase=self, response={}):
            pass
        self.equity_biz.Recharge_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_04(self):
        " 信用账户为负，充值后为正"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '40')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('accountNo', '6571945273143935892')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        def assertCallbackFunc(testcase=self, response={}):
            pass
        self.equity_biz.Recharge_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_05(self):
        " 信用账户为正，充值后为正"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '11')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('accountNo', '6598306214726074376')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        def assertCallbackFunc(testcase=self, response={}):
            pass
        self.equity_biz.Recharge_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_06(self):
        " 余额不足，消费，失败"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '100')  # 订单金额
        self.dataPool.set('accountNo', '6571945217308536836')  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        def assertCallbackFunc(testcase=self, response={}):
            print "response:", response.result.message
            testcase.assertEqual('00115300', response.result.code)
        self.equity_biz.Consume_Send(assertCallbackFunc=assertCallbackFunc)


    def test_Equity_07(self):
        " 消费金额小于等于余额，消费，成功"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '100')  # 订单金额
        self.dataPool.set('accountNo', '6601019852373098504')  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        def assertCallbackFunc(testcase=self, response={}):
            pass
            # print "response:", response.result.message
            # testcase.assertEqual('000', response.result.code)
        self.equity_biz.Consume_Send(assertCallbackFunc=assertCallbackFunc)
    def test_Equity_08(self):
        " 信用账户不考虑全部消费，消费，成功"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '2')  # 订单金额
        self.dataPool.set('accountNo', '6598306214726074376')  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        def assertCallbackFunc(testcase=self, response={}):
            pass
        self.equity_biz.Consume_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_09(self):
        " 非信用账户可以全部消费，成功"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '0')  # 订单金额
        self.dataPool.set('accountNo', '6571945217308536836')  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "1")

        def assertCallbackFunc(testcase=self, response={}):
            pass
        self.equity_biz.Consume_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_10(self):
        "信用账户 消费小于等于透支金额,成功"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '2')  # 订单金额
        self.dataPool.set('accountNo', '6571945273143935892')  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "1")

        def assertCallbackFunc(testcase=self, response={}):
            print "response:", response.result.message
            testcase.assertEqual('000', response.result.code)
        self.equity_biz.Consume_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_11(self):
        " 信用账户 消费大于透支金额,失败"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '11')  # 订单金额
        self.dataPool.set('accountNo', '6598306214726074376')  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "1")

        def assertCallbackFunc(testcase=self, response={}):
            print "response:", response.result.message
            testcase.assertEqual('000', response.result.code)
        self.equity_biz.Consume_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_12(self):
        " 信用账户可以冲正"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('accountNo', '6589084232746795016')  #
        self.dataPool.set('correctOrderNo', '2018101710243670399')  #
        self.dataPool.set('correctAmount', "0")  #
        self.dataPool.set('originalConsumeTransNo', "6613146168547344392")
        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.equity_biz.Correct_Send()

    def test_Equity_13(self):
        " 非信用账户可以冲正"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('accountNo', '6594612375347802120')  #
        self.dataPool.set('correctOrderNo', '6594612375347795250')  #
        self.dataPool.set('correctAmount', "1")  #
        self.dataPool.set('originalConsumeTransNo', "6594612375347802120")
        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.equity_biz.Correct_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_14(self):
        " 关闭状态不可以充值"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '11')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('accountNo', '6571944568768524308')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        def assertCallbackFunc(testcase=self, response={}):
            print "response:", response.result.message
            testcase.assertEqual('00115307', response.result.code)
        self.equity_biz.Recharge_Send(assertCallbackFunc=assertCallbackFunc)


    def test_Equity_15(self):
        " 关闭状态不可以消费"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '9')  # 订单金额
        self.dataPool.set('accountNo', '6571944568768524308')  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        def assertCallbackFunc(testcase=self, response={}):
            print "response:", response.result.message
            testcase.assertEqual('00115307', response.result.code)

        self.equity_biz.Consume_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_16(self):
        " 关闭状态可以冲正"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('accountNo', '6571945273143935892')  #
        self.dataPool.set('correctOrderNo',order_id)  #
        self.dataPool.set('correctAmount', "0")  #
        self.dataPool.set('originalConsumeTransNo', "6600908402266735508")

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.equity_biz.Correct_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_17(self):
        " 关闭状态可以退款"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('recfundOrderNo', '2018091410492550542')  #
        self.dataPool.set('accountNo', '6571944568768524308')  #
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('oldRechargeTransNo', "6600906778769096724")

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.equity_biz.Refund_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_18(self):
        " 信用账户可以退款"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('recfundOrderNo', '2018091818050760223')  #
        self.dataPool.set('accountNo', '6571944568768524308')  #
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('oldRechargeTransNo', "6602503368436875284")

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.equity_biz.Refund_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Equity_19(self):
        " 查询接口"
        self.dataPool.set('organizationIds', '119')  #
        self.dataPool.set('equityType', 'SMS')  #

        self.dataPool.set('accountNo', '6579901781646508151')  #
        self.dataPool.set('accountState', "OPENED")
        self.dataPool.set('balanceBefore', '-10')  #
        self.dataPool.set('balanceEnd', '1000')  #
        self.dataPool.set('balanceEnum', '3')  #
        self.dataPool.set('orderby', "desc")

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.equity_biz.queryParamAccountPageInfo(assertCallbackFunc=assertCallbackFunc)

if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Equity_Service)
    stream = file("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
