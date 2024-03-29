import math
import prime
import utils


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


def isPrime(n):
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


# p = prime.get_prime(15)
# print(p)
# print(isPrime(p))

# x = find_primitive(p)
# print(x)
# print(find_all_primitive(x, 919))

for p in range(9999, 100000, 2):
    ismatch = False
    for i in range(1, 200):
        if choose(p, i) % p != 0 and not prime.is_prime(p):
            print(p, i)
            ismatch = True
            break
    if not ismatch and not prime.is_prime(p):
        print(p, "NOT MATCH")
