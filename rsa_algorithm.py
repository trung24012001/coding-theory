import os, math, struct
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    oa, ob = a, b
    x2, x1 = 1, 0
    y2, y1 = 0, 1
    while b > 0:
        q = a // b
        x = x2 - q * x1
        y = y2 - q * y1

        a, b = b, a % b
        x2, x1 = x1, x
        y2, y1 = y1, y
    if x2 < 0:
        x2 += ob
    if y2 < 0:
        y2 += oa
    return (a, x2, y2)


def inverse(x, n):
    (d, inv, _) = extended_gcd(x, n)
    if d != 1:
        raise Exception("NotRelativePrimeError: {x}, {n}, {d}")
    return inv


def exp(b, n, m):
    res = 1
    power = b % m
    while n > 0:
        # n is odd
        if n & 1:
            res = res * power % m
        n = n >> 1  # n = n / 2
        power = (power * power) % m

    return res


def bytes2int(raw_bytes: bytes) -> int:
    return int.from_bytes(raw_bytes, "big", signed=False)


def int2bytes(num: int) -> bytes:
    bytes_required = max(1, math.ceil(num.bit_length() / 8))
    return num.to_bytes(bytes_required, "big")


def read_rand_odd_int(nbits):
    nbytes, rbits = divmod(nbits, 8)
    data = os.urandom(nbytes)

    if rbits > 0:
        randval = ord(os.urandom(1))
        randval >>= 8 - rbits
        data += struct.pack("B", randval)

    value = bytes2int(data)
    value |= 1 << (nbits - 1)

    return value | 1


def brute_force_primality_tesing(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


def fermat_primality_testing(num, k):
    for _ in range(k):
        a = random.randrange(2, num, 1)
        if pow(a, num - 1, num) != 1:
            return False
    return True


def is_prime(num):
    if num < 10:
        return num in {2, 3, 5, 7}

    if not (num & 1):
        return False

    return fermat_primality_testing(num, 5)


def get_prime(nbits):
    while True:
        num = read_rand_odd_int(nbits)
        if is_prime(num):
            return num


def find_p_q(nbits):
    halfbits = nbits // 2
    shift = halfbits // 16
    pbits = halfbits + shift
    qbits = halfbits - shift
    p = get_prime(pbits)
    q = get_prime(qbits)

    def is_acceptable(p, q):
        if p == q:
            return False
        n = p * q
        return n.bit_length() == nbits

    change_p = False
    while not is_acceptable(p, q):
        if change_p:
            p = get_prime(pbits)
        else:
            q = get_prime(qbits)
        change_p = not change_p

    return p, q


def genkeys(nbits, exponent):
    if nbits < 8:
        raise Exception("Key too small")

    p, q = find_p_q(nbits)
    phi_n = (p - 1) * (q - 1)
    d = inverse(exponent, phi_n)

    return p, q, exponent, d


class PublicKey:
    def __init__(self, n, e):
        self.n = n
        self.e = e


class PrivateKey:
    def __init__(self, n, e, d, p, q):
        self.n = n
        self.e = e
        self.d = d
        self.p = p
        self.q = q


def newkeys(nbits, exponent=127):
    p, q, e, d = genkeys(nbits, exponent)
    n = p * q

    return (PublicKey(n, e), PrivateKey(n, e, d, p, q))


def encrypt_int(message: int, e: int, n: int) -> int:
    return exp(message, e, n)


def decrypt_int(message: int, d: int, n: int) -> int:
    return exp(message, d, n)


def encrypt(message: bytes, pub_key: PublicKey) -> bytes:
    msglength = len(message) * 8
    if msglength > pub_key.n.bit_length():
        raise Exception("Message too large")

    payload = bytes2int(message)
    encrypted = encrypt_int(payload, pub_key.e, pub_key.n)

    return int2bytes(encrypted)


def decrypt(crypto: bytes, priv_key: PrivateKey) -> bytes:
    payload = bytes2int(crypto)
    decrypted = decrypt_int(payload, priv_key.d, priv_key.n)

    return int2bytes(decrypted)
