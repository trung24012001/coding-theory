import csv

accounts = []
with open("output/accounts1.csv", "r", encoding="utf8") as f:
    for row in csv.DictReader(f):
        accounts.append(row)


students = []
with open("data/students.template.csv", "r", encoding="utf8") as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        students.append(row)

output = ""
for row in students:
    sbd = row["sbd"]
    for account in accounts:
        taikhoan = account["username"]
        matkhau = account["password"]
        if "u" + sbd == taikhoan:
            hoten = row["hoten"]
            ten = row["ten"]
            output += f"cmsAddUser -p {matkhau} '{hoten}' '{ten}' {taikhoan}\n"

with open("output/CMSadduser.sh", "w", encoding="utf-8") as f:
    f.write(output)


# cmsAddUser -p pass 'firstname' 'lastname' username
# cmsAddParticipation -p pass -c contest_id username
