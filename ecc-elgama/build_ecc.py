import prime
import math
import random
import numpy as np
from utils import modinv


def ec_add(a, b, Acurve, Pcurve):  # Elliptic curve addition
    if a[0] == b[0] and a[1] == b[1]:
        Lam = ((3 * a[0] * a[0] + Acurve) * modinv((2 * a[1]), Pcurve)) % Pcurve
    elif a[0] == b[0]:
        return (np.inf, np.inf)
    else:
        Lam = ((b[1] - a[1]) * modinv(b[0] - a[0], Pcurve)) % Pcurve
    x = (Lam * Lam - a[0] - b[0]) % Pcurve
    y = (Lam * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def ec_double(a, Acurve, Pcurve):  # Point doubling, invented for EC
    Lam = ((3 * a[0] * a[0] + Acurve) * modinv((2 * a[1]), Pcurve)) % Pcurve
    x = (Lam * Lam - 2 * a[0]) % Pcurve
    y = (Lam * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def ec_multiply(
    GenPoint, ScalarHex, Acurve, Pcurve
):  # Double & add. Not true multiplication
    ScalarBin = str(bin(ScalarHex))[2:]
    Q = GenPoint
    for i in range(1, len(ScalarBin)):  #  EC multiplication.
        Q = ec_double(Q, Acurve, Pcurve)
        if ScalarBin[i] == "1":
            Q = ec_add(Q, GenPoint, Acurve, Pcurve)
            if Q[0] == np.inf:
                return Q
    return Q


def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def find_order(G, Pcurve):
    for o in range(
        Pcurve + 1 - 2 * int(math.sqrt(Pcurve)), Pcurve + 1 + 2 * int(math.sqrt(Pcurve))
    ):
        try:
            ec_multiply(G, o)
        except:
            return o
    return None


def get_prime_ecc(nbits):
    """
    return (p, a, b, order, g)
    """
    while True:
        p = prime.get_prime(nbits)
        a = random.randint(2, 20)
        b = random.randint(2, 20)
        if (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p == 0:
            continue

        x, y = 0, 0
        while y == 0:
            x = random.randint(1, 20)
            y2 = x**3 + a * x + b
            try:
                y = tonelli(y2, p)
            except:
                y = 0

        g = (x, y)
        while True:
            q = prime.get_prime(nbits)
            M = ec_multiply(g, q - 1, a, p)
            N = ec_multiply(g, q, a, p)

            if M[0] != np.inf and N[0] == np.inf:
                print(M, N)
                return (p, a, b, q, g)


# Elliptic curve: y^2 = x^3 + Acurve * x + Bcurve

nbits = 256
print(get_prime_ecc(nbits))

# Pcurve = 2473
# n = 935
# Acurve = 15
# Bcurve = 3
# Gx = 14
# Gy = 22
# GPoint = (Gx, Gy)
# print(ec_multiply(GPoint, n, Acurve, Pcurve))

# print("nbits:", nbits)
# print("P:", p)
# print("(a, b):", (Acurve, Bcurve))
# print("G:", GPoint)
