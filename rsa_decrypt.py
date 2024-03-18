import math


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def find_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n / i
    return n, 1


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)

    x2, x1 = 1, 0
    y2, y1 = 0, 1
    while b > 0:
        q = a // b
        r = a % b
        x = x2 - q * x1
        y = y2 - q * y1

        a, b = b, r
        x2, x1 = x1, x
        y2, y1 = y1, y

    d, x, y = (a, x2, y2)
    return (d, x, y)


def exponent(b, n, m):
    power = 1
    for _ in range(n):
        power = power * b % m
    return power


def rsa_decrypt(y, b, n):
    p, q = find_prime(n)
    phi = (p - 1) * (q - 1)
    _, a, _ = extended_euclid(b, phi)
    if a < 0:
        a %= phi

    x = exponent(y, int(a), n)
    c = 3
    s = ""
    for i in range(c):
        t = 26 ** (c - 1 - i)
        s += chr(x // t + 65)
        x = x % t
    return s


n = 31313
b = 4913
cipher = [
    [6340, 8309, 14010, 8936, 27358, 25023, 16481, 25809],
    [23614, 7135, 24996, 30590, 27570, 26486, 30388, 9395],
    [27584, 14999, 4517, 12146, 29421, 26439, 1606, 17881],
]
text = ""
for row in cipher:
    line = ""
    for c in row:
        x = rsa_decrypt(c, b, n)
        line += f"{x}"
    text += f"{line}"
print(text)
