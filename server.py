from http.server import BaseHTTPRequestHandler, HTTPServer

class MeuManipuladorHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        #self.send_header('Connection', 'Keep-Alive')  
        self.end_headers()
        mensagem = "Olá! Este é o meu servidor HTTP em Python."
        self.wfile.write(bytes(mensagem, "utf8"))
        return

def main():
    try:
        endereco = ('localhost', 8000)  
        servidor = HTTPServer(endereco, MeuManipuladorHTTP)
        print(f'Servidor HTTP em execução!')
        print(endereco)
        
        servidor.serve_forever()
        
    except KeyboardInterrupt:
        print('Servidor finalizado com sucesso!')
        servidor.socket.close()

if __name__ == '__main__':
    main()
