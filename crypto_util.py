from cryptography.fernet import Fernet

# Function to generate a key (should be done once and securely shared)
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message
def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message
