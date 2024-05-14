import http.server
import socketserver

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        return super().do_HEAD()
    
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Connection", "close")
        self.end_headers()
        # Replace 'Your custom message here' with the desired HTML content
        message = """
        <html>
        <body>
        <h1>Welcome to your custom server!</h1>
        <p>This is the content you requested.</p>
        </body>
        </html>
        """
        self.wfile.write(message.encode())

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
