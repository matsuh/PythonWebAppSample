from http.server import HTTPServer, SimpleHTTPRequestHandler


class MyFirstHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        body = '<html><body>Hello from Python!</body></html>'.encode('utf8')
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), MyFirstHTTPRequestHandler)
    httpd.serve_forever()
