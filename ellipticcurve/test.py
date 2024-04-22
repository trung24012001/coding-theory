# so thang du bac 2 toi da: (p-1)/2 = 8

# Cong thuc:
# lambda = (3*x1^2 + a) / 2*y1 (P = Q)
# lambda = y2 - y1 / x2 - x1 (P != Q)
# x3 = lambda^2 - x1 - x2
# y3 = (x1 - x3)*lambda - y1

numps = 0
g = set()
p = 127
a = 3
b = 5
point = (1, 3)  # chon diem sinh

for x in range(p):
    r = 4 * a**3 + 27 * b**2
    if r % p == 0:
        print("khong tmdk")

    y_2 = (x**3 + a * x + b) % p  # y^2 = x^3 + ax + b

    for y in range(1, p):
        if y_2 == y**2 % p:
            numps += 1
            g.add(y_2)
            # print((x, y))

numps += 1  # them diem vo cuc {O}
print("Tong so diem:", numps)
print("Cac diem trong tap thang du bac 2:", len(g), g)
print("P =", point)
lamd = (
    (3 * point[0] ** 2 + a) * pow((2 * point[1]), p - 2, p)
) % p  # (3x1^2 + a) / 2y1
x3 = (lamd**2 - 2 * point[0]) % p  # lambda^2 - x2 - x1
y3 = (lamd * (point[0] - x3) - point[1]) % p  # (x1 - x3)*lambda - y1
cumpoint = (x3, y3)
print(2, "P", cumpoint)
for k in range(3, numps):
    lamd = (
        (cumpoint[1] - point[1]) * pow((cumpoint[0] - point[0]), p - 2, p)
    ) % p  # (y2 - y1) / (x2 - x1)
    x3 = (lamd**2 - point[0] - cumpoint[0]) % p  # lambda^2 - x1 - x2
    y3 = (lamd * (point[0] - x3) - point[1]) % p  # (x1 - x3)*lambda - y1
    cumpoint = (x3, y3)
    print(k, "P", cumpoint)
