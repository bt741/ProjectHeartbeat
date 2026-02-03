
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

class HeartbeatHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        print(f"Received heartbeat: {post_data.decode('utf-8')}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Heartbeat received')


def run(server_class=HTTPServer, handler_class=HeartbeatHandler, ip=None, port=None):
    # Get IP and port from environment or use defaults
    ip = ip or os.getenv('SERVER_IP', 'localhost')
    port = int(port or os.getenv('SERVER_PORT', 8900))
    server_address = (ip, port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting heartbeat server on {ip}:{port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
