from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

KEY = b'1234567890123456'  # 16-byte key (Use secure key management in real apps)
BLOCK_SIZE = 16

def pad(data):
    return data + b"\0" * (BLOCK_SIZE - len(data) % BLOCK_SIZE)

def encrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    data = pad(data)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = iv + cipher.encrypt(data)
    
    enc_path = filepath + '.enc'
    with open(enc_path, 'wb') as f:
        f.write(encrypted)
    return enc_path

def decrypt_file(enc_path):
    with open(enc_path, 'rb') as f:
        encrypted = f.read()
    iv = encrypted[:BLOCK_SIZE]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted[BLOCK_SIZE:]).rstrip(b'\0')
    
    dec_path = enc_path.replace('.enc', '.dec')
    with open(dec_path, 'wb') as f:
        f.write(decrypted)
    return dec_path
