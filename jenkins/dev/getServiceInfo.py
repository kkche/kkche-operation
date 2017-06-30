#!/usr/bin/env python # coding: utf-8
import requests
import json
import sys
import aliyun_key
import time
import re

def getServiceInfo(services, cluster_api, verify, cert):
    for app_name in services:
        url = "https://%s/projects/%s" % (cluster_api, app_name)
        res = requests.get(url, verify=verify, cert=cert)
        return  json.loads(res.content)
            

def getServiceImage(func, services, cluster_api, verify, cert):
	data = func(services, cluster_api, verify, cert)
#        print data
        data = data["services"][0]
        print data['definition']['image']

if __name__ == '__main__':
#    print type(aliyun_key.kkc_ca)
    dev_cluster_api = "master2g1.cs-cn-qingdao.aliyun.com:18934"
    qa_cluster_api = "master2g1.cs-cn-qingdao.aliyun.com:15593"
    devb_cluster_api = "master3g3.cs-cn-qingdao.aliyun.com:20077"
    qab_cluster_api = "master2g3.cs-cn-qingdao.aliyun.com:20128"
    kkc_cluster_api = "master1g3.cs-cn-qingdao.aliyun.com:20158"
    prod_cluster_api = "master1g1.cs-cn-qingdao.aliyun.com:19539"
    ca = aliyun_key.qa_ca
    cert = aliyun_key.qa_cert_and_key
    services = ['kanche-sms']
    #getServiceInfo(['kanche-sms'], qa_cluster_api, ca, cert)
    getServiceImage(getServiceInfo, services, qa_cluster_api, ca, cert)
