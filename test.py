import numpy as np


def find_invere(n, x):
    for i in range(1, n):
        if gcd(i, n) != 1:
            continue
        for j in range(1, n):
            if i * j % n == 1:
                if x == None:
                    print(i, j)
                elif x == i:
                    print(i, j)
                break


def find_inverse_matrix():
    mat = [[1, 11, 12], [4, 23, 2], [17, 15, 9]]
    n = 26
    determinant = np.linalg.det(mat)
    invert = np.linalg.inv(mat).T
    cofactor = invert * determinant
    print(determinant)
    print(21 * cofactor % n)


def find_log(a, b, p):
    x = 1
    for k in range(1, p):
        x = x * a % p
        if x == b:
            return k
    return -1


def find_bin(a):
    s = ""
    while a > 0:
        s += str(a & 1)
        a = a >> 1
    return s[::-1]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Extended Euclidean
def gcd_extended(a: int, b: int):
    if b == 0:
        return (a, 1, 0)

    x2, x1 = 1, 0
    y2, y1 = 0, 1
    while b > 0:
        q = a // b
        a, b = b, a % b
        x2, x1 = x1, x2 - q * x1
        y2, y1 = y1, y2 - q * y1

    return (a, x2, y2)


# Extended Euclidean for modular inverse
def modinv(a: int, n: int):
    if n == 0:
        return a

    x1, x2, y1, y2 = 0, 1, 1, 0
    b = n
    while b > 0:
        q = a // b
        a, b = b, a % b
        x2, x1 = x1, x2 - q * x1
        y2, y1 = y1, y2 - q * y1

    return x2 % n


def encode_ascii(text):
    text_size = len(text)
    s = 0
    for t in text:
        s += (ord(t) - 65) * 26 ** (text_size - 1)
        text_size -= 1
    return s


# print(find_bin(83))
# print(encode_ascii("R"))

a = 16
n = 138
inv = modinv(a, n)
print(inv)
print(a * inv % n)
# print(127 * 646 % (23 * 29))
