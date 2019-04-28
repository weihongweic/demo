#!/bin/bash
mkdir -p /opt/tsf/app_config/apis 
cp  $GOPATH/src/demo-mesh-user/userService/spec.yaml /opt/tsf/app_config/
cp -r $GOPATH/src/demo-mesh-user/userService/apis /opt/tsf/app_config/
cd  $GOPATH/src/demo-mesh-user/userService/
python ./userService.py 8089
