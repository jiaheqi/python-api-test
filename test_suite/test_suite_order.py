# coding:utf-8
import sys


sys.path.append("../")


from test_case import test_sms

from test_case import _sms_template,_sms_outside_template,_equity_op_service,_sms_test,_equity_test,test_1,test_sms


from common.service import suiteReporter_facade

business = suiteReporter_facade.SuiteReporter_Utils()
"""
    添加测试套件说明
    1.引入被测模块
    2.运行被测模块并生成报告
    所需参数说明：
    test_module:被测模块（也就是第一步引入的模块）
    report_file_name:测试报告的名字6634780756335920259
    title:报告标题
    description:报告描述
"""
# test_module = [_sms_template ]
#test_module = [_sms_outside_template ]

# test_module = [_equity_op_service ]
# test_module = [_sms_test ]

test_module = [test_sms]
# test_module = [test_1,test_equity]
#test_module = [test_equity]


# test_module = [_equity_test]
test_module = [test_sms]
# test_module = [test_equity]


'''引入被测模块'''
# test_module = [rest_tangshiV2_payafter_addfood_no_promotion]

'''运行测试套件并生成报告'''
business.run_and_report(
    test_module=test_module,
    # report_file_name="test_equity",
    report_file_name="test_sms",
    title=u"HuaLaLa  Service",
    description=u"autotest_server")
