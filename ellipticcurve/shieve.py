import random


def double(x, y, a, p):
    lambd = (((3 * x**2) % p + a) * pow(2 * y, -1, p)) % p
    newx = (lambd**2 - 2 * x) % p
    newy = (-lambd * newx + lambd * x - y) % p
    return (newx, newy)


def add_points(xq, yq, xp, yp, p, a=0):
    if xq == yq == None:
        return xp, yp
    if xp == yp == None:
        return xq, yq
    if xq == xp and yq == yp:
        return double(xq, yq, a, p)
    elif xq == xp:
        return None, None

    lambd = ((yq - yp) * pow((xq - xp), -1, p)) % p
    xr = (lambd**2 - xp - xq) % p
    yr = (lambd * (xp - xr) - yp) % p
    return xr, yr


def sieve(upper):
    result = []
    prime = [True for i in range(upper)]
    p = 2
    while p << 2 <= upper:
        if prime[p]:
            for i in range(2 * p, upper, p):
                prime[i] = False
        p += 1
    for p in range(upper - 1, 0, -1):
        if prime[p]:
            result.append(p)
    return result[::-1][1:]


primes = sieve(200)
found = {}
# print(primes)
print("Start")
while True:
    Z = 127
    a, b = random.randrange(1, Z), random.randrange(1, Z)
    a, b = 3, 5
    print(f"Trying a = {a}, b = {b}")

    if pow(4 * a**3 + 27 * b**2, 1, Z) == 0:
        continue
    mapping = {}
    for i in range(Z):
        root = pow(i, 2, Z)
        if root in mapping:
            mapping[root].append(i)
        else:
            mapping[root] = [i]
    count = 1
    for x in range(0, Z):
        y = pow(x**3 + a * x + b, 1, Z)
        if (y) in mapping:
            # print(x, mapping[y])
            if x in found:
                found[x].append(mapping[y])
            else:
                found[x] = mapping[y]

            count += len(mapping[y])
        else:
            # print(x, "--")
            pass

    # print("Total ", count)

    if count in primes:
        print(count)
        break

print(f"Found a = {a}, b = {b}")

# print(found)
print("-" * 100)

x, y = 1, 3

points = [(x, y)]
next_x, next_y = x, y
print(1, "P", points)
for i in range(2, count + 1):
    # repeatedly add G to the next point to generate all the elements
    next_x, next_y = add_points(next_x, next_y, x, y, Z, a=a)
    print(i, "P", [next_x, next_y])
    points.append((next_x, next_y))
