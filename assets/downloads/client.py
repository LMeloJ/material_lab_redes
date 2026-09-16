import socket
import threading

# Configurações do cliente
HOST = '172.17.0.1' # Substitua pelo IP do PC que está executando o servidor
PORT = 55555                     # A mesma porta que o servidor está usando

# Pede um nome de usuário para o chat
nickname = input("Digite seu nome de usuário: ")

# Conecta ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Função para receber mensagens do servidor
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            # Se a mensagem for 'NICK', o servidor está pedindo o nickname
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ocorreu um erro! Desconectando do servidor.")
            client.close()
            break

# Função para enviar mensagens para o servidor
def send_messages():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Inicia as threads para receber e enviar mensagens
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
