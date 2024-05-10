# so thang du bac 2 toi da: (p-1)/2 = 8

# Cong thuc:
# y^2 = x^3 + ax + b
# lambda = (3*x1^2 + a) / 2*y1 (P = Q)
# lambda = y2 - y1 / x2 - x1 (P != Q)
# x3 = lambda^2 - x1 - x2
# y3 = (x1 - x3)*lambda - y1


p_curve = 127
a_curve = 4
b_curve = 7
point = (1, 3)  # select generate point


r = (4 * a_curve**3 + 27 * b_curve**2) % p_curve
assert r != 0, "4a^3 + 27b^2 = 0"


def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def countpoints():
    npoints = 0
    for x in range(p_curve):
        # y^2 = x^3 + ax + b
        y_2 = (x**3 + a_curve * x + b_curve) % p_curve
        if legendre(y_2, p_curve) != 1:
            continue
        npoints += 2
    #  add inf point {O}
    npoints += 1
    return npoints


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


# Elliptic curve addition
def ecc_add(a, b):
    if a[0] == b[0]:
        ld = ((3 * a[0] * a[0] + a_curve) * modinv((2 * a[1]), p_curve)) % p_curve
    else:
        ld = ((b[1] - a[1]) * modinv(b[0] - a[0], p_curve)) % p_curve
    x = (ld * ld - a[0] - b[0]) % p_curve
    y = (ld * (a[0] - x) - a[1]) % p_curve
    return (x, y)


# Point doubling,invented for EC
def ecc_double(a):
    ld = ((3 * a[0] * a[0] + a_curve) * modinv((2 * a[1]), p_curve)) % p_curve
    x = (ld * ld - 2 * a[0]) % p_curve
    y = (ld * (a[0] - x) - a[1]) % p_curve
    return (x, y)


# Double & add. Not true multiplication
def ecc_multiply(gpoint, scalar):
    Q = gpoint

    scalarbin = str(bin(scalar))[2:]
    # EC multiplication.
    for i in range(1, len(scalarbin)):
        Q = ecc_double(Q)
        assert Q[1] != 0, f"point: {Q}, scalar: {scalar} has y = 0"
        if scalarbin[i] == "1":
            Q = ecc_add(Q, gpoint)
            assert Q[1] != 0, f"point: {Q}, scalar: {scalar} has y = 0"

    return Q


if __name__ == "__main__":
    npoints = countpoints()
    print(f"points including inf: {npoints}")
    for k in range(1, npoints):
        print(k, "P", ecc_multiply(point, k))
