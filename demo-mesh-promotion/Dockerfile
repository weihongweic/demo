FROM ccr.ccs.tencentyun.com/qcloud/centos

RUN mkdir /root/app/

ADD promotionService.tar.gz /root/app/

ENTRYPOINT ["bash","/root/app/promotionService/start.sh"]
