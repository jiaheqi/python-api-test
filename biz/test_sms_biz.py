# coding:utf-8

import json
import sys
import time
import unittest

from biz.base_biz import BaseBiz
from model.data_pool import DataPool

reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("../")
from common.service import excel_case_facade_rpc

class TestSmsBiz(BaseBiz):

    def __init__(self,dataPool=DataPool):
        # type: (object, object) -> object
        self.testcase = unittest.TestCase
        self.dataPool = dataPool


        __file_name = 'test_sms_grpc',
        self.file_name = "../data/%s.xlsx" % __file_name

        self.sheet_index = 0

        self.excel_facade = excel_case_facade_rpc.GetExcelCaseData()

        pass


    def  Message_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=1,
                                                   module_proto='sms', module_host='sms', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print 'response:',response

        return response


    def Consume_Message_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=2,
                                                   module_proto='sms', module_host='sms', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)
        return response

    def Outside_Message_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=3,
                                                   module_proto='sms', module_host='sms', dataPool=self.dataPool)

        response = caseData[1]
        print ('输出短信:',response.messageContent.encode('UTF-8'))
        expectData = caseData[0]
        self.testcase.assertEqual(response.result.code, expectData['result']['code'])

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)

    def Deposit_Message_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=4,
                                                   module_proto='sms', module_host='sms', dataPool=self.dataPool)

        response = caseData[1]
        print( '输出短信:',response.messageContent.encode('UTF-8'))
        expectData = caseData[0]
        self.testcase.assertEqual(response.result.code, expectData['result']['code'])

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)

    def messageBatchSend(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=5,
                                                   module_proto='sms', module_host='sms', dataPool=self.dataPool)

        response = caseData[1]
        print( '输出短信:',response)
        expectData = caseData[0]

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)
        return response

    def messageVariableBatchSend(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=6,
                                                   module_proto='sms', module_host='sms', dataPool=self.dataPool)

        response = caseData[1]
        print('输出短信:', response)
        expectData = caseData[0]

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)

        return response




