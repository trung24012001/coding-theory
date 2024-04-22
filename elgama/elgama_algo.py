# # TR
# ## -6
# x = 13 * 26 + 11
# x = 349
# p = 919

# a = 315 # selection
# alpha = 7
# beta = 660  # alpha^a mod p

# k = 412 # selection
# y1 = 643  # alpha^k mod p
# y2 = 617  # x.beta^k mod p

# # 434 = (y1^a)^-1 = y1^(p-a-1)
# # d = y2(y1^a)^-1 mod p


# # 36,434


import random
import prime
from primitive import find_primitive


def text2int(x):
    n = len(x)
    s = 0
    while n > 0:
        s += (ord(x[n - 1]) - 64) * 26 ** (n - 1)
        n -= 1
    return s


def int2text(s):
    x = ""
    while s > 0:
        s, r = divmod(s, 26)
        x += chr(r + 64)
    return x


def encrypt_int(x, p, alpha, beta):
    k = random.randint(2, p)
    y1 = pow(alpha, k, p)
    y2 = x * pow(beta, k, p) % p

    return (y1, y2)


def encrypt(text, p, alpha, beta):
    x = text2int(text)
    return encrypt_int(x, p, alpha, beta)


def decrypt_int(y1, y2, a, p):
    y = y2 * pow(y1, p - a - 1, p) % p
    return y


def decrypt(y1, y2, a, p):
    d = decrypt_int(y1, y2, a, p)
    return int2text(d)


def main():
    p = prime.get_prime(64)
    print(len(str(p)))
    a = random.randint(p // 2, p)
    alpha = find_primitive(p)
    if alpha == -1:
        print("No primitive found!")
        return
    beta = pow(alpha, a, p)

    plaintext = "HELLOWORLD"
    print("plaintext:", plaintext)
    (y1, y2) = encrypt(plaintext, p, alpha, beta)
    decryptedText = decrypt(y1, y2, a, p)
    print("decrypted:", decryptedText)


if __name__ == "__main__":
    main()
