from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
#Claves
def generate_key():
    return os.urandom(32)#Bytes
def generate_iv():
    return os.urandom(16)
#Encriptar archivos
def encrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as f:
        plaintext=f.read()
    cipher=Cipher(algorithms.AES(key),modes.CBC(iv),backend=default_backend())
    encryptor=cipher.encryptor()
    padding_length=16-(len(plaintext)%16)
    padded_plaintext=plaintext+bytes([padding_length]*padding_length)
    ciphertext=encryptor.update(padded_plaintext)+encryptor.finalize()
    encrypted_file_path=file_path+'.enc'
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv+ciphertext)
    print(f"Archivo encriptado: {encrypted_file_path}")