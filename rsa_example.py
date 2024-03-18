import rsa
import datetime

# print("Start  :", datetime.datetime.now())
pubkey, privkey = rsa.newkeys(1024)
# print("Genkey :", datetime.datetime.now())
# print(pubkey.save_pkcs1("PEM").decode("UTF-8"))
# print(privkey.save_pkcs1("PEM").decode("UTF-8"))

# pubkey, privkey = rsa.newkeys(256)
# print(pubkey.save_pkcs1("PEM").decode("UTF-8"))
# print(privkey.save_pkcs1("PEM").decode("UTF-8"))

plaintext = "hello world".encode("utf8")
print("Plaintext: ", plaintext)

ciphertext = rsa.encrypt(plaintext, pubkey)
print("Ciphertext: ", ciphertext)

# print("Encrypt:", datetime.datetime.now())

decryptedMessage = rsa.decrypt(ciphertext, privkey)
print("Decrypted message: ", decryptedMessage)

# print("Decrypt:", datetime.datetime.now())
