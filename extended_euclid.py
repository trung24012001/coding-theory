# def extended_euclid(a, b):
#     if b == 0:
#         return (a, 1, 0)

#     d, x1, y1 = extended_euclid(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1

#     return (d, x, y)

# ax + by = d


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)

    x2, x1 = 1, 0
    y2, y1 = 0, 1
    while b > 0:
        q = a // b
        r = a % b
        x = x2 - q * x1
        y = y2 - q * y1

        a, b = b, r
        x2, x1 = x1, x
        y2, y1 = y1, y

    d, x, y = (a, x2, y2)
    return (d, x, y)


a, b = 36, 919
print(extended_euclid(a, b))
