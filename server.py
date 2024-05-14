import http.server
import socketserver
import re

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        return super().do_HEAD()
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Connection", "keep-alive")
        self.send_header('keep-alive', 'timeout=1, max=10')
        self.end_headers()

        message = """
        <html>
        <body>
        <h1>Bem vindo ao servidor de testes!</h1>
        
        <p>O conteudo vai ser exibido abaixo!</p>
        </body>
        </html>
        """
        self.wfile.write(message.encode())
        msg = ""
        print('Digite abaixo para exibir texto no cliente \nPara sair digite S')       
        while True:
            script = r'<script.*?</script>|<.*?javascript:.*?>|<.*?\\s+on.*?>'
            texto = input('Mensagem: ')
            if texto != 'S':
                texto_tratado = re.sub(script, '', texto, flags=re.IGNORECASE | re.DOTALL)
                result = msg + texto_tratado + '</br>'
                self.wfile.write(result.encode())
                self.wfile.flush()
            else:
                break

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
