import socket
import threading


def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:import socket
import threading
from cryptography.fernet import Fernet
from crypto_utils import encrypt_message, decrypt_message


key = b'mysecretkeygeneratedbyfernet'  


def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            message = decrypt_message(key, encrypted_message)
            print(f"Received from {client_address}: {message}")
            for client in clients:
                if client != client_socket:
                    client.send(encrypt_message(key, message))
        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"Connection closed from {client_address}")
    client_socket.close()
    clients.remove(client_socket)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server listening on port 12345")

clients = []

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

                break
            print(f"Received from {client_address}: {message.decode()}")
            # Broadcast message to all clients
            for client in clients:
                if client != client_socket:
                    client.send(message)
        except:
            break
    print(f"Connection closed from {client_address}")
    client_socket.close()
    clients.remove(client_socket)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(5)
print("Server listening on port 12345")

clients = []

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
