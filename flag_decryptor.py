from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.backends import default_backend

import os

FLAG = "84794b1ccb6905ab2397aac415c82afbb5fd8d40049d82c3043f0a4200fb77da"
KEY = "0GfABNP4esxc8fDNGQpPnEZJyiaVIoAH"

IV = "NuweSEEuropeanCyberHackathon2022"

backend = default_backend()


key = bytes(KEY, 'ascii')
iv = bytes(IV, 'ascii')[:16]
flag = bytes.fromhex(FLAG)

def unpad(plain):
	if plain[-1] > 16:
		raise ValueError("meh")
	if not all(i==plain[-1] for i in plain[-plain[-1]:]):
		raise ValueError("meh2")
	length = len(plain) - plain[-1]
	return plain[:length]


cipher = Cipher(algorithms.AES256(key), modes.CBC(iv), backend=backend)
decryptor = cipher.decryptor()

flag_decrypted = decryptor.update(flag) + decryptor.finalize()
flag_decrypted = unpad(flag_decrypted)

print(flag_decrypted)

