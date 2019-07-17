# -*- coding: UTF-8 -*-
import json
import logging
import sys
import unittest
from ddt import ddt, data,unpack
import re
from model.data_pool import DataPool


import time

reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("../../")

from common.integretion import HTMLTestRunner
from common.service.excel_util import ExcelUtil

from biz.test_sms_biz import TestSmsBiz
from common.common import Common

excel = ExcelUtil('../data/testdata/test_sms_data.xlsx')

@ddt
class Test_Sms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global caseNum
        caseNum = 0
        cls.sheet_index = 0

        cls.dataPool = DataPool()
        cls.sms_biz = TestSmsBiz(dataPool=cls.dataPool)
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

        self.dataPool.set('groupID', '8')  # 集团编码
        self.dataPool.set('toMobile', '16619756865')  # 手机号
        self.dataPool.set('serviceCode', 'CRM-Card')  # 业务编码
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
        self.dataPool.set('shopID', '76069106')  # 店铺ID

        self.dataPool.set('cardTypeID', '6589815257655414792')  # 卡类型
        self.dataPool.set('cardLevel', 'VIP6')  # 卡等级
        self.dataPool.set('shopName', '小木偶')  # 店铺名称
        self.dataPool.set('cardNO', 'gao1234')  # 卡号





    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")

    count={'first': 1, 'second': 3, 'third': 2}, {'first': 4, 'second': 6, 'third': 5},{'aaa': 4, 'test': 6, 'third': 5}

    # @unpack
    # @data({'first': 1, 'second': 3, 'third': 2}, {'first': 4, 'second': 6, 'third': 5},{'aaa': 4, 'test': 6, 'third': 5})
    # @data(count)
    @data(*excel.next())
    def test_Sms(self,data):

        print data['Test Scene']
        '获取excel中的值'
        subName = data['MethodName']
        input = data['Input']
        expect = eval(data['Expect'])
        if '$' in input:
            '先匹配替换变量'
            input1 = eval(self.com.matches(input))
        else:
            input1=eval(input)
        self.dataPool = DataPool(**input1)


        if(subName=='CRM-Pay'):
            response = self.sms_biz.Consume_Message_Send()
        elif(subName=='messageBatchSend'):
            response = self.sms_biz.messageBatchSend()
        elif (subName=='messageVariableBatchSend'):
            response = self.sms_biz.messageVariableBatchSend()
        else:
            response=self.sms_biz.Message_Send()


        # matches = re.findall('\$\{(.*?)\}', expect)
        # mset = set(matches)
        # for item in mset:
        #     itemVal = str(self.dataPool.get(item))
        #     expect = expect.replace("${%s}" % item, itemVal)
        # print 'expMsg:', expect
        # self.assertEqual(response.result.code,'000')
        # print 'act:',response.messageContent.encode('UTF-8')
        # self.assertEqual(response.messageContent.encode('UTF-8').decode('utf-8'),expect.decode('utf-8'))

        '断言期望值'
        self.com.assertExp(expect, response)

        '将返回的以后用到的set到dataPool'
        if data['Extract Field'] is not None and len(data['Extract Field']) > 0:
            extract_Field = eval(data['Extract Field'])
            self.com.setEf(extract_Field, response)






if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Sms)
    stream = open("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
