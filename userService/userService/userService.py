import sys
import json
import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import common

sidecarPort = 80


class TodoHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/api/v6/user/create':
            print >> sys.stderr, "headers are %s" % self.headers.keys()
            headers = common.build_trace_headers(self)
            if common.sendAndVerify("shop", sidecarPort, "/api/v6/shop/items", headers):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg = {"result":{"userId":"1234", "userName":"vincent"}}
                self.wfile.write(json.dumps(msg))
            else:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg = {"exception":"Error invoke %s" % "/api/v6/shop/items"}
                self.wfile.write(json.dumps(msg))

        elif self.path == '/api/v6/user/account/query':
            headers = common.build_trace_headers(self)
            headers['x-trace-service'] = "user"
            if common.sendAndVerify("shop", sidecarPort, "/api/v6/shop/order", headers):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg = {"userId":"1234", "detail":{"moneyLeft":52000,"deposit":12000}}
                self.wfile.write(json.dumps(msg))
            else:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg = {"exception":"Error invoke %s" % "/api/v6/shop/order"}
                self.wfile.write(json.dumps(msg))
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg = {
                "status":"UP"
            }
            self.wfile.write(json.dumps(msg))
        else:
            self.send_error(404, "{\"message\":\"File not found.\"}")
            return


if __name__ == '__main__':
    # Start a simple server, and loop forever
    ServerClass  = BaseHTTPServer.HTTPServer
    hostPort = int(sys.argv[1])
    print >> sys.stderr, "host port is %s"%hostPort
    server = ServerClass(('0.0.0.0', hostPort), TodoHandler)
    print >> sys.stderr, "Starting userService, use <Ctrl-C> to stop"
    server.serve_forever()
