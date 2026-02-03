from http.server import BaseHTTPRequestHandler, HTTPServer
 # ...existing code...

class HeartbeatHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        print(f"Received heartbeat: {post_data.decode('utf-8')}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Heartbeat received')

def run(server_class=HTTPServer, handler_class=HeartbeatHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting heartbeat server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
