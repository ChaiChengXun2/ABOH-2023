from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2
import textwrap

def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as file:
        ciphertext_iv = file.read()

    iv = ciphertext_iv[-AES.block_size:]
    ciphertext = ciphertext_iv[:-AES.block_size]

    passwd = textwrap.dedent(password)[:-1]
    salt = b'salt123'
    key = PBKDF2(passwd.encode(), salt, dkLen=16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext

password = "ni5h2h?Yrq8Do?n+|6a;pKbZkv%}O~tV"
encrypted_file_path = "./flag.txt.enc"
plaintext = decrypt_file(encrypted_file_path, password)

print(plaintext.decode())