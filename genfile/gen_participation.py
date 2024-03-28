import csv


day = 3

accounts = []
with open(f"output/accounts{day}.csv", "r", encoding="utf8") as f:
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
            output += f"cmsAddParticipation -p {matkhau} -c {day} {taikhoan}\n"

with open(f"output/CMSparticipation{day}.sh", "w", encoding="utf-8") as f:
    f.write(output)


# cmsAddUser -p pass 'firstname' 'lastname' username
# cmsAddParticipation -p pass -c contest_id username
