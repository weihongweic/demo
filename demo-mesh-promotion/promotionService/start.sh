#! /bin/bash

mkdir -p /opt/tsf/app_config/apis 
cp /root/app/promotionService/spec.yaml /opt/tsf/app_config/
cp -r /root/app/promotionService/apis /opt/tsf/app_config/
cd /root/app/promotionService/
python ./promotionService.py 8091 1>./logs/promotion.log 2>&1
