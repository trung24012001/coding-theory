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


# Elgamal
# pub(p, alpha, beta)
# priv(p, a)

# Sign
# sig(x, k) = (y, s)
# ver(x)

p = 139  # prime
alpha = 2  # find primitive
a = 29  # random private key
beta = pow(alpha, a, p)

x = 185  # message
k = 41  # random
k_1 = modinv(k, p - 1)  # k^-1 mod (p - 1)
y = pow(alpha, k, p)  # y = alpha^k mod p
s = ((x - a * y) * k_1) % (p - 1)  # (h(x) - ay)*k^-1 mod (p - 1)

print("message:", x)
print("p:", p)
print("alpha:", alpha)
print("a:", a)
print("beta:", beta)
print("k, k inverse:", k, k_1)
print("signature (y, s):", y, s)

# Verify
t1 = pow(beta, y, p) * pow(y, s, p) % p
t2 = pow(alpha, x, p)
assert t1 == t2, "No match"  # beta^y * y^s mod p == alpha^x
