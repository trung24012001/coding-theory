import math
import prime


def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def coefcheck(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        n = n - 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return (ntok % ktok) == 0

    return True


def isprime(n):
    if n < 10:
        return n in {2, 3, 5, 7}

    if not (n & 1):
        return False

    for i in range(3, (n // 2) + 1):
        if not coefcheck(n, i):
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
            if pow(r, phi // i, n) == 1:
                is_primitive = False
                break

        if is_primitive:
            return r

    return -1


def find_all_primitive(p, n):
    phi = n - 1
    prim = set()
    for i in range(2, n):
        if math.gcd(i, phi) == 1:
            beta = pow(p, i, n)
            prim.add(beta)

    return prim
