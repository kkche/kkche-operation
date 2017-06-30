#!/usr/bin/env python # coding: utf-8
import requests
import json
import sys
import aliyun_key
import time
import re

cluster_api = sys.argv[1]
tag = sys.argv[2]
services = ['config','service-organization','service-vehicle','service-finance-sales','service-merchant','kanche-sms','kanche-vehicle-spec','kanche-data-dictionary','service-vehicle-share','kanche-uploader','kanche-sn-generator','kanche-thirdparty-api','service-customer','service-customer-service','service-vehicle-inspection','service-vehicle-evaluation','legacy-spec-thirdparty-apis','service-vehicle-inspection','service-search-manager','service-billing','service-vehicle-sales','service-mapping-config','service-insurance-sales','service-support','service-menu-config','kanche-notification','service-spy','service-webmagic','service-data-api','service-performance-assessment','download','elasticsearch','es2','kanche-leo','service-vin','zookeeper','kanche-fs','service-task-tracker', 'service-job-tracker','schedule-center-console', 'kanche-taurus','kanche-platform-gateway']

hosts = {
    "139.129.214.230":"dev-cs1", "139.129.215.65":"dev-cs2", "139.129.216.137":"dev-cs3", "114.215.220.41":"dev-cs4", "118.190.112.18":"dev-cs5",
    "139.129.219.128":"qa-cs1", "139.129.219.126":"qa-cs2", "114.215.25.63":"qa-cs3", "115.28.93.55":"qa-cs4",
    "139.129.207.150":"pro-cs1", "139.129.213.204":"pro-cs2", "139.129.212.254":"pro-cs3", "139.129.217.28":"pro-cs4", "139.129.216.98":"pro-cs5", "139.129.206.123":"pro-cs6",
    "118.190.77.158":"pro-cs7", "118.190.133.211":"pro-cs8", "118.190.117.236":"pro-cs9", "118.190.117.220":"pro-cs10",
    "118.190.113.8":"kkc-cs1", "118.190.84.93":"kkc-cs2", "118.190.86.29":"kkc-cs3", "114.215.71.86":"kkc-cs4", "118.190.81.129":"kkc-cs5", "118.190.77.35":"kkc-cs6", 
    "114.215.68.96":"kkc-cs7", "118.190.113.9":"kkc-cs8",
    "118.190.137.169":"devB-cs1", "118.190.112.109":"devB-cs2","118.190.137.137":"devB-cs3","118.190.87.182":"devB-cs4","118.190.79.129":"devB-cs5",
    "118.190.115.81":"qaB-cs1", "118.190.138.160":"qaB-cs2","118.190.138.156":"qaB-cs3","118.190.138.153":"qaB-cs4","118.190.138.118":"qaB-cs5"
}

for app_name in services:
    url = "https://%s/projects/%s" % (cluster_api, app_name)
    if tag == 'dev':
	res = requests.get(url, verify=aliyun_key.dev_ca, cert=aliyun_key.dev_cert_and_key)
        #print json.loads(res.content)
        data = json.loads(res.content)
	service = data['services'][0]
        container = service['containers']
	keyid = container.keys()
	instance = container[keyid[0]]
#        print instance['node']
#        print instance['name']
        if instance['node'] in hosts:
            #re.split('_', instance['name'])[0].replace('/','')
            print "%s %s" % (hosts[instance['node']], app_name)
        else:
            print "%s not " % app_name
    elif tag == 'qa':
        res = requests.get(url, verify=aliyun_key.qa_ca, cert=aliyun_key.qa_cert_and_key)
        #print res.status_code
        if res.status_code != 200:
            print "%s not" % app_name
            continue
        data = json.loads(res.content)
	service = data['services'][0]
        container = service['containers']
	keyid = container.keys()
	instance = container[keyid[0]]
#        print instance['node']
#        print instance['name']
        if instance['node'] in hosts:
            #re.split('_', instance['name'])[0].replace('/','')
            print "%s %s" % (hosts[instance['node']], app_name)
        else:
            print "%s not " % app_name
    elif tag == 'qaB':
        res = requests.get(url, verify=aliyun_key.qaB_ca, cert=aliyun_key.qaB_cert_and_key)
        print json.loads(res.content)
    elif tag == 'devB':
        res = requests.get(url, verify=aliyun_key.devB_ca, cert=aliyun_key.devB_cert_and_key)
        print json.loads(res.content)
    elif tag == 'prod':
        res = requests.get(url, verify=aliyun_key.prod_ca, cert=aliyun_key.prod_cert_and_key)
        print json.loads(res.content)
    elif tag == 'kkc':
        res = requests.get(url, verify=aliyun_key.kkc_ca, cert=aliyun_key.kkc_cert_and_key)
        if res.status_code != 200:
            print "%s not" % app_name
            continue
        data = json.loads(res.content)
	service = data['services'][0]
        container = service['containers']
	keyid = container.keys()
	instance = container[keyid[0]]
        if instance['node'] in hosts:
            print "%s %s" % (hosts[instance['node']], app_name)
        else:
            print "%s not " % app_name
    else:
	    print "argv error, please input dev or qa or prod or kkc!"



"""
def getServiceNode(cluster_api, tag, services):
    for app_name in services:
	res = requests.get(url, verify=aliyun_key.dev_ca, cert=aliyun_key.dev_cert_and_key)


def first():
	return json.loads(res.content)

def checkService(data):
	service = data['services'][0]
	if service['current_state'] == "running":
		print "%s Services state is: %s" % (service['id'], "Running")
	else:
		print "%s Service Deploy Failure!" % service['id']
		sys.exit(1)
	return service


def checkContainer(service):
	container = service['containers']
	keyid = container.keys()
	instance = container[keyid[0]]
	#print instance
	if instance['health'] == "success":
		print "%s Container state is: %s" % (instance['name'], "Running")
		if instance['node'] in hosts:
			node = "> ##### 部署node: %s \n" % hosts[instance['node']]
			sbody['markdown']['text'] = "%s \n + %s \n + %s" % (sapp, node, times)
	else:
		print "%s Container Deploy Failure!" % instance['name']
		if instance['node'] in hosts:
		sys.exit(1)
	return instance
"""

#getContainerNode(instance)

#aa = getContainerNode(instance)
#checkApp(data)
#service = checkService(data)
#checkContainer(service)
