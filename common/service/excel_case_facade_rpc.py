# -*- coding: UTF-8 -*-

import json
import logging
import re
import sys

from grpc._channel import _Rendezvous

from common.module import env_module
from common.module import excel_module
from model.data_pool import DataPool

sys.path.append("..")
sys.path.append("../../")
import grpc

# from deepdiff import DeepDiff
# from pprint import pprint

class GetExcelCaseData:
    """
    初始化获取excelData
    1、获取对应id的行的内容
    2、获取url
    3、获取请求方式
    4、获取请求参数，并进行转码
    5、获取预期结果
    6、将预期结果转换为字典
    7、设置headers
    8、获取response
    9、获取字典格式的response
    :param file_name: 测试数据的文件名
    :param sheet_index: sheet表的索引
    :param id: caseId
    :return:
    """

    def __init__(self):
        self.protoFileName = ''
        self.serviceName = ''
        self.methodName = ''
        self.requestClass = ''
        self.exp_resp = '{}'
        self.data_res = '{}'

    def get_case_data(self, file_name, sheet_index=0, row_id=0, module_proto='order', module_host='order', dataPool=DataPool, data=None,
                      **kwargs):

        """
        1、获取对应id的行的内容
        5、获取预期结果
        8、获取response
        :param file_name: 测试数据的文件名
        :param sheet_index: sheet表的索引
        :param id: caseId
        :return:exp_resp_dic,act_resp_dic
        """
        excel_handle = excel_module.Read_Excel(file_name)
        sheet = excel_handle.get_sheet_by_index(sheet_index)
        case_data_list = excel_handle.get_row_values(sheet, row_id)


        self.protoFileName = case_data_list[1]
        self.serviceName = case_data_list[2]
        self.methodName = case_data_list[3]
        self.requestClass = case_data_list[4]

        if case_data_list[5] is not None:
            self.data_res = case_data_list[5]
        if case_data_list[6] is not None:
            self.exp_resp = case_data_list[6]

        matches = re.findall('\$\{(.*?)\}', self.data_res)
        mset = set(matches)
        for item in mset:
            itemVal = str(dataPool.get(item)).encode('UTF-8')
            self.data_res = self.data_res.replace("${%s}" % item, itemVal)
            if itemVal == '':
                print ('变量{}没有设置值'.format(item))


        self.data = json.loads(self.data_res, encoding="utf-8")
        logging.info(self.data_res)
        if kwargs is not None:
            for i in kwargs:
                for j in self.data:
                    if i == j:
                        self.data[j] = kwargs[i]
        if data is not None:
            self.data = data

        self.data = self.__rewriteData(self.data)

        exp_resp = self.get_case_data_exp()
        act_resp = self.get_case_data_act(module_proto, module_host)


        # print ("exp_resp\n", json.dumps(exp_resp))
        # print("act_resp\n", act_resp)
        return exp_resp, act_resp

    def __rewriteData(self, data):

        if isinstance(data, int) or isinstance(data, float) or isinstance(data, long):
            return data

        if isinstance(data, unicode):
            return data.encode('utf-8')

        if ( isinstance(data, list)):
            _list = []
            for item in data:
                _list.append(self.__rewriteData(item))

            return _list

        if (isinstance(data, tuple)):
            _tuple = []
            for item in data:
                _tuple.append(self.__rewriteData(item))

            return tuple(_tuple)


        if (isinstance(data, dict)):
            _data = {}
            for key in data:
                if isinstance(key, unicode):
                    _key = key.encode('utf-8')
                else:
                    _key = key

                _data[_key] = self.__rewriteData(data[key])

            return _data

        return data







    def get_case_input(self, file_name, sheet_index=0, row_id=0):
        """
        真实数据获取
        1、获取实际结果
        2、获取真实结果
        :return:exp_resp_dic,act_resp_dic
        """
        excel_handle = excel_module.Read_Excel(file_name)
        sheet = excel_handle.get_sheet_by_index(sheet_index)
        case_data_list = excel_handle.get_row_values(sheet, row_id)
        self.data = case_data_list[6]
        return self.data



    def get_case_data_exp(self):
        """
        预期结果获取
        1、直接获取预期结果
        2、将预期结果转换为字典
        :return:预期结果
        """
        logging.debug("-----------------1.expect-------------------------" + self.exp_resp)
        # return self.exp_resp.encode("utf-8")
        return json.loads(self.exp_resp)

    def get_case_data_act(self, module_proto, module_host='order'):
        """s
        真实数据获取
        1、设置headers
        2、获取response
        3、获取字典格式的response
        :param module_host:
        :return:实际结果
        """
        target = env_module.Env_Module().get_grpc_target(module_host);
        print ('target:', target)
        print (self.serviceName + "." + self.methodName)
        print ('input:', json.dumps(self.data))
        channel = grpc.insecure_channel(target)

        pb2 = "test_case.pb2." + module_proto + "." + self.protoFileName + "_pb2"
        pb2_grpc = "test_case.pb2." + module_proto + "." + self.protoFileName + "_pb2_grpc"
        stubName = self.serviceName + "Stub"
        methodName = self.methodName
        requestClass = self.requestClass

        # import test_case.protos.pb2.saasOrderService_pb2
        # import test_case.protos.pb2.saasOrderService_pb2_grpc.SaasOrderServiceStub
        # import test_case.pb2.pos.posmsgservice_pb2
        # import test_case.pb2.pos.posmsgservice_pb2
        # import test_case.pb2.pos.posmsgservice_pb2_grpc;
        pb2_mod = __import__(pb2, fromlist=True)
        pb2_grpc_mod = __import__(pb2_grpc, fromlist=True)

        stub = getattr(pb2_grpc_mod, stubName)(channel)

        request = getattr(pb2_mod, requestClass)(**self.data)
        response = None
        try:
            if(hasattr(stub, methodName)):
                response = getattr(stub, methodName)(request)
        except (
                _Rendezvous
        ) as e:
            print (e)
            print ('grpc exception!!!')

            error_code = e._state.code.name
            error_msg = e._state.details

            if error_code == 'UNAVAILABLE':
                # 当服务状态是不可用的时候，将当前云端的状态置为不可用
                print ('grpc error: UNAVAILABLE')
                raise e
            elif error_code == 'UNAUTHENTICATED':
                # 如果状态是验证未通过，将当前的HPosInfo置为过期
                print ('grpc error: UNAUTHENTICATED')
                raise e
            elif error_code == 'DEADLINE_EXCEEDED':
                # 不间断的五次deadLine，认为链路不可用
                print ('grpc error: DEADLINE_EXCEEDED')
                raise e
            else:
                print ('grpc error: other errors')
                raise e


        # if (hasattr(stub, methodName)):
        #     response = getattr(stub, methodName)(request)
        return response

    def firstCharToLower(self, str):
        return str[0].lower() + str[1:]

    def get_case_data1(self, *case_data_list):

        """
        1、获取对应id的行的内容
        5、获取预期结果
        8、获取response
        :param file_name: 测试数据的文件名
        :param sheet_index: sheet表的索引
        :param id: caseId
        :return:exp_resp_dic,act_resp_dic
        """

        self.protoFileName = case_data_list[1]
        self.serviceName = case_data_list[2]
        self.methodName = case_data_list[3]
        self.requestClass = case_data_list[4]
        module_proto = case_data_list[0]
        module_host = case_data_list[0]

        if case_data_list[5] is not None:
            self.data = case_data_list[5]
        self.data = self.__rewriteData(self.data)
        logging.info(self.data_res)
        act_resp = self.get_case_data_act(module_proto, module_host)

        return act_resp
