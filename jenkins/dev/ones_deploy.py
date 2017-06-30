#!/usr/bin/env python
# codinig: utf-8
import requests
import json
import yaml
import sys
import aliyun_key
import time

cluster_api = sys.argv[1]
tag = sys.argv[2]
nodes = "1"
if len(sys.argv)<3:
   print 'No action specified.'
   exit()

deploy_url = "https://%s/projects/" % cluster_api

kanche_platform_gateway_links = ['config.local', 'service-organization.local', 'service-vehicle.local', 'service-finance-sales.local', 'service-merchant.local', 'kanche-sms.local', 'kanche-vehicle-spec.local', 'kanche-data-dictionary.local', 'service-vehicle-share.local', 'kanche-uploader.local', 'kanche-sn-generator.local', 'kanche-thirdparty-api.local', 'service-customer.local', 'service-customer-service.local', 'service-vehicle-inspection.local', 'service-vehicle-evaluation.local', 'legacy-spec-thirdparty-apis.local', 'service-vehicle-inspection.local', 'service-search-manager.local', 'service-billing.local', 'service-vehicle-sales.local', 'service-mapping-config.local', 'service-insurance-sales.local', 'service-support.local', 'service-menu-config.local', 'kanche-notification.local', 'service-spy.local', 'service-webmagic.local', 'service-data-api.local', 'service-data-api2.local', 'service-performance-assessment.local']
service_search_manager_links = ['config.local','service-vehicle.local','service-merchant.local','service-organization.local','service-vehicle-sales.local', 'service-customer-service.local', 'service-customer.local','kanche-vehicle-spec.local']
kanche_notification_links = ['config.local', 'kanche-sms.local']
kanche_share_links = ['service-vehicle-share.local']
kanche_thirdparty_api_links = ["config.local", "kanche-sn-generator.local", "legacy-spec-thirdparty-apis.local",]
service_billing_links = ['config.local', 'kanche-sn-generator.local', 'service-mapping-config.local', 'kanche-notification.local', 'service-vehicle.local', 'kanche-fs.local', 'kanche-sms.local', 'kanche-thirdparty-api.local']
service_customer_service_links = ['config.local', 'kanche-sn-generator.local', 'service-vehicle-sales.local']
service_finance_sales_links = ['config.local', 'kanche-sn-generator.local' ,'service-vehicle-inspection.local', 'service-vehicle-evaluation.local', 'kanche-thirdparty-api.local', 'service-mapping-config.local','kanche-fs.local', 'kanche-notification.local']
service_insurance_sales_links = ['config.local', 'kanche-sn-generator.local', 'service-mapping-config.local', 'kanche-notification.local']
service_merchant_links = ['config.local', 'kanche-sn-generator.local', 'kanche-data-dictionary.local', 'service-organization.local', 'kanche-thirdparty-api.local']
service_organization_links = ['config.local', 'kanche-sms.local']
service_performance_assessment_links = ['config.local', 'kanche-sms.local', 'service-organization.local']
service_spy_links = ['config.local', 'kanche-sn-generator.local']
service_task_tracker_links = ['config.local', 'service-customer-service.local', 'service-vehicle-share.local']
service_vehicle_evaluation_links = ['config.local', 'kanche-sn-generator.local', 'kanche-fs.local', 'kanche-notification.local']
service_vehicle_inspection_links = ['config.local', 'kanche-sn-generator.local', 'kanche-data-dictionary.local', 'service-organization.local', 'kanche-thirdparty-api.local', 'kanche-natification.local', 'kanche-uploader.local']
service_vehicle_links = ['config.local', 'kanche-sn-generator.local', 'kanche-vehicle-spec.local', 'service-mapping-config.local', 'service-organization.local', 'kanche-uploader.local', 'kanche-thirdparty-api.local']
service_vehicle_sales_links = ['config.local', 'kanche-sn-generator.local', 'kanche-notification.local', 'service-organization.local', 'service-merchant.local']
service_vehicle_share_links = ['config.local', 'kanche-share.local', 'kanche-sn-generator.local', 'legacy-spec-thirdparty-apis.local']
service_webmagic_links = ['config.local', 'kanche-sn-generator.local']
base_links = ['config.local']

services = {
#"kanche-platform-gateway":{"external_links":kanche_platform_gateway_links, "node": 1},
#"service-organization":{"external_links":service_organization_links, "node": 1},
"service-menu-config":{"external_links":base_links, "node": 1},"kanche-fs":{"external_links": base_links, "node": 2},
#"kanche-sms":{"external_links": base_links, "node": 2},
"kanche-uploader":{"external_links": base_links, "node": 1}, "kanche-data-dictionary":{"external_links":base_links, "node": 1},
"kanche-sn-generator":{"external_links":base_links, "node": 2},#"kanche-vehicle-spec":{"external_links": base_links, "node": 2},
"service-mapping-config":{"external_links": base_links, "node": 3},"service-support":{"external_links":base_links, "node": 4},
"legacy-spec-thirdparty-apis":{"external_links": base_links, "node": 2},"service-customer":{"external_links":base_links, "node": 3},
"service-vin":{"external_links":base_links, "node": 5},"service-data-api":{"external_links":base_links, "node": 5},
"kanche-notification":{"external_links":kanche_notification_links, "node": 1}, "kanche-thirdparty-api": {"external_links": kanche_thirdparty_api_links, "node":2},
"service-billing": {"external_links": service_billing_links, "node": 3}, "service-customer-service": {"external_links": service_customer_service_links,"node":3},
"service-finance-sales": {"external_links": service_finance_sales_links, "node":5},"service-vehicle":{"external_links":service_vehicle_links, "node": 4},"service-vehicle-share":{"external_links":service_vehicle_share_links, "node": 4}, "kanche-share":{"external_links":kanche_share_links, "node": 4},
"service-merchant":{"external_links":service_merchant_links, "node": 3}, "service-vehicle-inspection":{"external_links":service_vehicle_inspection_links, "node": 4},
"service-vehicle-evaluation":{"external_links":service_vehicle_evaluation_links, "node": 5},
"service-insurance-sales":{"external_links":service_insurance_sales_links, "node": 3},
"service-vehicle-sales":{"external_links":service_vehicle_sales_links, "node": 4},
"service-performance-assessment":{"external_links":service_performance_assessment_links, "node": 5},
"service-web-magic":{"external_links":service_webmagic_links, "node": 4}, "service-spy":{"external_links":service_spy_links, "node": 4},
"service-search-manager":{"external_links": service_search_manager_links, "node": 3},
"service-job-tracker":{"external_links":base_links, "node": 3}, "service-task-tracker":{"external_links":service_task_tracker_links, "node": 4},
"schedule-center-console":{"external_links":base_links, "node": 2}
}


for app_name in services.keys():
    image_name = "docker.kkche.cn/%s:1.0.1-devB" % app_name
#    print image_name
    service = services[app_name]
#    print service
#    print(service.get('external_links', 'not exist'))
#    print(service.get('node', 'not exist'))
    daemon_name = app_name+'.local'
    document = """
    %s:
        image: '%s'
        restart: always
        external_links: %s
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
    """ % (app_name, image_name, service['external_links'], app_name, tag, service['node'], nodes, daemon_name, app_name) 
    deploy_body = '''{
        "name": "%s",
        "description": "This is a %s application",
        "template": "%s",
	"version": "1",
	"latest_image": true
    }''' % (app_name, app_name, yaml.load(document))
#    print deploy_body
    url = '''https://%s/projects/%s?force=true&v=true''' % (cluster_api, app_name)
    res = requests.delete(url, verify=aliyun_key.qaB_ca, cert=aliyun_key.qaB_cert_and_key)
#    time.sleep(10)
    res = requests.post(deploy_url, verify=aliyun_key.qaB_ca, cert=aliyun_key.qaB_cert_and_key, data=deploy_body)
    print res.status_code


#update_url = "https://%s/projects/%s/update" % (cluster_api,app_name)

