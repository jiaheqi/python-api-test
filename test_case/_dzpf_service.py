# -*- coding: UTF-8 -*-
import json
import logging
import sys
import unittest
import  time
from model.data_pool import DataPool
import datetime
import random

reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("../../")


from common.integretion import HTMLTestRunner

from biz.test_dzfp_biz import TestDzfpBiz



class Test_Dzfp_Service(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        global caseNum
        caseNum = 0
        cls.sheet_index = 0

        cls.dataPool = DataPool()

        cls.dzfp_biz = TestDzfpBiz(dataPool=cls.dataPool)
        cls.now = time.strftime("%Y%m%d%H%M%S", time.localtime())



    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """
        获取本类的类名，用来找到数据池里的数据文件
        :return:
        """

        __file_name = 'test_dzfp_grpc',
        self.file_name = "../data/%s.xlsx" % __file_name
        global caseNum
        caseNum += 1
        logging.info("-------------CASE" + str(caseNum) + " START---------------------")

        self.dzfp_biz.setTestCase(self)


    def tearDown(self):
        logging.info("-------------CASE" + str(caseNum) + " FINISH---------------------")


    def test_Dzfp_01(self):
        "预开票"
        order_id = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + str(
            random.randint(0000000000, 9999999999))
        self.dataPool.set('traceID', 'a4e3f248-3b0e-1ac3-9241-514f1d10691b')
        self.dataPool.set('groupID', '8')
        self.dataPool.set('taxShopID', '76069106')
        self.dataPool.set('taxShopName', '高焕的店铺')
        self.dataPool.set('orderKey', order_id)
        self.dataPool.set('shopOrderKey', order_id)
        self.dataPool.set('orderTotal', '12.00')
        self.dataPool.set('orderTime', self.now)
        print self.now
        self.dataPool.set('taxOrderNo', order_id)

        def assertCallbackFunc(testcase=self, response={}):
            print "response:",response
            print "response:", response.result.message
        self.dzfp_biz.Message_Send(assertCallbackFunc=assertCallbackFunc)



if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Dzfp_Service)
    stream = file("../report/test.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title="titile", description="desc")
    runner.run(suite)
