def exponent(b, n, m):
    power = b % m
    for _ in range(n - 1):
        power = power * b % m
    return power


print(exponent(989, 931, 3599))
