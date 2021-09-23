import http.server
import socketserver
import threading
from cardlist import CardList
from controller import Controller

PORT = 8000

class SortServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #looking for pattern like "/json?index=<integer>"
        if len(self.path) > 12 and self.path[0:5] == "/json": #too lazy for regex
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            index = int(self.path[12:]) #too lazy for parsing
            self.wfile.write(cardlist.get_cards_since(index).encode('utf-8'))
        else:
            super().do_GET()

cardlist = CardList()
controller = Controller(cardlist)
with socketserver.TCPServer(("", PORT), SortServer) as httpd:
    c = threading.Thread(target=controller.run)
    c.start()
    print("serving at port", PORT)
    httpd.serve_forever()