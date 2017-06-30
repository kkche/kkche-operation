import requests
import sys
import aliyun_key

cluster_api = sys.argv[1]
app_name = sys.argv[2]
tag = sys.argv[3]
if len(sys.argv)<4:
    print 'No action specified.'
    exit()

url = '''https://%s/projects/%s?force=true&v=true''' % (cluster_api, app_name)
if tag == 'qa':
    res = requests.delete(url, verify=aliyun_key.qa_ca, cert=aliyun_key.qa_cert_and_key)
    print res.text
    print res.status_code
elif tag == 'dev':
    res = requests.delete(url, verify=aliyun_key.dev_ca, cert=aliyun_key.dev_cert_and_key)
    print res.text
    print res.status_code
elif tag == 'qaB':
    res = requests.delete(url, verify=aliyun_key.qaB_ca, cert=aliyun_key.qaB_cert_and_key)
    print res.text
    print res.status_code
elif tag == 'devB':
    res = requests.delete(url, verify=aliyun_key.devB_ca, cert=aliyun_key.devB_cert_and_key)
    print res.text
    print res.status_code
elif tag == 'prod':
    res = requests.delete(url, verify=aliyun_key.prod_ca, cert=aliyun_key.prod_cert_and_key)
    print res.text
    print res.status_code
elif tag == 'kkc':
    res = requests.delete(url, verify=aliyun_key.kkc_ca, cert=aliyun_key.kkc_cert_and_key)
    print res.text
    print res.status_code
else:
    print 'Parameter error, please enter a dev qa prod'

