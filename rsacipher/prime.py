import math
import random
import utils


def brute_force_primality_tesing(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def fermat_primality_testing(n: int, k: int) -> bool:
    if n < 2:
        return False

    for _ in range(k):
        a = random.randrange(2, n, 1)
        if pow(a, n - 1, n) != 1:
            return False

    return True


def miller_rabin_primality_testing(n: int, k: int) -> bool:
    if n < 2:
        return False

    r = 0
    d = n - 1
    while not (d & 1):
        r += 1
        d >>= 1

    for _ in range(k):
        a = random.randrange(2, n - 1, 1)
        x = utils.exp(a, d, n)

        for _ in range(r):
            y = utils.exp(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y

        if y != 1:
            return False

    return True


def is_prime(num):
    if num < 10:
        return num in {2, 3, 5, 7}

    if not (num & 1):
        return False

    return miller_rabin_primality_testing(num, 5)


def get_prime(nbits: int) -> int:
    while True:
        num = utils.read_rand_odd_int(nbits)
        if is_prime(num):
            return num
