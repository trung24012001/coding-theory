import math
import prime
import utils


def isPrime(n):
    if n < 10:
        return n in {2, 3, 5, 7}

    if not (n & 1):
        return False

    for i in range(3, (n // 2) + 1):
        c = math.comb(n, i)
        if c == 0 or c == 1:
            continue
        if c % n != 0:
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
    print(s)

    for r in range(2, phi + 1):
        is_primitive = True
        for i in s:
            if utils.exp(r, phi // i, n) == 1:
                is_primitive = False
                break

        if is_primitive:
            return r

    return -1


def find_all_primitive(p, n):
    phi = n - 1
    prim = set()
    for i in range(2, n):
        if utils.gcd(i, phi) == 1:
            beta = utils.exp(p, i, n)
            prim.add(beta)

    return prim


p = prime.get_prime(9)
print(p)
print(isPrime(p))
# x = find_primitive(p)
# print(x)

# print(find_all_primitive(x, 919))
