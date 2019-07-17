# -*- coding: UTF-8 -*-
import urllib2
import json
from common.module import env_module

class HttpUtil(object):
    def __init__(self):
        pass
    def http_post(self,module_host,path, data_json):
        host = env_module.Env_Module().get_grpc_target(module_host)

        headers = {'content-type': "application/json"}
        jdata = json.dumps(data_json)
        print "data_json:", jdata
        print "url:", host+path
        try:
            req = urllib2.Request(host+path, jdata,headers = headers)
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            print e.reason


        return response.read()


