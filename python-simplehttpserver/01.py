# 01.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send 200 response
        self.send_response(200)
        # send response headers
        self.end_headers()
        # send the body of the response
        self.wfile.write(bytes("It Works!", "utf-8"))

httpd = HTTPServer(('localhost', 10000), MyHandler)
httpd.serve_forever()