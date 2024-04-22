import math


def miller_primality_testing(n: int) -> bool:
    if n < 2:
        return False

    r = 0
    d = n - 1
    while not (d & 1):
        r += 1
        d >>= 1

    for a in range(2, min(n - 2, (2 * int(math.log(n) ** 2)))):
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

    return miller_primality_testing(num)


if __name__ == "__main__":
    p = 63881222142611097438575479816170835840118478665532904251413402882253972664723
    print(p, len(str(p)))
    print(is_prime(p))
