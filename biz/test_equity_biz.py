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

class TestEquityBiz(BaseBiz):

    def __init__(self,dataPool=DataPool):
        # type: (object, object) -> object
        self.testcase = unittest.TestCase
        self.dataPool = dataPool


        __file_name = 'test_equity_grpc',
        self.file_name = "../data/%s.xlsx" % __file_name

        self.sheet_index = 0
        self.excel_facade = excel_case_facade_rpc.GetExcelCaseData()

        pass



    def Recharge_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=1,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print(response)

        if(response.result.code=='000'):
            result=self.queryRechargeDetail()
            self.testcase.assertEqual(str(result.model.rechargeAmount), self.dataPool.get('rechargeAmount'))

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)
        return response
    def Recharge_test_Send(self):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=1,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print response

        if(response.result.code=='000'):
            result=self.queryRechargeDetail()
            self.testcase.assertEqual(result.model.rechargeAmount, long(self.dataPool.get('rechargeAmount')))
        return response


    def Consume_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=2,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print response



        return response


    def Correct_Send(self):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=3,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)

        response = caseData[1]
        expectData = caseData[0]
        print response
        if (response.result.code == '000'):
            result = self.queryCorrectDetail()
            self.testcase.assertEqual(result.model.correctAmount, long(self.dataPool.get('correctAmount')))

        return response

    def Refund_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=4,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)

        response = caseData[1]
        expectData = caseData[0]
        print response
        # self.testcase.assertEqual(response.result.code, expectData['result']['code'])

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)

    def Refund_test_Send(self):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=4,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)

        response = caseData[1]
        expectData = caseData[0]
        return response
        # self.testcase.assertEqual(response.result.code, expectData['result']['code'])


    def updateAccountOpen(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=5,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print response
        if (response.result.code == '000'):
            result = self.queryAccountDetail()
            state=''
            if(result.accountState==1):
                state='OPENED'
            elif(result.accountState==2):
                state = 'CLOSED'
            elif(result.accountState == 3):
                state = 'FREEZED'
            else:
                state = 'CANCELED'
            self.testcase.assertEqual(result.accountModel.isAllowNegtive, self.dataPool.get('isAllowNegtive'))
            if(self.dataPool.get('overdraftAmount')!='null'):
                self.testcase.assertEqual(result.accountModel.overdraftAmount,int(self.dataPool.get('overdraftAmount')))
            else:
                self.testcase.assertEqual(result.accountModel.overdraftAmount,0)
            self.testcase.assertEqual(state, self.dataPool.get('accountState'))
        # if callable(assertCallbackFunc):
        #     assertCallbackFunc(testcase=self.testcase, response=response)
        return response

    def queryParamAccountPageInfo(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=6,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print response
        # self.testcase.assertEqual(response.result.code, expectData['result']['code'])

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)
        return response

    def open(self):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=11,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)

        response = caseData[1]
        expectData = caseData[0]
        print response


        return response

    def updateAccount(self):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=12,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)

        response = caseData[1]
        expectData = caseData[0]
        print response

        return response

    def queryRechargeDetail(self):

        # self.dataPool.set('rechargeOrderNo', rechargeOrderNo)  #
        # self.dataPool.set('businessSrcToken', businessSrcToken)  #
        # self.dataPool.set('accountNo', accountNo)  # 资产账户

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=7,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        return response

    def queryConsumeDetail(self):

        # self.dataPool.set('consumeOrderNo', consumeOrderNo)  #
        # self.dataPool.set('businessSrcToken', businessSrcToken)  #
        # self.dataPool.set('accountNo', accountNo)  # 资产账户

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=8,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print response
        return response

    def queryCorrectDetail(self):

        # self.dataPool.set('correctOrderNo', correctOrderNo)  #
        # self.dataPool.set('businessSrcToken', businessSrcToken)  #
        # self.dataPool.set('accountNo', accountNo)  # 资产账户

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=9,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print response
        return response

    def queryAccountDetail(self):

        # self.dataPool.set('accountNo', accountNo)  # 资产账户

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=10,
                                                   module_proto='equity', module_host='equity', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        print response
        return response


