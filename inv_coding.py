n = 9987
x = 1844


# def gcd(a, b):
#     if b != 0:
#         return a
#     return gcd(b, a % b)


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


for i in range(1, n):
    if gcd(i, n) != 1:
        continue
    for j in range(1, n):
        if i * j % n == 1:
            if x == None:
                print(i, j)
            elif x == i:
                print(i, j)
            break
