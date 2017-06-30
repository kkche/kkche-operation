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
cluster_api = sys.argv[4]
app_version = sys.argv[5]
app_status = sys.argv[6]
node = sys.argv[7]
nodes = sys.argv[8]
service_name = app_name + "-v" + app_version
if len(sys.argv)<9:
   print 'No action specified.'
   exit()

deploy_url = "https://%s/projects/" % cluster_api
update_url = "https://%s/projects/%s/update" % (cluster_api,app_name)
document = """
%s:
  image: '%s'
  restart: always
  container_name: es1.cloud
  environment:
    - constraint:aliyun.node_index==%s
  command:
    - '-Des.cluster.name=kanche-devB'
    - '-Des.networmk.host=0.0.0.0'
    - '-Des.network.publish_host=es1.cloud'
    - '-Des.discovery.zen.ping.multicast.enabled=false'
  labels:
    aliyun.scale: '%s'
    aliyun.latest_image: true
  volumes:
    - '/data/%s:/usr/share/elasticsearch/data:rw'

""" % (service_name, image_name, node, nodes, app_name)

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
