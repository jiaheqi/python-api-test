# coding:utf-8

import logging
import sys
from setting import ENVIRONMENT_CONFIG
from setting import ENVIRONMENT_GRPC_CONFIG


class Env_Module():
    def __init__(self):
        """
        初始化
        """
        pass

    def get_env_url(self, module):
        """
        :return:返回命令行环境映射地址
        """
        if sys.argv.__len__() < 2:
            env = 'dohko'
        else:
            env = sys.argv[1]
        env_url = ENVIRONMENT_CONFIG[env]
        # env_url = ENVIRONMENT_CONFIG["dohko"]
        if module == '':
            module = 'order'
        return env_url[module]

    def get_grpc_target(self, module):
        if sys.argv.__len__() < 2:
            env = 'dohko'
#            env = 'local'
#            env = 'pre'
        else:
            env = sys.argv[1]
        env_target = ENVIRONMENT_GRPC_CONFIG[env]
        return env_target[module]

