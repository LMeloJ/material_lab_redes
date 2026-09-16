import socket
import threading

# Configurações do servidor
HOST = '0.0.0.0'
PORT = 55555

clients = []

def read_commands():
    while(True):
        commando = input("")
        if(commando == "start"):
            print("Comecando o jogo!")


def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # --- Adicione esta linha antes do bind() ---
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor de chat iniciado em {HOST}:{PORT}")

    command_thread = threading.Thread(target=read_commands)
    command_thread.daemon = True # Permite que o programa feche mesmo com esta thread rodando
    command_thread.start()

    while True:
            client_socket, addr = server.accept()
            print(f"Conexão aceita de {addr[0]}:{addr[1]}")
            clients.append(client_socket)
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()
    

if __name__ == "__main__":
    start_server()
