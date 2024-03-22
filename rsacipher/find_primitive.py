import math
import prime
import utils


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def find_prime_factors(s: set, n: int) -> None:
    while n % 2 == 0:
        s.add(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            s.add(i)
            n //= i

    if n > 2:
        s.add(n)


def find_primitive(n: int) -> int:
    if not prime.is_prime(n):
        return -1

    s = set()
    phi = n - 1

    find_prime_factors(s, phi)

    for r in range(2, phi + 1):
        is_primitive = True
        for i in s:
            if utils.exp(r, phi // i, n) == 1:
                is_primitive = False
                break

        if is_primitive:
            return r

    return -1


x = find_primitive(prime.get_prime(64))
print(x)
