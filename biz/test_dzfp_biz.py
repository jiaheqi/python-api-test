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

class TestDzfpBiz(BaseBiz):

    def __init__(self,dataPool=DataPool):
        # type: (object, object) -> object
        self.testcase = unittest.TestCase
        self.dataPool = dataPool


        __file_name = 'test_dzfp_grpc',
        self.file_name = "../data/%s.xlsx" % __file_name

        self.sheet_index = 0

        self.excel_facade = excel_case_facade_rpc.GetExcelCaseData()

        pass


    def  Message_Send(self, assertCallbackFunc=None):

        caseData = self.excel_facade.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=1,
                                                   module_proto='dzfp', module_host='dzfp', dataPool=self.dataPool)
        response = caseData[1]
        expectData = caseData[0]
        self.testcase.assertEqual(response.result.code, expectData['result']['code'])

        if callable(assertCallbackFunc):
            assertCallbackFunc(testcase=self.testcase, response=response)







