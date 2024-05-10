import random

nbits = 6

# Pcurve = prime.get_prime(nbits)  # The proven prime
Pcurve = 127

# Elliptic curve: y^2 = x^3 + Acurve * x + Bcurve
Acurve = 3
Bcurve = 5

# Generator Point
Gx = 1
Gy = 3
GPoint = (Gx, Gy)

k = random.getrandbits(nbits)


# def modinv(a, n=Pcurve):  # Extended Euclidean Algorithm/'division' in elliptic curves
#     lm, hm = 1, 0
#     low, high = a % n, n
#     while low > 1:
#         ratio = high / low
#         nm, new = hm - lm * ratio, high - low * ratio
#         lm, low, hm, high = nm, new, lm, low
#     return lm % n


def modinv(a, n=Pcurve):
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


def ECadd(a, b):  # Elliptic curve addition
    LamAdd = ((b[1] - a[1]) * modinv(b[0] - a[0], Pcurve)) % Pcurve
    x = (LamAdd * LamAdd - a[0] - b[0]) % Pcurve
    y = (LamAdd * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def ECdouble(a):  # Point doubling,invented for EC
    Lam = ((3 * a[0] * a[0] + Acurve) * modinv((2 * a[1]), Pcurve)) % Pcurve
    x = (Lam * Lam - 2 * a[0]) % Pcurve
    y = (Lam * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def EccMultiply(GenPoint, ScalarHex):  # Double & add. Not true multiplication

    if ScalarHex == 0:
        raise Exception("Invalid Scalar/Private Key")

    ScalarBin = str(bin(ScalarHex))[2:]
    Q = GenPoint

    for i in range(1, len(ScalarBin)):  #  EC multiplication.
        Q = ECdouble(Q)
        if ScalarBin[i] == "1":
            Q = ECadd(Q, GenPoint)
    return Q


privKey = random.getrandbits(nbits)


def gen_pubKey():
    PublicKey = EccMultiply(GPoint, privKey)
    return PublicKey


def encryption(Public_Key, msg):
    C1 = EccMultiply(GPoint, k)
    C2 = EccMultiply(Public_Key, k)[0] + int(msg)

    return (C1, C2)


def decryption(C1, C2, private_Key):
    solution = C2 - EccMultiply(C1, private_Key)[0]
    return solution


def encode(msg):
    string_ascii = ""
    for i in msg:
        string_ascii += str(ord(i))

    return string_ascii


def decode(newascii_string):
    pack = ""
    i = 0
    dec_message = ""
    while i < len(str(newascii_string)):

        pack = newascii_string[i : i + 3]
        dec_message += chr(pack)
        i = i + 3

    return dec_message


if __name__ == "__main__":

    message = "12"

    (C1, C2) = encryption(gen_pubKey(), message)

    decrypted_string = decryption(C1, C2, privKey)

    print("Cipher Text : ", C1, C2)
    print("-----")
    print(" **Original Message** ")
    print(decrypted_string)
