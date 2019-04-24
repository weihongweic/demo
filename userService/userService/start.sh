#! /bin/bash

mkdir -p /opt/tsf/app_config/apis 
cp /root/app/userService/spec.yaml /opt/tsf/app_config/
cp -r /root/app/userService/apis /opt/tsf/app_config/
cd /root/app/userService/
python ./userService.py 8089 1>./logs/user.log 2>&1
