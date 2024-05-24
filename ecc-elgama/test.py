from utils import modinv, decode_ascii, encode_ascii
from primitive import find_primitive


def inverse():
    a = 29
    n = 138
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


# inverse()
# encode()
primit()
