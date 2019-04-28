import json
import sys
import BaseHTTPServer
import common
from BaseHTTPServer import BaseHTTPRequestHandler

sidecarPort = 80


class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/v6/promotion/query':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg = {
                "promotions":
                    [{"itemId":"001", "status":"off"},
                          {"itemId":"002", "status":"on"},
                          {"itemId":"003", "status":"on"}
                          ]
                   }
            self.wfile.write(json.dumps(msg))
        elif self.path == '/api/v6/promotion/item/discount':
            headers = common.build_trace_headers(self)
            headers['x-trace-service'] = "promotion"
            if common.sendAndVerify("shop", sidecarPort, "/api/v6/product/deliver", headers):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg = {
                    "discount": "40",
                    "itemId": "002"
                }
                self.wfile.write(json.dumps(msg))
            else:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg = {"exception":"Error invoke %s" % "/api/v6/product/deliver"}
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
    print >> sys.stderr, "Starting promotionService, use <Ctrl-C> to stop"
    server.serve_forever()
