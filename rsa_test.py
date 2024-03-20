import rsa_algorithm as rsa
import datetime

# print("Start  :", datetime.datetime.now())
pubkey, privkey = rsa.newkeys(128)
# print("Genkey :", datetime.datetime.now())

plaintext = "Hello World".encode("utf8")
print("Plaintext: ", plaintext)

ciphertext = rsa.encrypt(plaintext, pubkey)
print("Ciphertext: ", ciphertext)

# print("Encrypt:", datetime.datetime.now())

decryptedMessage = rsa.decrypt(ciphertext, privkey)
print("Decrypted message: ", decryptedMessage)

# print("Decrypt:", datetime.datetime.now())
