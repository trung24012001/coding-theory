import numpy as np


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_invere(n, x):
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


# print(find_invere(9987, 1844))


def find_inverse_matrix():
    mat = [[1, 11, 12], [4, 23, 2], [17, 15, 9]]
    n = 26
    determinant = np.linalg.det(mat)
    invert = np.linalg.inv(mat).T
    cofactor = invert * determinant
    print(determinant)
    print(21 * cofactor % n)


def find_bin(a):
    s = ""
    while a > 0:
        s += str(a & 1)
        a = a >> 1
    return s[::-1]


print(find_bin(83))
