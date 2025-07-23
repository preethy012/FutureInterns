from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import os

key = os.environ.get("AES_KEY", get_random_bytes(16))

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def encrypt_file(file_data):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(file_data)
    return b64encode(cipher.encrypt(padded_data))

def decrypt_file(encrypted_data):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(b64decode(encrypted_data)).rstrip(b' ')
