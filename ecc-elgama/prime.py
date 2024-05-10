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
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
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
