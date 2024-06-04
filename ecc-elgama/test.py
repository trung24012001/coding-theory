from utils import modinv, decode_ascii, encode_ascii
from primitive import find_primitive
import prime


def inverse():
    a = 5
    n = 17
    inv = modinv(a, n)
    print(f"inverse of {a} mod {n} :", inv)
    print("check:", a * inv % n)


def encode():
    text = "TR"
    print(f"ascii of {text}:", encode_ascii(text))


def primit():
    n = 149
    prim = find_primitive(n)
    print(f"primitive of {n}:", prim)


def curve():
    a, b = 2, 2
    p = 17
    P = (7, 11)
    Q = (5, 1)
    if P[0] == Q[0] and P[1] == Q[1]:
        s = (3 * P[0] ** 2 + a) * modinv(2 * P[1], p) % p
    elif P[0] == Q[0]:
        print("This is a infinite point")
        return
    else:
        s = (Q[1] - P[1]) * modinv(Q[0] - P[0], p)
    x3 = (s**2 - P[0] - Q[0]) % p
    y3 = (s * (P[0] - x3) - P[1]) % p
    print("(x3, y3):", x3, y3)


# inverse()
# encode()
# primit()
# curve()

print(prime.get_prime(30))
