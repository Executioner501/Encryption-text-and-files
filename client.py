import socket
import threading
from cryptography.fernet import Fernet
from crypto_utils import encrypt_message, decrypt_message

# Key should be securely shared beforehand
key = b'mysecretkeygeneratedbyfernet'  # Replace with your generated key

def receive_messages(client_socket):
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            message = decrypt_message(key, encrypted_message)
            print(message)
        except Exception as e:
            print(f"Error: {e}")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

print("Connected to the chat server. Type your messages below.")

while True:
    message = input()
    if message.lower() == 'quit':
        break
    encrypted_message = encrypt_message(key, message)
    client_socket.send(encrypted_message)

client_socket.close()
