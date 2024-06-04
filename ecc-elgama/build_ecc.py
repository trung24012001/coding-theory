import prime
import math
from utils import modinv


def ECadd(a, b):  # Elliptic curve addition
    if a[0] == b[0]:
        raise Exception("This is an infinite point")
    LamAdd = ((b[1] - a[1]) * modinv(b[0] - a[0], Pcurve)) % Pcurve
    x = (LamAdd * LamAdd - a[0] - b[0]) % Pcurve
    y = (LamAdd * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def ECdouble(a):  # Point doubling, invented for EC
    Lam = ((3 * a[0] * a[0] + Acurve) * modinv((2 * a[1]), Pcurve)) % Pcurve
    x = (Lam * Lam - 2 * a[0]) % Pcurve
    y = (Lam * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def EccMultiply(GenPoint, ScalarHex):  # Double & add. Not true multiplication
    ScalarBin = str(bin(ScalarHex))[2:]
    Q = GenPoint
    for i in range(1, len(ScalarBin)):  #  EC multiplication.
        Q = ECdouble(Q)
        if ScalarBin[i] == "1":
            Q = ECadd(Q, GenPoint)
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


def find_order(G):
    for i in range(
        Pcurve + 1 - 2 * int(math.sqrt(Pcurve)), Pcurve + 1 + 2 * int(math.sqrt(Pcurve))
    ):
        try:
            EccMultiply(G, i)
        except:
            print(i)
            return i
    return 1


nbits = 256
Pcurve = prime.get_prime(nbits)

# Elliptic curve: y^2 = x^3 + Acurve * x + Bcurve
Acurve = 3
Bcurve = 7
# Generator Point
Gx = prime.get_prime(nbits // 2)
Gy2 = Gx**3 + Acurve * Gx + Bcurve
Gy = tonelli(Gy2, Pcurve)
GPoint = (Gx, Gy)
# Order of G
n = find_order(GPoint)

print("nbits:", nbits)
print("P:", Pcurve)
print("(a, b):", (Acurve, Bcurve))
print("G:", GPoint)
print("order of G:", n)
