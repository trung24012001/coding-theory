n = 18923
b = 1261


def rsa_decrypt(y, b, n):
    x = y**b % n
    c = 3
    s = ""
    for i in range(c):
        t = 26 ** (c - 1 - i)
        q = x // t
        x = x % t
        s += chr(q + 65)
    return s


s = rsa_decrypt(12423, b, n)
print(s)
