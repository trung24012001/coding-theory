m = 8
encode = "TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"
decode = ""
per = {1:2, 2:4, 3:6, 4:1, 5:8, 6:3, 7:5, 8:7}

for i in range(len(encode) // m):
  s = encode[i*m:(i+1)*m]
  for j in range(1, m+1):
    dc = s[per[j]-1]
    decode += dc

print(decode, len(decode))