import requests
import json
import yaml
import sys
import aliyun_key
import time
time.sleep(12)

app_name = sys.argv[1]
image_name = sys.argv[2]
tag = sys.argv[3]
domain_name = sys.argv[4]
cluster_api = sys.argv[5]
app_version = sys.argv[6]
app_status = sys.argv[7]
node = sys.argv[8]
nodes = sys.argv[9]
service_name = app_name + "-v" + app_version
if len(sys.argv)<10:
   print 'No action specified.'
   exit()

deploy_url = "https://%s/projects/" % cluster_api
update_url = "https://%s/projects/%s/update" % (cluster_api,app_name)
document = """
%s:
  image: '%s'
  restart: always
  external_links:
    - 'config.local'
    - 'kanche-sn-generator.local'
    - 'kanche-data-dictionary.local'
    - 'service-organization.local'
    - 'kanche-thirdparty-api.local'
    - 'kanche-natification.local'
    - 'kanche-uploader.local'
  environment:
    - 'CONFIG_SERVER_ADDRESS=http://config.local'
    - 'APPLICATION_NAME=%s'
    - 'TAG=%s'
    - constraint:aliyun.node_index==%s
  labels:
    aliyun.scale: '%s'
    aliyun.routing.port_8080: '%s'
    aliyun.latest_image: true
    aliyun.probe.url: tcp://container:8080
    aliyun.probe.timeout_seconds: "10"
    aliyun.probe.initial_delay_seconds: "3"
  volumes:
    - '/logs/%s:/logs'

""" % (service_name, image_name, app_name, tag, node, nodes, domain_name, app_name)

deploy_body = '''{
        "name": "%s",
        "description": "This is a %s application",
        "template": "%s",
	"version": "%s",
	"latest_image": true

}''' % (app_name, app_name, yaml.load(document), app_version)
update_body = '''{
        "name": "%s",
        "description": "This is a %s application",
        "template": "%s",
	"version": "%s",
	"update_method": "blue-green"

}''' % (app_name, app_name, yaml.load(document), app_version)
#print yaml.load(body)
if tag == 'qa':
    if app_status == "deploy":
        res = requests.post(deploy_url, verify=aliyun_key.qa_ca, cert=aliyun_key.qa_cert_and_key, data=deploy_body)
        print res.status_code
    elif app_status == "update":
        res = requests.post(update_url, verify=aliyun_key.qa_ca, cert=aliyun_key.qa_cert_and_key, data=update_body)
        print res.status_code
    else:
	print "Input parameter error, Please check!!!"
        sys.exit(1)
elif tag == 'dev':
    if app_status == "deploy":
        res = requests.post(deploy_url, verify=aliyun_key.dev_ca, cert=aliyun_key.dev_cert_and_key, data=deploy_body)
        print res.status_code
    elif app_status == "update":
        res = requests.post(update_url, verify=aliyun_key.dev_ca, cert=aliyun_key.dev_cert_and_key, data=update_body)
        print res.status_code
    else:
	print "Input parameter error, Please check!!!"
        sys.exit(1)
elif tag == 'devB':
    if app_status == "deploy":
        res = requests.post(deploy_url, verify=aliyun_key.devB_ca, cert=aliyun_key.devB_cert_and_key, data=deploy_body)
        print res.status_code
    elif app_status == "update":
        res = requests.post(update_url, verify=aliyun_key.devB_ca, cert=aliyun_key.devB_cert_and_key, data=update_body)
        print res.status_code
    else:
	print "Input parameter error, Please check!!!"
        sys.exit(1)
elif tag == 'qaB':
    if app_status == "deploy":
        res = requests.post(deploy_url, verify=aliyun_key.qaB_ca, cert=aliyun_key.qaB_cert_and_key, data=deploy_body)
        print res.status_code
    elif app_status == "update":
        res = requests.post(update_url, verify=aliyun_key.qaB_ca, cert=aliyun_key.qaB_cert_and_key, data=update_body)
        print res.status_code
    else:
	print "Input parameter error, Please check!!!"
        sys.exit(1)
elif tag == 'prod':
    if app_status == "deploy":
        res = requests.post(deploy_url, verify=aliyun_key.prod_ca, cert=aliyun_key.prod_cert_and_key, data=deploy_body)
        print res.status_code
    elif app_status == "update":
        res = requests.post(update_url, verify=aliyun_key.prod_ca, cert=aliyun_key.prod_cert_and_key, data=update_body)
        print res.status_code
    else:
	print "Input parameter error, Please enter deploy or update!!!"
        sys.exit(1)
elif tag == 'kkc':
    if app_status == "deploy":
        res = requests.post(deploy_url, verify=aliyun_key.kkc_ca, cert=aliyun_key.kkc_cert_and_key, data=deploy_body)
        print res.status_code
    elif app_status == "update":
        res = requests.post(update_url, verify=aliyun_key.kkc_ca, cert=aliyun_key.kkc_cert_and_key, data=update_body)
        print res.status_code
    else:
	print "Input parameter error, Please enter deploy or update!!!"
        sys.exit(1)
else:
    print 'Parameter error, please enter a dev qa prod'
