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


p = 17  # prime
a, b = 2, 2  # curve
G = (5, 1)  # generate point
n = 19  # order of G


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


d = 9  # private key
hx = 26

# sign
Q = multiply(G, d)  # Q = dG
r = Q[0] % n
if r == 0:
    raise Exception("r = 0, select another d")
k = 13  # select k
k_1 = modinv(k, n)
s = (hx + d * r) * k_1 % n
if s == 0:
    raise Exception("s = 0, select another k")

# sign (r, s)

# verify
w = modinv(s, n)
u1 = hx * w % n
u2 = r * w % n

V = addition(multiply(G, u1), multiply(Q, u2))

print(V, Q)

assert V[0] == r, "No match"  # verify v == r
