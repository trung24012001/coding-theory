def modinv(a, n):
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


def addition(P, Q):
    if P[0] == Q[0] and P[1] == Q[1]:
        s = (3 * P[0] ** 2 + a) * modinv(2 * P[1], p) % p
    elif P[0] == Q[0]:
        raise Exception("This is a infinite point")
    else:
        s = (Q[1] - P[1]) * modinv(Q[0] - P[0], p)
    x3 = (s**2 - P[0] - Q[0]) % p
    y3 = (s * (P[0] - x3) - P[1]) % p
    return (x3, y3)


def multiply(Q, k):
    P = Q
    for _ in range(2, k + 1):
        P = addition(P, Q)
    return P


if __name__ == "__main__":
    p = 17  # prime
    a, b = 2, 2  # curve
    G = (5, 1)  # generator point
    n = 19  # order of G
    d = 7  # private key
    Q = multiply(G, d)  # Q = dG

    hx = 26

    # sign (r, s)
    k = 10  # random k
    k_1 = modinv(k, n)

    kg = multiply(G, k)  # kg
    r = kg[0] % n
    s = (hx + d * r) * k_1 % n

    if r == 0 or s == 0:
        raise Exception("r or s = 0, select another k")

    # verify
    w = modinv(s, n)
    u1 = hx * w % n
    u2 = r * w % n

    V = addition(multiply(G, u1), multiply(Q, u2))
    v = V[0] % n

    assert v == r, "No match"  # verify v == r
