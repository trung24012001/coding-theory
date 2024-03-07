n = 26

def gcd(a, b):
  if not b:
    return a
  return gcd(b, a%b)

for i in range(1, n):
  if gcd(i, n) != 1:
    continue
  for j in range(1, n):
    if i * j % n == 1:
      print(i, j)
      break