import csv


rows = []
with open("data/students.template.csv", "r", encoding="utf8") as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        rows.append(row)

output = "sbd,hoten,ngaysinh,gioitinh,donvi\n"
for row in rows:
    sbd = row["sbd"]
    hoten = row["hoten"]
    ten = row["ten"]
    ngaysinh = row["ngaysinh"]
    gioitinh = row["gioitinh"]
    donvi = row["donvi"]
    output += f"{sbd},{hoten+ten},{ngaysinh},{gioitinh},{donvi}\n"

with open("data/students.csv", "w", encoding="utf-8") as f:
    f.write(output)
