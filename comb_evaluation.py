# from scipy.misc import comb
import random, time
import math


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


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f"{f.__name__} function took {(time2-time1)*1000.0} ms")
        return ret

    return wrap


# @timing
def test_func(combination_func, nk):
    for n, k in nk:
        combination_func(n, k)


nk = []
for _ in range(1000):
    n = int(random.random() * 10000)
    k = random.randint(0, n)
    # nk.append((n, k))
    if math.comb(n, k) - choose(n, k) != 0:
        print(n, k)
# test_func(math.comb, nk)
# test_func(choose, nk)
