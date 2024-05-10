# so thang du bac 2 toi da: (p-1)/2 = 8

# Cong thuc:
# lambda = (3*x1^2 + a) / 2*y1 (P = Q)
# lambda = y2 - y1 / x2 - x1 (P != Q)
# x3 = lambda^2 - x1 - x2
# y3 = (x1 - x3)*lambda - y1

p = 127
a = 3
b = 5
point = (1, 3)  # chon diem sinh

npoints = 0
g = set()

for x in range(p):
    r = 4 * a**3 + 27 * b**2
    if r % p == 0:
        print("khong tmdk")

    y_2 = (x**3 + a * x + b) % p  # y^2 = x^3 + ax + b

    for y in range(1, p):
        if y_2 == y**2 % p:
            npoints += 1
            g.add(y_2)
            # print((x, y))

# them diem vo cuc {O}
npoints += 1

print("Tong so diem:", npoints)
print("Cac diem trong tap thang du bac 2:", len(g), g)
print("P =", point)

# (3x1^2 + a) / 2y1
ld = ((3 * point[0] ** 2 + a) * pow((2 * point[1]), p - 2, p)) % p
# lambda^2 - x2 - x1
x3 = (ld**2 - 2 * point[0]) % p
# (x1 - x3)*lambda - y1
y3 = (ld * (point[0] - x3) - point[1]) % p

cpoint = (x3, y3)
print(2, "P", cpoint)

for k in range(3, npoints):
    # (y2 - y1) / (x2 - x1)
    ld = ((cpoint[1] - point[1]) * pow((cpoint[0] - point[0]), p - 2, p)) % p
    # lambda^2 - x1 - x2
    x3 = (ld**2 - point[0] - cpoint[0]) % p
    # (x1 - x3)*lambda - y1
    y3 = (ld * (point[0] - x3) - point[1]) % p

    cpoint = (x3, y3)
    print(k, "P", cpoint)
