#!/usr/bin/env python

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
"kanche-platform-gateway":{"external_links":kanche_platform_gateway_links, "node": 1},
"service-organization":{"external_links":service_organization_links, "node": 1},
"service-menu-config":{"external_links":base_links, "node": 1},"kanche-fs":{"external_links": base_links, "node": 2},
"kanche-sms":{"external_links": base_links, "node": 2},
"kanche-uploader":{"external_links": base_links, "node": 1}, "kanche-data-dictionary":{"external_links":base_links, "node": 1},
"kanche-sn-generator":{"external_links":base_links, "node": 2},"kanche-vehicle-spec":{"external_links": base_links, "node": 2},
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
    print app_name
    print services[app_name]['external_links']
    print services[app_name]['node']
