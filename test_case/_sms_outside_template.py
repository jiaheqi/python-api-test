# -*- coding: UTF-8 -*-
import json
import logging
import sys
import unittest
import  datetime


reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("../../")

from model.data_pool import DataPool
from common.integretion import HTMLTestRunner

from biz.test_sms_biz import TestSmsBiz


class Test_Sms_Outside_Template(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global caseNum
        caseNum = 0
        cls.sheet_index = 0

        cls.dataPool = DataPool()


        cls.sms_biz = TestSmsBiz(dataPool=cls.dataPool)
        cls.now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')


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

    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")

    def test_Sms_outside_01(self):
        "堂食自助-下单"

        #您在${shopName}的堂食订单${orderKey}已成功下单，下单时间为${acceptTime}。

        self.dataPool.set('groupID', '8')  # 集团编码
        self.dataPool.set('toMobile', '16619756865')  # 手机号
        self.dataPool.set('serviceCode', 'spot_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'SUBMITED')  # 业务子码
        self.dataPool.set('bizSrc', 'order')  # 业务线
        self.dataPool.set('shopName', '小木偶')  # 店铺名称
        self.dataPool.set('orderKey', '2018090312455522')  # 订单号
        self.dataPool.set('acceptTime', self.now)  # 下单时间

        self.dataPool.set('shopID', '76069106')  # 店铺ID
        self.dataPool.set('cardTypeID', '6589815257655414792')  # 卡类型

        self.dataPool.set('shopTel', '0')  # 店铺电话
        self.dataPool.set('shopAddress', '0')  # 店铺地址
        self.dataPool.set('orderTime', '0')  # 预定时间
        self.dataPool.set('takeoutConfirmTime', '0')  # 自提时间
        self.dataPool.set('dueTotalAmount', '0')  # 订单金额
        self.dataPool.set('cancelTime', '0')  # 退款时间
        self.dataPool.set('paymentRemark', '0')  # 退单原因
        self.dataPool.set('takeoutAddress', '0')  # 配送地址
        self.dataPool.set('takeoutTime', '0')  # 送出时间
        self.dataPool.set('takeoutConfirmTime', '0')  # 送达时间
        self.dataPool.set('captcha', '0')  # 验证码


        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)


    def test_Sms_outside_02(self):
        "堂食自助-退款"

        #您在${shopName}的堂食订单${orderKey}因${paymentRemark}已操作退款，所支付金额${dueTotalAmount}元将返回您的支付账户。
        self.dataPool.set('shopID', '76057208')  # 店铺ID
        self.dataPool.set('serviceSubCode', 'REFUNDED')  # 业务子码
        self.dataPool.set('dueTotalAmount', '15')  # 订单金额
        self.dataPool.set('paymentRemark', '测试测试')  # 退单原因

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    '''
    def test_Sms_outside_03(self):
        "堂食自助-支付"

        #您在${shopName}的堂食订单${orderKey}已成功支付，下单时间为${acceptTime}，支付金额为${dueTotalAmount}元。

        self.dataPool.set('serviceSubCode', 'PAID')  # 业务子码
        self.dataPool.set('dueTotalAmount', '10')  # 订单金额

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_04(self):
        "预定-下单"

        #您在${shopName}预订的订单${orderKey}已提交，预订到店时间为${orderTime}。店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'commonreserve_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'SUBMITED')  # 业务子码
        self.dataPool.set('shopTel', '0102233222')  # 店铺电话
        self.dataPool.set('orderTime', self.now)  # 店铺电话

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_05(self):
        "预定-接单"

       #您在${shopName}预订的订单${orderKey}商家已接单。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'ACCEPTED')  # 业务子码

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_06(self):
        "预定-退单"

       #您在${shopName}的预订订单${orderKey}于${cancelTime}退订成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'PENDING_REVOKE')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退单时间
        self.dataPool.set('dueTotalAmount', '14')  # 订单金额

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_07(self):
        "预定-退款"

       #您在${shopName}的预订订单${orderKey}于${cancelTime}退款成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'REFUNDED')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_08(self):
        "闪吃-下单"

       #您在${shopName}预订的“闪吃”订单${orderKey}已提交，预订到店时间为${orderTime}。店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'justeat_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'SUBMITED')  # 业务子码
        self.dataPool.set('orderTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_09(self):
        "闪吃-接单"

       #您在${shopName}预订的“闪吃”订单${orderKey}已开始为您备餐并预留餐桌，为确保菜品品质，请在${orderTime}准时到店就餐。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'ACCEPTED')  # 业务子码
        self.dataPool.set('orderTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_10(self):
        "闪吃-退单"

       #您在${shopName}的预订订单${orderKey}于${cancelTime}退款成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'PENDING_REVOKE')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_11(self):
        "闪吃-退款"

       #您在${shopName}的“闪吃”订单${orderKey}于${cancelTime}退款成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'REFUNDED')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_12(self):
        "自提-下单"

       #您在${shopName}的自提订单${orderKey}已提交，自提时间为${takeoutConfirmTime}。 店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'takeout_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'SUBMITED')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_13(self):
        "自提-接单"

       #您在${shopName}的自提订单${orderKey}正在准备，请于${takeoutConfirmTime}准时到店提取。店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'takeout_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'ACCEPTED')  # 业务子码
        self.dataPool.set('takeoutConfirmTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_14(self):
        "自提-确认自提"

       #您在${shopName}的自提订单${orderKey}已提取，期待您再次光临。店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'takeout_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'OrderSubType')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_15(self):
        "自提-退单"

       #您在${shopName}的自提订单${orderKey}于${cancelTime}退订成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'takeout_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'PENDING_REVOKE')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_16(self):
        "自提-退款"

       #您在${shopName}的自提订单${orderKey}于${cancelTime}退款成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'takeout_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'REFUNDED')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_17(self):
        "外送-下单"

       #您在${shopName}的外送订单${orderKey}已提交，预计${takeoutConfirmTime}送达。店铺电话：${shopTel}

        self.dataPool.set('serviceCode', 'takeaway_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'SUBMITED')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_18(self):
        "外送-接单"

       #您在${shopName}的外送订单${orderKey}正在准备，预计${takeoutConfirmTime}送达，请确保手机号码畅通。店铺电话：${shopTel}
        self.dataPool.set('serviceCode', 'takeaway_order')  # 业务编码
        self.dataPool.set('serviceSubCode', 'ACCEPTED')  # 业务子码
        self.dataPool.set('takeoutConfirmTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_19(self):
        "外送-确认送出"


        #您在${shopName}的外送订单${orderKey}已于${takeoutTime}飞奔向您，请确保${takeoutAddress}有人接收。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'DELIVERYING')  # 业务子码
        self.dataPool.set('takeoutTime',self.now)  # 送出时间
        self.dataPool.set('takeoutAddress', '测试地址')  # 地址

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_20(self):
        "外送-确认送达"

       #您在${shopName}的外送订单${orderKey}已送达，祝您用餐愉快，期待再次光临。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'PENDING_REVIEW')  # 业务子码

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_21(self):
        "外送-退订"

       # 您在${shopName}的外送订单${orderKey}于${cancelTime}退订成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'PENDING_REVOKE')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_22(self):
        "外送-退款"

        #您在${shopName}的外送订单${orderKey}于${cancelTime}退款成功，订单金额${dueTotalAmount}元将返回您的支付账户。店铺电话：${shopTel}

        self.dataPool.set('serviceSubCode', 'REFUNDED')  # 业务子码
        self.dataPool.set('cancelTime',self.now)  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)

    def test_Sms_outside_23(self):
        "会员验证"

        #短信验证码是：${captcha}
        
        self.dataPool.set('serviceCode', 'CRM-Captcha')  # 业务编码
        self.dataPool.set('serviceSubCode', 'captcha')  # 业务子码
        self.dataPool.set('captcha','2389')  # 退款时间

        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Outside_Message_Send(assertCallbackFunc=assertCallbackFunc)
    '''
    def test_Sms_outside_24(self):
        "pos押金"

     
       #${userName}${useSex}，您于${transTime}，在${shopName}，通过${payWay}支付了${transAmount}的押金，核销码为${captcha}，该核销码用于消费支付，切勿告诉他人
    
        self.dataPool.set('bizSrc', 'SAAS')  # 业务线
        self.dataPool.set('serviceCode', 'deposit')  # 业务编码
        self.dataPool.set('serviceSubCode', 'depositCaptcha')  # 业务子码
        self.dataPool.set('toMobile', '16619756865')  # 手机号
        self.dataPool.set('cardTypeID', '6589815257655414792')  # 卡类型

        self.dataPool.set('userName', '张三')  # 客户名
        self.dataPool.set('useSex', '男')  # 性别
        self.dataPool.set('transTime', self.now)  # 交易时间
        self.dataPool.set('payWay', '支付宝')  # 支付方式
        self.dataPool.set('transAmount', '100')  # 押金
        self.dataPool.set('captcha', '20365')  # 核销码


        def assertCallbackFunc(testcase=self, response={}):
            pass

        self.sms_biz.Deposit_Message_Send(assertCallbackFunc=assertCallbackFunc)

if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Sms_Outside_Template)
    stream = file("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
