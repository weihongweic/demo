FROM ccr.ccs.tencentyun.com/qcloud/centos

RUN mkdir /root/app/

ADD shopService.tar.gz /root/app/

ENTRYPOINT ["bash","/root/app/shopService/start.sh"]
