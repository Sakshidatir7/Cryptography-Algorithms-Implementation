from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

cipher = PKCS1_OAEP.new(public_key)

message = input("Enter message: ").encode()

encrypted = cipher.encrypt(message)

print("\nEncrypted:")
print(encrypted.hex())

decipher = PKCS1_OAEP.new(private_key)

decrypted = decipher.decrypt(encrypted)

print("\nDecrypted:")
print(decrypted.decode())