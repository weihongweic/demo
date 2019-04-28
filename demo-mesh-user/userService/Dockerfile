FROM docker.oa.com:8080/public/golang:latest
ADD ./demo-mesh-user $GOPATH/src/demo-mesh-user/

WORKDIR  $GOPATH/src/demo-mesh-user/userService/
RUN chmod +x start.sh
EXPOSE 8089
ENTRYPOINT ["bash","start.sh"]
