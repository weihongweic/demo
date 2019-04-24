FROM ccr.ccs.tencentyun.com/qcloud/centos

RUN mkdir /root/app/

ADD userService.tar.gz /root/app/

ENTRYPOINT ["bash","/root/app/userService/start.sh"]
