def decrypt(c, n, e):
    it = 1
    ck = c
    while True:
        ck = pow(ck, e, n)
        if ck == c:
            break
        it += 1

    return it


it = decrypt(2608, 18721, 25)
print(it)
