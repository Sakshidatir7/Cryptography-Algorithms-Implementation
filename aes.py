from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC)

message = input("Enter message: ").encode()

ciphertext = cipher.encrypt(pad(message, AES.block_size))

print("\nEncrypted Message:")
print(ciphertext.hex())

decipher = AES.new(key, AES.MODE_CBC, cipher.iv)

plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("\nDecrypted Message:")
print(plaintext.decode())