import requests
import sys
import aliyun_key
cluster_api = sys.argv[1]
app_name = sys.argv[2]
tag = sys.argv[3]

url = "https://%s/projects/%s/rollback-update?force=true" % (cluster_api, app_name)
if tag == 'qa':
    res = requests.post(url, verify=aliyun_key.qa_ca, cert=aliyun_key.qa_cert_and_key)
    print res.status_code
elif tag == 'dev':
    res = requests.post(url, verify=aliyun_key.dev_ca, cert=aliyun_key.dev_cert_and_key)
    print res.status_code
elif tag == 'prod':
    res = requests.post(url, verify=aliyun_key.prod_ca, cert=aliyun_key.prod_cert_and_key)
    print res.text
    print res.status_code
elif tag == 'kkc':
    res = requests.post(url, verify=aliyun_key.kkc_ca, cert=aliyun_key.kkc_cert_and_key)
    print res.status_code
else:
    print 'Parameter error, please enter a dev qa prod'
