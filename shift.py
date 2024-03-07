encode = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
decode = ""
maxK = 26

for k in range(maxK):
    decode = ""
    for s in encode:
        dc = (ord(s) - 65 - k) % maxK
        if dc < 0:
            dc = maxK - dc
        decode += chr(dc + 65)
    print(k, decode)
