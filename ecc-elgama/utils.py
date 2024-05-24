import os
import struct
import math


def bytes2int(raw_bytes: bytes) -> int:
    return int.from_bytes(raw_bytes, "big", signed=False)


def int2bytes(num: int) -> bytes:
    bytes_required = max(1, math.ceil(num.bit_length() / 8))
    return num.to_bytes(bytes_required, "big")


def read_rand_odd_int(nbits: int) -> int:
    nbytes, rbits = divmod(nbits, 8)
    data = os.urandom(nbytes)
    if rbits > 0:
        randval = ord(os.urandom(1))
        randval >>= 8 - rbits
        data = struct.pack("B", randval) + data
    value = bytes2int(data)
    value |= 1 << (nbits - 1)

    return value | 1


def exp(b: int, n: int, m: int) -> int:
    res = 1
    power = b % m
    while n > 0:
        # n is odd
        if n & 1:
            res = res * power % m
        n = n >> 1  # n = n / 2
        power = (power * power) % m

    return res


# Euclidean
def gcd(a: int, b: int):
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


# encode ascii
def encode_ascii(x):
    n = len(x)
    s = 0
    while n > 0:
        s += (ord(x[::-1][n - 1]) - 65) * 26 ** (n - 1)
        n -= 1
    return s


# decode ascii
def decode_ascii(s):
    x = ""
    while s > 0:
        s, r = divmod(s, 26)
        x += chr(r + 65)
    return x[::-1]
