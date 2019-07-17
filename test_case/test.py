# coding:utf-8
def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):  
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身



# dic={"accountModel": {"transTime": "", "alarmAmount": 0, "businessType": "\\u77ed\\u4fe1", "transDate": "20181017", "businessSrc": "\\u5185\\u90e8\\u7ebf", "accountName": "cs151835742", "alarmPhone": "13255256541", "organizationId": "8", "memo": "\\u65e0", "isAllowWithdrawal": "N", "useDefaultAlarm": "N", "businessSrcToken": "201810171518356697", "isAllowRecharge": "Y", "subBusinessType": "\\u8425\\u9500", "equityType": "SMS", "balanceUnit": "SCALE_TIAO", "overdraftAmount": 0, "isAllowNegtive": "N", "organizationType": "GROUP", "operatorId": "6592133101197991936"}}
dic='''{
  traceID: "947a07d8-0b26-4d1e-ae80-220dd9183f37"
  code: "00116002"
  message: "\345\212\240\351\224\201\345\244\261\350\264\245\357\274\214\346\237\245\344\270\215\345\210\260\345\216\237\350\264\246\345\217\267accountNo\344\270\272:6574692226"
}'''
print eval(dic)
tmp_list=[]
ls=get_target_value('transDate',dic,tmp_list)
ls=get_target_value('alarmAmount',dic,tmp_list)
print ls