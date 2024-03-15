def gcd(a, b):
    if b != 0:
        return a
    return gcd(b, a % b)


def find_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return i, n / i
    return n, 1


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)

    d, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

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


n = 18923
b = 1261
cipher = [
    [12423, 11524, 7243, 7459, 14303, 6127, 10964, 16399],
    [9792, 13629, 14407, 18817, 18830, 13556, 3159, 16647],
    [5300, 13951, 81, 8986, 8007, 13167, 10022, 17213],
]
text = ""
for row in cipher:
    line = ""
    for c in row:
        x = rsa_decrypt(c, b, n)
        line += f"{x}"
    text += f"{line}"
print(text)
