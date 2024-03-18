def exponentiation(b, n, m):
    res = 1
    power = b % m
    while n > 0:
        # n is odd
        if n & 1:
            res = res * power % m
        n = n >> 1  # n = n / 2
        power = (power * power) % m

    return res


print(exponentiation(6308, 2395, 34199))
