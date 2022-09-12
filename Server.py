import http.server
import socketserver
import os
from dotenv import load_dotenv

load_dotenv()
def runServer():
  Handler = http.server.SimpleHTTPRequestHandler
  port = os.environ.get('PORT')
  with socketserver.TCPServer(("", int(port)), Handler) as httpd:
    print(f'serving at port {port}')
    httpd.serve_forever()

