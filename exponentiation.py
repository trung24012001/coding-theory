def exponentiation(b, n, m):
    res = 1
    power = b % m
    while n > 0:
        # n is odd
        if (n & 1) != 0:
            res = res * power % m
        n = n >> 1  # n = n / 2
        power = (power * power) % m
        return res

    return res


print(exponentiation(23121312123123, 21312323123, 23123123123))
