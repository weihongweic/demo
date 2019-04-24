FROM harbor.enncloud.cn/enncloud/centos_jdk:1.8.0_131
ADD OpenUrl /OpenUrl
EXPOSE 8080
WORKDIR /OpenUrl
CMD java -jar pyrmont.jar