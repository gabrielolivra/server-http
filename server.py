from http.server import BaseHTTPRequestHandler, HTTPServer

# Define a classe do manipulador HTTP personalizado
class MeuManipuladorHTTP(BaseHTTPRequestHandler):
    
    # Método para lidar com solicitações GET
    def do_GET(self):
        # Configura o cabeçalho de resposta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        #self.send_header('Connection', 'Keep-Alive')  # Define a conexão como Keep-Alive
        self.end_headers()
        # Corpo da resposta
        mensagem = "Olá! Este é o meu servidor HTTP em Python."
        self.wfile.write(bytes(mensagem, "utf8"))
        return

# Função principal para inicializar o servidor
def main():
    try:
        # Definindo o endereço e a porta do servidor
        endereco = ('localhost', 8000)  # Use '' para aceitar solicitações em todos os IPs da máquina
        servidor = HTTPServer(endereco, MeuManipuladorHTTP)
        print(f'Servidor HTTP em execução!')
        print(endereco)
        
        # Mantém o servidor em execução até que o usuário pressione Ctrl+C
        servidor.serve_forever()
        
    except KeyboardInterrupt:
        print('Servidor finalizado com sucesso!')
        servidor.socket.close()

if __name__ == '__main__':
    main()
