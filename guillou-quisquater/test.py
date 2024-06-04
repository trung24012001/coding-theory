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


# TA
p = 489133282872437279
q = 19175002942688032928599
n = p * q
b = 977920532201  # TA select prime b then public
# TA_pub = {n,b}

u = 101576  # A select private u
v = pow(modinv(u, n), b, n)  #  A calculate v (mask u) then send to TA

Ia = 23025112 % n  # TA identify A by Ia or ID(A)

d = 617341279  # select private key for rsa sign
phin = (p - 1) * (q - 1)
e = modinv(d, phin)  # public key for rsa sign
s1 = pow(Ia, d, n)
s2 = pow(v, d, n)
# assign to A: C(A) = (Ia, v, s) # s = (s1, s2)


# A

k = 187485187485  # select random
ya = pow(k, b, n)
# A send to B information (C(A), ya)

# B
# B verify (Ia, v) from s = (s1, s2)
assert pow(s1, e, n) == Ia, "Verify s1 rsa fail"
assert pow(s2, e, n) == v, "Verify s2 rsa fail"

r = 23432452343245  # B select random r then send to A
y = k * pow(u, r, n) % n  # A calculate y then send to B
yb = pow(v, r, n) * pow(y, b, n) % n  # B use y to test

assert ya == yb, "Verify A and B fail"
print("This is a real A")
