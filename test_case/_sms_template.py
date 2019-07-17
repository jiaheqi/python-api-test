# -*- coding: UTF-8 -*-
import json
import logging
import sys
import unittest
from model.data_pool import DataPool

import time



reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("../../")


from common.integretion import HTMLTestRunner


from biz.test_sms_biz import TestSmsBiz



class Test_Sms_Template(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        global caseNum
        caseNum = 0
        cls.sheet_index = 0

        cls.dataPool=DataPool()
        cls.sms_biz = TestSmsBiz(dataPool=cls.dataPool)


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """
        获取本类的类名，用来找到数据池里的数据文件
        :return:
        """

        __file_name = 'test_sms_grpc',
        self.file_name = "../data/%s.xlsx" % __file_name
        global caseNum
        caseNum += 1
        logging.info("-------------CASE" + str(caseNum) + " START---------------------")

        self.sms_biz.setTestCase(self)
        self.dataPool.set('groupID', '8')  # 集团编码
        self.dataPool.set('toMobile', '16619756865')  # 手机号
        self.dataPool.set('serviceCode', 'CRM-Card')  # 业务编码
        self.dataPool.set('serviceSubCode', 'openCard')  # 业务子码
        self.dataPool.set('cardLevel', 'VIP6')  # 卡等级
        self.dataPool.set('shopName', '小木偶')  # 店铺名称
        self.dataPool.set('cardNO', 'gao1234')  # 卡号
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '5')  # 调账/转账赠送卡值
        self.dataPool.set('pointAmount', '10')  # 积分余额
        self.dataPool.set('modifyMoneyAmount', '100')  # 现金卡值
        self.dataPool.set('deductPoint', '5')  # 扣减积分
        self.dataPool.set('givePoint', '10')  # 赠送积分
        self.dataPool.set('giveMoneyAmount', '7')  # 赠送卡值
        self.dataPool.set('canUseMoneyBalance', '1000')  # 可用余额
        self.dataPool.set('modifyPointAmount', '12')  # 调账/转账积分
        self.dataPool.set('lockMoneyAmount', '30')  # 冻结金额
        self.dataPool.set('returnMoneyPreStage', '10')  # 每次返还金额
        self.dataPool.set('moneyBalance', '200')  # 卡值余额
        self.dataPool.set('shopID', '76069628')  # 店铺ID
        self.dataPool.set('cardTypeID', '6589815257655414792')  # 卡类型


    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")


    def test_Sms_01(self):
        "开卡"

        self.dataPool=DataPool(**{'shopName':'lalall','toMobile': '16519756865'})
        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg="【哗啦啦】欢迎加入"+self.dataPool.get('shopName')+"会员，您的会员卡号为"+self.dataPool.get('cardNO')+"，等级为"+self.dataPool.get('cardLevel')
            print  ('expMsg:',expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)


    def test_Sms_02(self):
        "消费（消费卡值不为0，消费积分不为0，返积分不为0）"

        self.dataPool.set('serviceCode', 'CRM-Pay')  # 业务编码
        self.dataPool.set('serviceSubCode', 'consume')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 消费卡值
        self.dataPool.set('deductPoint', '100')  # 扣减积分
        self.dataPool.set('creditPay', '0.8')  # 挂账金额
        self.dataPool.set('givePoint', '10')  # 赠送积分


        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print "messageContent':", messageContent
            expMsg = "【哗啦啦】您的会员卡"+self.dataPool.get('cardNO')+"在"+self.dataPool.get('shopName')+"，消费卡值"+self.dataPool.get('saveMoneyAmount')+"，挂账金额"+self.dataPool.get('creditPay')+\
                     "，消费扣积分"+self.dataPool.get('deductPoint')+"，消费返积分"+self.dataPool.get('givePoint')+"，剩余卡值"+self.dataPool.get('moneyBalance')+"，积分余额"+self.dataPool.get('pointAmount')+\
                     "，等级为"+self.dataPool.get('cardLevel')
            print'expMsg:', expMsg
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Consume_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_03(self):
        "消费（消费卡值为0，消费积分不为0，返积分不为0）"

        self.dataPool.set('serviceCode', 'CRM-Pay')  # 业务编码
        self.dataPool.set('serviceSubCode', 'consume')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '0')  # 消费卡值
        self.dataPool.set('deductPoint', '100')  # 扣减积分
        self.dataPool.set('creditPay', '0')  # 挂账金额
        self.dataPool.set('givePoint', '10')  # 赠送积分


        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + \
                     "，消费扣积分" + self.dataPool.get('deductPoint') + "，消费返积分" + self.dataPool.get('givePoint') + \
                     "，剩余卡值" + self.dataPool.get('moneyBalance') + "，积分余额" + self.dataPool.get( 'pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Consume_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_04(self):
        "消费（消费卡值为0，消费积分不为0，返积分为0）"

        self.dataPool.set('serviceCode', 'CRM-Pay')  # 业务编码
        self.dataPool.set('serviceSubCode', 'consume')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '0')  # 消费卡值
        self.dataPool.set('deductPoint', '100')  # 扣减积分
        self.dataPool.set('creditPay', '0')  # 挂账金额
        self.dataPool.set('givePoint', '0')  # 赠送积分
        # self.dataPool.set('cardTypeID', '6589815257655414791')  # 卡类型

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print "messageContent':", messageContent
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get( 'shopName') + "，消费扣积分" + self.dataPool.get('deductPoint') + \
                     "，剩余卡值" + self.dataPool.get('moneyBalance') + "，积分余额" + self.dataPool.get('pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print 'expMsg:', expMsg
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Consume_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_05(self):
        "消费（消费卡值不为0，消费积分为0，返积分为0）"

        self.dataPool.set('serviceCode', 'CRM-Pay')  # 业务编码
        self.dataPool.set('serviceSubCode', 'consume')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '10')  # 消费卡值
        self.dataPool.set('deductPoint', '0')  # 扣减积分
        self.dataPool.set('creditPay', '0')  # 挂账金额
        self.dataPool.set('givePoint', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') +  "，消费卡值" + self.dataPool.get('saveMoneyAmount') +  \
                     "，剩余卡值" + self.dataPool.get('moneyBalance') + "，积分余额" + self.dataPool.get('pointAmount') + \
                     "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)

        self.sms_biz.Consume_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_06(self):
        "消费（消费卡值不为0，消费积分为0，返积分不为0）"
        

        self.dataPool.set('serviceCode', 'CRM-Pay')  # 业务编码
        self.dataPool.set('serviceSubCode', 'consume')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 消费卡值
        self.dataPool.set('deductPoint', '0')  # 扣减积分
        self.dataPool.set('creditPay', '0.8')  # 挂账金额
        self.dataPool.set('givePoint', '10')  # 赠送积分
        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + \
                     "，消费卡值" + self.dataPool.get('saveMoneyAmount') + "，挂账金额" + self.dataPool.get('creditPay') + "，消费返积分" + self.dataPool.get( 'givePoint') + \
                     "，剩余卡值" + self.dataPool.get('moneyBalance') + "，积分余额" + self.dataPool.get('pointAmount') + \
                     "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Consume_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_07(self):
        "消费（消费卡值不为0，消费积分不为0，返积分为0）"
         

        self.dataPool.set('serviceCode', 'CRM-Pay')  # 业务编码
        self.dataPool.set('serviceSubCode', 'consume')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 消费卡值
        self.dataPool.set('deductPoint', '100')  # 扣减积分
        self.dataPool.set('creditPay', '0.8')  # 挂账金额
        self.dataPool.set('givePoint', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get( 'shopName') + \
                     "，消费卡值" + self.dataPool.get('saveMoneyAmount') + "，挂账金额" + self.dataPool.get( 'creditPay') + \
                     "，消费扣积分" + self.dataPool.get('deductPoint') + "，剩余卡值" + self.dataPool.get('moneyBalance') + \
                     "，积分余额" + self.dataPool.get( 'pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Consume_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_08(self):
        "消费撤销"

        self.dataPool.set('serviceCode', 'CRM-Pay')  # 业务编码
        self.dataPool.set('serviceSubCode', 'correct')  # 业务子码
        self.dataPool.set('moneyBalance', '200')  # 卡值余额
        self.dataPool.set('pointAmount', '10')  # 积分余额

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡在"+ self.dataPool.get( 'shopName') +"撤销了一笔交易，当前剩余卡值"+ self.dataPool.get( 'moneyBalance') +"，积分余额"+self.dataPool.get('pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_09(self):
        "储值（储值和返现，返积分不为0）"

        self.dataPool.set('serviceCode', 'CRM-Stored')  # 业务编码
        self.dataPool.set('serviceSubCode', 'buySaveMoneySet')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '7')  # 赠送卡值
        self.dataPool.set('moneyBalance', '200')  # 卡值余额
        self.dataPool.set('givePoint', '10')  # 赠送积分
        self.dataPool.set('pointAmount', '100')  # 积分余额

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在"+ self.dataPool.get( 'shopName') +"，储值"+ self.dataPool.get( 'saveMoneyAmount') +\
                     "，返现"+ self.dataPool.get( 'giveMoneyAmount') +"，返积分"+ self.dataPool.get( 'givePoint') +"，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +\
                     "，积分余额"+ self.dataPool.get( 'pointAmount') +"，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_10(self):
        "储值/套餐储值(返现不为0，返积分为0不显示)"

        self.dataPool.set('serviceCode', 'CRM-Stored')  # 业务编码
        self.dataPool.set('serviceSubCode', 'buySaveMoneySet')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '5')  # 赠送卡值
        self.dataPool.set('moneyBalance', '200')  # 卡值余额
        self.dataPool.set('givePoint', '0')  # 赠送积分
        self.dataPool.set('pointAmount', '100')  # 积分余额

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + "，储值" + self.dataPool.get('saveMoneyAmount') + \
                     "，返现" + self.dataPool.get('giveMoneyAmount') +"，当前卡值余额" + self.dataPool.get('moneyBalance') + \
                     "，积分余额" + self.dataPool.get('pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_11(self):
        "储值/套餐储值(返现为0，返积分不为0)"

        self.dataPool.set('serviceCode', 'CRM-Stored')  # 业务编码
        self.dataPool.set('serviceSubCode', 'buySaveMoneySet')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('moneyBalance', '200')  # 卡值余额
        self.dataPool.set('givePoint', '5')  # 赠送积分
        self.dataPool.set('pointAmount', '100')  # 积分余额

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + "，储值" + self.dataPool.get('saveMoneyAmount') + \
                     "，返积分" + self.dataPool.get( 'givePoint') + "，当前卡值余额" + self.dataPool.get('moneyBalance') + \
                     "，积分余额" + self.dataPool.get('pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_12(self):
        "储值/套餐储值(返现，返积分为0不显示)"

        self.dataPool.set('serviceCode', 'CRM-Stored')  # 业务编码
        self.dataPool.set('serviceSubCode', 'buySaveMoneySet')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('givePoint', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在"+ self.dataPool.get( 'shopName') +"，储值"+ self.dataPool.get( 'saveMoneyAmount') +\
                    "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额"+ self.dataPool.get( 'pointAmount') +"，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_13(self):

        "购买未来权益套餐(第二日返还)"

        self.dataPool.set('serviceCode', 'CRM-Stored')  # 业务编码
        self.dataPool.set('serviceSubCode', 'buyFutureRights')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('givePoint', '0')  # 赠送积分
        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在"+ self.dataPool.get( 'shopName') +"，储值"+self.dataPool.get( 'saveMoneyAmount')+\
                     "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额"+ self.dataPool.get( 'pointAmount') +"，当前可用余额"+ self.dataPool.get( 'canUseMoneyBalance') +\
                     "，冻结金额"+ self.dataPool.get( 'lockMoneyAmount') +"于次日返还，等级为" + self.dataPool.get('cardLevel')
            print ("expMsg:",expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)


    def test_Sms_14(self):

        "购买未来权益套餐(分期返还)"

        self.dataPool.set('serviceCode', 'CRM-Stored')  # 业务编码
        self.dataPool.set('serviceSubCode', 'buyFutureRightsStage')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('givePoint', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg="【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + "，储值"+ self.dataPool.get('saveMoneyAmount') + \
                   "，当前卡值余额" + self.dataPool.get('moneyBalance') + "，积分余额"+ self.dataPool.get( 'pointAmount') + \
                   "，当前可用余额"+self.dataPool.get( 'canUseMoneyBalance')+"，冻结金额"+ self.dataPool.get( 'lockMoneyAmount') +"，分6期返还，每次间隔3天，等级为" + self.dataPool.get('cardLevel')
            print ("expMsg:",expMsg)

            testcase.assertEqual(expMsg, messageContent)

        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_15(self):

        "returnFutureRights（返还未来权益） 定时任务"

        self.dataPool.set('serviceCode', 'CRM-Stored')  # 业务编码
        self.dataPool.set('serviceSubCode', 'returnFutureRights')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('givePoint', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "，今日返还金额10，当前卡余额" + self.dataPool.get('moneyBalance') + \
                     "，当前可用卡值"+self.dataPool.get( 'canUseMoneyBalance')+"，冻结金额"+ self.dataPool.get( 'lockMoneyAmount') +"，剩余分期次数5"
            print ("expMsg:", expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)


    def test_Sms_16(self):

        "调增(赠送卡值不为0显示)"

        self.dataPool.set('serviceCode', 'CRM-Adjust')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountAdjustAdd')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '10')  # 赠送卡值
        self.dataPool.set('givePoint', '0')  # 赠送积分
        self.dataPool.set('modifyMoneyAmount', '50')  # 现金卡值

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + "，现金卡值调增" + self.dataPool.get('modifyMoneyAmount') + \
                     "，赠送卡值调增" + self.dataPool.get('modifyGiveMoneyAmount') + "，积分调增" + self.dataPool.get('modifyPointAmount') + \
                     "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print ("expMsg:", expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_17(self):

        "调增（赠送卡值为０不显示）"

        self.dataPool.set('serviceCode', 'CRM-Adjust')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountAdjustAdd')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '0')  # 积分调增
        self.dataPool.set('modifyGiveMoneyAmount', '0')  # 调账/转账赠送卡值
        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + "，现金卡值调增"+ self.dataPool.get('modifyMoneyAmount') +\
                     "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print ("expMsg:", expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_18(self):

        "调减（赠送卡值不为0显示）"

        self.dataPool.set('serviceCode', 'CRM-Adjust')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountAdjustMinus')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '10')  # 赠送卡值
        self.dataPool.set('givePoint', '0')  # 赠送积分
        self.dataPool.set('modifyPointAmount', '10')  # 积分调增
        self.dataPool.set('modifyGiveMoneyAmount', '10')  # 调账/转账赠送卡值

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + "，现金卡值调减"+ self.dataPool.get('modifyMoneyAmount') +\
                     "，赠送卡值调减" + self.dataPool.get('modifyGiveMoneyAmount') + "，积分调减" + self.dataPool.get('modifyPointAmount') + \
                     "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_19(self):
        "调减（赠送卡值为０不显示）"


        self.dataPool.set('serviceCode', 'CRM-Adjust')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountAdjustMinus')  # 业务子码
        self.dataPool.set('saveMoneyAmount', '12')  # 卡值
        self.dataPool.set('giveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('givePoint', '0')  # 赠送积分
        self.dataPool.set('modifyPointAmount', '0')  # 积分调增
        self.dataPool.set('modifyGiveMoneyAmount', '0')  # 调账/转账赠送卡值

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡" + self.dataPool.get('cardNO') + "在" + self.dataPool.get('shopName') + "，现金卡值调减"+ self.dataPool.get('modifyMoneyAmount') +\
                     "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount') + "，等级为" + self.dataPool.get('cardLevel')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_20(self):
        "转入（转账现金卡值，赠送卡值，积分不为０显示）"


        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunIn')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '10')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '10')  # 赠送积分
        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转入现金卡值"+ self.dataPool.get('modifyMoneyAmount') +"，转入赠送卡值" + self.dataPool.get('modifyGiveMoneyAmount') +\
                     "，转入积分" + self.dataPool.get('modifyPointAmount') + "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_21(self):
        "转入（转入赠送卡值不为0，积分为0时）"


        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunIn')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '10')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转入现金卡值" + self.dataPool.get('modifyMoneyAmount') + "，转入赠送卡值" + self.dataPool.get('modifyGiveMoneyAmount') + \
                     "，当前卡值余额" + self.dataPool.get( 'moneyBalance') + "，积分余额" + self.dataPool.get('pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_22(self):
        "转入（转入赠送卡值为0，积分不为0时）"


        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunIn')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '10')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转入现金卡值" + self.dataPool.get( 'modifyMoneyAmount') + \
                     "，转入积分" + self.dataPool.get('modifyPointAmount') + "，当前卡值余额" + self.dataPool.get( 'moneyBalance') + "，积分余额" + self.dataPool.get('pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_23(self):
        "转入（转入赠送卡值和积分为0时）"


        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunIn')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转入现金卡值"+ self.dataPool.get('modifyMoneyAmount') +"，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_24(self):
        "转出（转账现金卡值，赠送卡值，积分不为０显示）"

        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunOut')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '10')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '10')  # 赠送积分
        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转出现金卡值"+ self.dataPool.get('modifyMoneyAmount') +"，转出赠送卡值" + self.dataPool.get('modifyGiveMoneyAmount') + \
                     "，转出积分" + self.dataPool.get('modifyPointAmount') + "，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_25(self):
        "转出（转出赠送卡值为0，积分为0时）"

        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunOut')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转出现金卡值"+ self.dataPool.get('modifyMoneyAmount') +"，当前卡值余额"+ self.dataPool.get( 'moneyBalance') +"，积分余额" + self.dataPool.get( 'pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_26(self):
        "转出（转账现金卡值，赠送卡值不为0，积分为０）"

        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunOut')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '10')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '0')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转出现金卡值" + self.dataPool.get('modifyMoneyAmount') + "，转出赠送卡值" + self.dataPool.get('modifyGiveMoneyAmount') + \
                     "，当前卡值余额" + self.dataPool.get( 'moneyBalance') + "，积分余额" + self.dataPool.get('pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)

        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_27(self):
        "转出（转账现金卡值，赠送卡值为0，积分不为０显示）"

        self.dataPool.set('serviceCode', 'CRM-Trun')  # 业务编码
        self.dataPool.set('serviceSubCode', 'accountTrunOut')  # 业务子码
        self.dataPool.set('modifyMoneyAmount', '12')  # 卡值
        self.dataPool.set('modifyGiveMoneyAmount', '0')  # 赠送卡值
        self.dataPool.set('modifyPointAmount', '20')  # 赠送积分

        def assertCallbackFunc(testcase=self, response={}):
            messageContent = response.messageContent.encode('UTF-8')
            print("messageContent':", messageContent)
            expMsg = "【哗啦啦】您的会员卡进行了一笔转账交易，转出现金卡值" + self.dataPool.get( 'modifyMoneyAmount') + \
                     "，转出积分" + self.dataPool.get('modifyPointAmount') + "，当前卡值余额" + self.dataPool.get(
                'moneyBalance') + "，积分余额" + self.dataPool.get('pointAmount')
            print('expMsg:', expMsg)
            testcase.assertEqual(expMsg, messageContent)
        self.sms_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)

if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Sms_Template)
    stream = open("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
