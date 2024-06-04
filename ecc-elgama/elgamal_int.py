# TR
## -6
# x = 13 * 26 + 11
# x = 349
# p = 919

# a = 315 # selection
# alpha = 7
# beta = 660  # alpha^a mod p

# k = 412 # selection
# y1 = 643  # alpha^k mod p
# y2 = 617  # x.beta^k mod p

# 434 = (y1^a)^-1 = y1^(p-a-1)
# d = y2(y1^a)^-1 mod p
# 36,434


import random
from primitive import find_primitive


def encrypt_int(x, p, alpha, beta):
    k = random.randint(2, p)
    y1 = pow(alpha, k, p)
    y2 = x * pow(beta, k, p) % p

    return (y1, y2)


def decrypt_int(y1, y2, a, p):
    y = y2 * pow(y1, p - a - 1, p) % p
    return y


def main():
    p = 489133282872437279
    a = 1234123
    # alpha = find_primitive(p)
    alpha = 13
    print("primitive:", alpha)
    if alpha == -1:
        print("No primitive found!")
        return

    # Diff-Helman
    beta = pow(alpha, a, p)
    print("my beta:", beta)
    # b = 54954500367826819
    betab = 209036596540015354
    common = pow(betab, a, p)
    print("common key:", common)

    # elgama
    a = common
    beta = pow(alpha, a, p)

    print("new beta:", beta)

    x = 23025112
    print("message:", x)
    (y1, y2) = encrypt_int(x, p, alpha, beta)
    print("y:", y1, y2)
    decrypted = decrypt_int(y1, y2, a, p)
    print("decrypted:", decrypted)


if __name__ == "__main__":
    main()
