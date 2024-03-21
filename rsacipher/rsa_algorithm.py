import prime
import utils


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int) -> tuple:
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


def inverse(x: int, n: int) -> int:
    (d, inv, _) = extended_gcd(x, n)
    if d != 1:
        raise Exception("NotRelativePrimeError: {x}, {n}, {d}")
    return inv


def find_p_q(nbits: int) -> tuple:
    halfbits = nbits // 2
    shift = halfbits // 16
    pbits = halfbits + shift
    qbits = halfbits - shift
    p = prime.get_prime(pbits)
    q = prime.get_prime(qbits)

    def is_acceptable(p, q):
        if p == q:
            return False
        n = p * q
        return n.bit_length() == nbits

    change_p = False
    while not is_acceptable(p, q):
        if change_p:
            p = prime.get_prime(pbits)
        else:
            q = prime.get_prime(qbits)
        change_p = not change_p

    return p, q


def genkeys(nbits: int, exponent: int) -> tuple:
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


def newkeys(nbits: int, exponent: int = 127) -> tuple:
    p, q, e, d = genkeys(nbits, exponent)
    n = p * q

    return (PublicKey(n, e), PrivateKey(n, e, d, p, q))


def encrypt_int(message: int, e: int, n: int) -> int:
    return utils.exp(message, e, n)


def decrypt_int(message: int, d: int, n: int) -> int:
    return utils.exp(message, d, n)


def encrypt(message: bytes, pub_key: PublicKey) -> bytes:
    msglength = len(message) * 8
    if msglength > pub_key.n.bit_length():
        raise Exception("Message too large")

    payload = utils.bytes2int(message)
    encrypted = encrypt_int(payload, pub_key.e, pub_key.n)

    return utils.int2bytes(encrypted)


def decrypt(crypto: bytes, priv_key: PrivateKey) -> bytes:
    payload = utils.bytes2int(crypto)
    decrypted = decrypt_int(payload, priv_key.d, priv_key.n)

    return utils.int2bytes(decrypted)
