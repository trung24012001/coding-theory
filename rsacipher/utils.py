import os
import struct
import math


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def bytes2int(raw_bytes: bytes) -> int:
    return int.from_bytes(raw_bytes, "big", signed=False)


def int2bytes(num: int) -> bytes:
    bytes_required = max(1, math.ceil(num.bit_length() / 8))
    return num.to_bytes(bytes_required, "big")


def read_rand_odd_int(nbits: int) -> int:
    nbytes, rbits = divmod(nbits, 8)
    data = os.urandom(nbytes)
    print(data)
    if rbits > 0:
        randval = ord(os.urandom(1))
        randval >>= 8 - rbits
        print("rb", data)
        data = struct.pack("B", randval) + data
    print(data)
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
