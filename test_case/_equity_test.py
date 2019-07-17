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



class Test_Equity_Test(unittest.TestCase):



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
        datenow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
        self.dataPool.set('transDate', datenow)  #


    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")

    def open_account(self):
        " 开户"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        name = 'cs' + datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S') + str(random.randint(000, 999))
        self.dataPool.set('accountName', name)
        self.dataPool.set('businessSrcToken', order_id)
        self.dataPool.set('organizationId', '8')
        self.dataPool.set('alarmPhone', '13255256541')
        self.dataPool.set('operatorId', '123456')
        response = self.equity_biz.open()
        self.assertEqual('000', response.result.code)
        self.dataPool.set('accountNo1', response.accountNo)
        return response

    def test_Equity_01(self):
        "充值：资产账号不存在   --失败"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '1000')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('accountNo', '111')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('organizationId', '1155')


        response = self.equity_biz.Recharge_Send()
        self.assertEqual('00116002', response.result.code)

    def test_Equity_02(self):
        "修改成禁用-》充值-》启用-》充值"
        self.open_account()
        '修改成禁用'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'CLOSED')  # 账户状态
        self.dataPool.set('accountNo',self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('overdraftAmount', '0')  # 透支金额

        response1=self.equity_biz.updateAccountOpen()
        self.assertEqual('000', response1.result.code)

        '充值'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '50')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        response = self.equity_biz.Recharge_Send()
        self.assertEqual('00115307', response.result.code)

        '修改成启用'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('accountState', 'OPENED')  # 账户状态

        response1 = self.equity_biz.updateAccountOpen()
        self.assertEqual('000', response1.result.code)

        '充值'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '50')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        response = self.equity_biz.Recharge_Send()
        self.assertEqual('000', response.result.code)

    def test_Equity_03(self):
        " 同一类型账户名重复开户"

        response = self.equity_biz.open()
        self.assertEqual('00115305', response.result.code)

    def test_Equity_04(self):
        " 修改权益账户"
        name = 'cs' + datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S') + str(random.randint(000, 999))
        self.dataPool.set('accountName', name)
        self.dataPool.set('accountNo', self.dataPool.get('accountNo'))
        self.dataPool.set('alarmPhone', '13251256541')
        self.dataPool.set('organizationId', '8')
        response_up = self.equity_biz.updateAccount()
        self.assertEqual('000', response_up.result.code)

    def test_Equity_05(self):
        " 修改权益账户名称重复"
        self.dataPool.set('accountName', '测试')
        response_up = self.equity_biz.updateAccount()
        self.assertEqual('00115305', response_up.result.code)

    def test_Equity_06(self):
        " 资产账户不存在冲正"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('accountNo', '11112')  #
        self.dataPool.set('correctOrderNo', '2018091710333462360')  #
        self.dataPool.set('correctAmount', "2")  #
        self.dataPool.set('originalConsumeTransNo', "6602015911123615752")
        response=self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response.result.code)

    def test_Equity_07(self):
        " 账号不存在充值"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '1')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('accountNo', '2233')  # 资产账户
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        response = self.equity_biz.Recharge_Send()
        self.assertEqual('00116002', response.result.code)

    def test_Equity_08(self):
        " 修改权益账户，账户不存在"
        self.dataPool.set('accountNo', '11223')
        response = self.equity_biz.updateAccount()
        self.assertEqual('00115306', response.result.code)

    def test_Equity_09(self):
        " 原流水不存在冲正"
        print 'accountNo',self.dataPool.get('accountNo')
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  #
        self.dataPool.set('correctOrderNo', '20180917103334623')  #
        self.dataPool.set('correctAmount', "2")  #
        self.dataPool.set('originalConsumeTransNo', "66020159111236157")
        response = self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response.result.code)

    def test_Equity_10(self):
        " 原流水和资产账号不一致"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  #
        self.dataPool.set('correctOrderNo', '6571703921750851584')  #
        self.dataPool.set('correctAmount', "2")  #
        self.dataPool.set('originalConsumeTransNo', "6571703921750859788")
        response = self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response.result.code)

    def test_Equity_11(self):
        " 消费大于余额"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '100')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")


        response=self.equity_biz.Consume_Send()
        # self.testcase.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))
        self.assertEqual('00115300', response.result.code)

    def test_Equity_12(self):
        " 消费小于余额->一次冲正小于订单金额->第二次等于订单金额"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '5')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        self.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))

        '冲正'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "2")  #
        self.dataPool.set('originalConsumeTransNo',response.consumeTransNo)

        self.equity_biz.Correct_Send()

        '二次冲正'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "3")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        self.equity_biz.Correct_Send()

    def test_Equity_13(self):
        " 消费小于0"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '-1')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('00116002', response.result.code)



    def test_Equity_14(self):
        " 等于余额-》冲正等于订单金额->已冲正为0的再次冲正"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '45')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        self.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))

        '冲正等于订单金额'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "45")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        self.equity_biz.Correct_Send()

        '已冲正为0的再次冲正'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "3")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        self.equity_biz.Correct_Send()

    def test_Equity_15(self):
        " 充值-》消费小于余额-》一次冲正小于订单金额-》再次冲正大于订单金额"
        '充值'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '50')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        response = self.equity_biz.Recharge_Send()
        self.assertEqual('000', response.result.code)

        '消费'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '10')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        self.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))

        '冲正小于订单金额'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "5")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        response1= self.equity_biz.Correct_Send()
        self.assertEqual('000', response1.result.code)

        '再次冲正大于余额'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "10")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        response3=self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response3.result.code)


    def test_Equity_16(self):
        " 消费小于余额-》一次冲正，大于订单金额"
        '消费'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '10')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        self.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))

        '冲正大于余额'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "20")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        response3 = self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response3.result.code)


    def test_Equity_17(self):
        " 消费小于余额-》修改成禁用-》冲正-》消费-》启用"
        '消费'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '10')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        self.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))

        '修改成禁用'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'CLOSED')  # 账户状态
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('overdraftAmount', '0')  # 透支金额

        response1 = self.equity_biz.updateAccountOpen()
        self.assertEqual('000', response1.result.code)

        '禁用下冲正'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "20")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        response3 = self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response3.result.code)

        '禁用下消费'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '10')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('00115307', response.result.code)

        '启用'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('overdraftAmount', '0')  # 透支金额

        response1 = self.equity_biz.updateAccountOpen()
        self.assertEqual('000', response1.result.code)

    def test_Equity_18(self):
        " 消费小于余额-》冲正金额等于0-》冲正金额为负"
        '消费'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '10')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        self.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))

        '冲正金额0'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "0")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        response3 = self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response3.result.code)

        '冲正金额小于0'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('correctOrderNo', self.dataPool.get('consumeOrderNo'))  #
        self.dataPool.set('correctAmount', "0")  #
        self.dataPool.set('originalConsumeTransNo', response.consumeTransNo)

        response3 = self.equity_biz.Correct_Send()
        self.assertEqual('00116002', response3.result.code)

    def test_Equity_19(self):
        " 非信用账户，全部消费"
        '消费'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '75')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "1")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        self.assertEqual(response.model.consumeAmount, long(self.dataPool.get('consumeAmount')))

    def test_Equity_20(self):
         "开户-》修改成透支的，不设置透支额度，默认为0-》修改成信用账户，设置透支额度-》消费大于透支额度"

         self.open_account()

         '修改成透支的，不设置透支额度，默认为0'
         order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(random.randint(00000, 99999))
         self.dataPool.set('isAllowNegtive', 'Y')  # 是否允许透支
         self.dataPool.set('accountState', 'OPENED')  # 账户状态
         self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
         self.dataPool.set('overdraftAmount', 'null')  # 透支金额

         response=self.equity_biz.updateAccountOpen()
         self.assertEqual('000', response.result.code)

         '修改成信用账户，设置透支额度'
         self.dataPool.set('overdraftAmount', '30')  # 透支金额

         response = self.equity_biz.updateAccountOpen()
         self.assertEqual('000', response.result.code)
         '消费大于透支额度'

         order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(random.randint(00000, 99999))
         self.dataPool.set('consumeAmount', '75')  # 订单金额
         self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
         self.dataPool.set('consumeOrderNo', order_id)  # 订单号
         self.dataPool.set('businessSrcToken', order_id)  #
         self.dataPool.set('isconsumeAll', "0")

         response = self.equity_biz.Consume_Send()
         self.assertEqual('00116002', response.result.code)

    def test_Equity_21(self):
        " 消费等于透支额度-》充值后为正-》修改成非信用账户"
        '消费等于透支额度'

        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '30')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)

        '充值后为正'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '50')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        response = self.equity_biz.Recharge_Send()
        self.assertEqual('000', response.result.code)
        '修改成非信用账户'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('overdraftAmount', '30')  # 透支金额

        response = self.equity_biz.updateAccountOpen()
        self.assertEqual('000', response.result.code)

    def test_Equity_22(self):
        " 修改成信用账户-》消费小于透支额度-》充值后为负-》修改成非信用账户-》充值-》修改成非信用账户"
        '修改成信用账户'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'Y')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('overdraftAmount', '30')  # 透支金额

        response = self.equity_biz.updateAccountOpen()
        self.assertEqual('000', response.result.code)
        '消费小于透支额度'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('consumeAmount', '40')  # 订单金额
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('consumeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #
        self.dataPool.set('isconsumeAll', "0")

        response = self.equity_biz.Consume_Send()
        self.assertEqual('000', response.result.code)
        '充值后为负'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '5')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        response = self.equity_biz.Recharge_Send()
        self.assertEqual('000', response.result.code)
        '修改成非信用账户'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('overdraftAmount', '30')  # 透支金额

        response = self.equity_biz.updateAccountOpen()
        self.assertEqual('00116002', response.result.code)
        '充值'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('rechargeAmount', '15')  # 订单数量
        self.dataPool.set('orderMoney', '10')  # 订单金额
        self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
        self.dataPool.set('businessSrcToken', order_id)  #

        response = self.equity_biz.Recharge_Send()
        self.assertEqual('000', response.result.code)
        '修改成非信用账户'
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', self.dataPool.get('accountNo1'))  # 资产账户
        self.dataPool.set('overdraftAmount', '30')  # 透支金额

        response = self.equity_biz.updateAccountOpen()
        self.assertEqual('000', response.result.code)

    def test_Equity_23(self):
        "非短信账户修改成信用账户"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(00000, 99999))
        self.dataPool.set('isAllowNegtive', 'Y')  # 是否允许透支
        self.dataPool.set('accountState', 'OPENED')  # 账户状态
        self.dataPool.set('accountNo', '6572439881560096776')  # 资产账户
        self.dataPool.set('overdraftAmount', '80')  # 透支金额
        self.dataPool.set('organizationId', '8')

        response = self.equity_biz.updateAccountOpen()
        self.assertEqual('00115306', response.result.code)



    # def test_Equity_44(self):
    #      " 接收手机号大于5个（没有限制）"
    #      order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
    #          random.randint(00000, 99999))
    #      name = 'cs'+datetime.datetime.strftime(datetime.datetime.now(), '%H%M%S') + str(random.randint(000, 999))
    #      self.dataPool.set('accountName', name)
    #      self.dataPool.set('businessSrcToken', order_id)
    #      self.dataPool.set('organizationId', '8')
    #      self.dataPool.set('alarmPhone', '13255256541,13522565222,16619552524,16619552525,16619552526,16619552527')
    #      response = self.equity_biz.open()
    #      self.assertEqual('00115305', response.result.code)


    # def test_Equity_03(self):
    #     "open正常账户充值-修改成禁用状态-充值-修改成启用状态"
    #     order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
    #         random.randint(00000, 99999))
    #     self.dataPool.set('rechargeAmount', '11')  # 订单数量
    #     self.dataPool.set('orderMoney', '10')  # 订单金额
    #     self.dataPool.set('accountNo', '6590225723384922120')  # 资产账户
    #     self.dataPool.set('rechargeOrderNo', order_id)  # 订单号
    #     self.dataPool.set('businessSrcToken', order_id)  #
    #
    #     response1 = self.equity_biz.Recharge_Send()
    #     self.assertEqual('000', response1.result.code)
    #
    #     self.dataPool.set('isAllowNegtive', 'N')  # 是否允许透支
    #     self.dataPool.set('accountState', 'CLOSED')  # 账户状态
    #     self.dataPool.set('overdraftAmount', '0')  # 透支金额
    #     self.dataPool.set('organizationId', '8')
    #     response2=self.equity_biz.updateAccountOpen()
    #     self.assertEqual('000', response2.result.code)
    #
    #     response3 = self.equity_biz.Recharge_Send()
    #     self.assertEqual('00115307', response3.result.code)
    #
    #     self.dataPool.set('accountState', 'OPENED')  # 账户状态
    #     response4 = self.equity_biz.updateAccountOpen()
    #     self.assertEqual('000', response4.result.code)








if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Equity_Test)
    stream = open("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
