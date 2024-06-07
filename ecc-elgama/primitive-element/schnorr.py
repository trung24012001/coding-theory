import prime
import random

"""
https://en.wikipedia.org/wiki/Schnorr_group
https://crypto.stackexchange.com/questions/54254/how-to-find-a-generator-g-for-a-large-prime-p
https://crypto.stackexchange.com/questions/72811/the-definition-and-origin-of-schnorr-groups


p = qr + 1 (p,q: prime)
h^r != 1 mod p
g = h^r mod p
g is a generator of subgroup Zp* of order q
ordp(g) = q
"""


def get_prime_general_schnorr(nbits):
    """
    return (prime, order, generator)
    """
    while True:
        q = prime.get_prime(nbits)
        r = random.randint(3, 20)
        p = q * r + 1

        if prime.is_prime(p) == False:
            continue

        g = 1
        while g % p == 1:
            h = random.randint(2, p)
            g = pow(h, r, p)
            if g % p != 1:
                return (p, q, g)  # generates a subgroup of order q


"""
p = 2q + 1 (safe prime)

(a/p) = a^(p-1/2) mod p (Jacobi/Legendre symbol)

a^(p-1/2) = 1 mod p 
a is a quadratic residue (Euler's criterion)

if p = +- 1 mod 8 then 2^q  = 1 mod p  => 2 is a generator of subgroup Zp* of order q
if p = +- 3 mod 8 then 2^q != 1 mod p  => 2 is a primitive of Zp*
"""


def get_prime_specific_schnorr(nbits):
    """
    return (prime, order, generator)
    """
    g = 2
    while True:
        q = prime.get_prime(nbits)
        p = 2 * q + 1

        if prime.is_prime(p) == False:
            continue

        # Jacobi symbol
        res = p % 8
        if res == 1 or res == 7:
            return (p, q, g)  # generates a subgroup of order q
        if res == 3 or res == 5:
            return (p, p - 1, g)  # primitive


print(get_prime_specific_schnorr(1024))
