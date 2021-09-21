import http.server
import socketserver
import json

PORT = 8000

class SortServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/json":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'peepee': 'poopoo', 'card1': 'Storm Crow'}).encode('utf-8'))
        else:
            super().do_GET()


with socketserver.TCPServer(("", PORT), SortServer) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()