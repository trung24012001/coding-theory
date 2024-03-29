# import math
# import array as arr


# def perfectPower(n):
#     """Checks if number is a power of another integer,
#     if it returns true, then it is composite.
#     """
#     for b in range(2, int(math.log2(n)) + 1):
#         a = n ** (1 / b)
#         if a - int(a) == 0:
#             return True
#     return False


# def findR(n):
#     """Find smallest r such that the order of n mod r > log2(n)^2."""
#     maxK = math.log2(n) ** 2
#     maxR = math.log2(n) ** 5
#     nexR = True
#     r = 1
#     while nexR == True:
#         r += 1
#         nexR = False
#         k = 0
#         while k <= maxK and nexR == False:
#             k = k + 1
#             if fastMod(n, k, r) == 0 or fastMod(n, k, r) == 1:
#                 nexR = True
#     return r


# def fastMod(base, power, n):
#     """Implement fast modular exponentiation."""
#     r = 1
#     while power > 0:
#         if power % 2 == 1:
#             r = r * base % n
#         base = base**2 % n
#         power = power // 2
#     return r


# def fastPoly(base, power, r):
#     """Use fast modular exponentiation for polynomials to raise them to a big power."""
#     x = arr.array(
#         "d",
#         [],
#     )
#     a = base[0]

#     for i in range(len(base)):
#         x.append(0)
#     x[(0)] = 1
#     n = power

#     while power > 0:
#         if power % 2 == 1:
#             x = multi(x, base, n, r)
#         base = multi(base, base, n, r)
#         power = power // 2

#     x[(0)] = x[(0)] - a
#     x[(n % r)] = x[(n % r)] - 1
#     return x


# def multi(a, b, n, r):
#     """Function used by fastPoly to multiply two polynomials together."""
#     x = arr.array("d", [])
#     for i in range(len(a) + len(b) - 1):
#         x.append(0)
#     for i in range(len(a)):
#         for j in range(len(b)):
#             x[(i + j) % r] += a[(i)] * b[(j)]
#             x[(i + j) % r] = x[(i + j) % r] % n
#     for i in range(r, len(x)):
#         x = x[:-1]
#     return x


# def eulerPhi(r):
#     """Implement the euler phi function"""
#     x = 0
#     for i in range(1, r + 1):
#         if math.gcd(r, i) == 1:
#             x += 1
#     return x


# def aks(n):
#     """The main AKS algorithm"""
#     if perfectPower(n) == True:  # step 1
#         return "Composite"

#     r = findR(n)  # step 2

#     for a in range(2, min(r, n)):  # step 3
#         if math.gcd(a, n) > 1:
#             return "Composite"

#     if n <= r:  # step 4
#         return "Prime"

#     x = arr.array(
#         "l",
#         [],
#     )  # step 5
#     for a in range(1, math.floor((eulerPhi(r)) ** (1 / 2) * math.log2(n))):
#         x = fastPoly(arr.array("l", [a, 1]), n, r)
#         if any(x):
#             return "Composite"
#     return "Prime"

#!/usr/bin/python3

import math
import multiprocessing
from sys import argv


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            amount += 1
    return amount


def step1(n):
    for b in range(2, math.floor(math.log2(n) + 1)):
        a = n ** (1 / b)
        if a.is_integer():
            return False
    return True


def step2(n):
    mk = math.floor(math.log2(n) ** 2)
    nexr = True
    r = 1
    while nexr:
        r += 1
        nexr = False
        k = 0
        while k <= mk and not nexr:
            k = k + 1
            if pow(n, k, r) in (0, 1):
                nexr = True
    return r


def step3(n, r):
    for a in range(1, r + 1):
        if 1 < math.gcd(a, n) < n:
            return False
    return True


def step4(n, r):
    if n <= r:
        print(f"{n} - prime. Step 4")
        return True
    return False


def step5(n, r):
    max = math.sqrt(phi(r))
    rn = math.floor(max * math.log2(n))
    if rn > n:
        rn = n
    threads = []
    ran = rn / 8
    ran = math.floor(ran)
    if ran == 0:
        ran = 1

    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    for a in range(0, rn, ran):
        process = multiprocessing.Process(
            target=step5_check, args=(n, a, a + ran, return_dict)
        )
        process.start()
        threads.append(process)
    for i in threads:
        i.join()

    if False not in return_dict.values():
        print(f"{n} - prime. Step 5")
        return True
    return False


def step5_check(n, bot, top, return_dict):
    x = bot / (top - bot)
    if bot == 0:
        bot = 1
    for a in range(bot, top):
        b = pow(a, n, n)
        if b - a != 0:
            return_dict[x] = False
            return False
    return_dict[x] = True
    return True


def aks(n):
    # if step1(n):
    if True:
        r = step2(n)
        return step3(n, r) and (step4(n, r) or step5(n, r))
    return False


def trivial(n):
    if n == 2:
        return True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    for i in range(int(argv[1]), int(argv[2])):
        assert aks(i) == trivial(i)


# if __name__ == "__main__":
#     # main()
#     print(aks(311523237))
