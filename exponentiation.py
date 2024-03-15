def exponent(b, n, m):
    power = 1
    for _ in range(n):
        power = power * b % m
    return power


print(exponent(2, 3, 5))
