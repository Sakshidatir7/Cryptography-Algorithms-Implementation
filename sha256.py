import hashlib

text = input("Enter text: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("\nSHA-256 Hash:")
print(hash_value)