#!/usr/bin/env python
# coding: utf-8
import requests
import json
import sys
import aliyun_key
import time

time.sleep(60)
cluster_api = sys.argv[1]
app_name = sys.argv[2]
tag = sys.argv[3]
url = "https://%s/projects/%s" % (cluster_api, app_name)
########钉钉#########
sapp = "#### %s 环境%s 部署成功 \n" % (tag, app_name)
fapp = "#### %s 环境%s 部署失败 \n" % (tag, app_name)
jurl = "https://oapi.dingtalk.com/robot/send?access_token=2a3613c98fbe9a69463545aec995542eac43e6e6e9f6410912b912e2fe7f4949"
headers = {"Content-Type":"application/json", "charset":"utf-8"}
ts = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
times = "> ##### 发布时间: %s \n" % ts
########钉钉#########
if tag == 'dev':
    res = requests.get(url, verify=aliyun_key.dev_ca, cert=aliyun_key.dev_cert_and_key)
elif tag == 'qa':
    res = requests.get(url, verify=aliyun_key.qa_ca, cert=aliyun_key.qa_cert_and_key)
elif tag == 'qaB':
    res = requests.get(url, verify=aliyun_key.qaB_ca, cert=aliyun_key.qaB_cert_and_key)
elif tag == 'devB':
    res = requests.get(url, verify=aliyun_key.devB_ca, cert=aliyun_key.devB_cert_and_key)
elif tag == 'prod':
    res = requests.get(url, verify=aliyun_key.prod_ca, cert=aliyun_key.prod_cert_and_key)
elif tag == 'kkc':
    res = requests.get(url, verify=aliyun_key.kkc_ca, cert=aliyun_key.kkc_cert_and_key)
else:
    print "argv error, please input dev or qa or prod or kkc!"
def first():
	return json.loads(res.content)


#######################
abody = {
    "msgtype": "markdown",
    "markdown": {
        "title": "jenkins",
        "text": fapp +
	     times
    }	
}
#print first()
data = first()
def checkApp(data):
	if data['current_state'] == "running":
		print "%s Application state is: %s" % (app_name, "Running")
	else:
		print "%s Application Deploy Failure!" % app_name
		requests.post(jurl, data=json.dumps(abody), headers=headers)
		sys.exit(1)


def checkService(data):
	service = data['services'][0]
	if service['current_state'] == "running":
		print "%s Services state is: %s" % (service['id'], "Running")
	else:
		print "%s Service Deploy Failure!" % service['id']
		sys.exit(1)
	return service


def checkContainer(service):
        global node
	container = service['containers']
	keyid = container.keys()
	instance = container[keyid[0]]
	#print instance
	if instance['health'] == "success":
		print "%s Container state is: %s" % (instance['name'], "Running")
		if instance['node'] in hosts:
			node = "> ##### 部署node: %s \n" % hosts[instance['node']]
			sbody['markdown']['text'] = "%s \n + %s \n + %s" % (sapp, node, times)
			requests.post(jurl, data=json.dumps(sbody), headers=headers)
	else:
		print "%s Container Deploy Failure!" % instance['name']
		if instance['node'] in hosts:
			node = "> ##### 部署node: %s \n" % hosts[instance['node']]
			fbody['markdown']['text'] = "%s \n + %s \n + %s" % (fapp, node, times)
			requests.post(jurl, data=json.dumps(fbody), headers=headers)
		sys.exit(1)
	return instance


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


#########成功文本##########
node = "> ##### 部署node: dev-cs1 \n"
sbody = {
    "msgtype": "markdown",
    "markdown": {
    "title":"jenkins",
    "text": sapp +
	 node  +
	 times
    }
}
#########失败文本#######
fbody = {
     "msgtype": "markdown",
     "markdown": {
         "title":"jenkins",
         "text": fapp +
	      node +
              times
     }
 }
#getContainerNode(instance)

#aa = getContainerNode(instance)
checkApp(data)
service = checkService(data)
checkContainer(service)
