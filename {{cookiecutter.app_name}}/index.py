from http.server import BaseHTTPRequestHandler


def hello_world():
    return "Hello world!"


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = hello_world()
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(data).encode())
        return
