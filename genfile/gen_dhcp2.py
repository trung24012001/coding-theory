import csv

# host Class305-GV{
#         option host-name "Class305-GV";
#         hardware ethernet 38:60:77:8A:46:B5;
#         fixed-address 192.168.2.6;
# }
rows = []
with open("data/computers.csv", "r") as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        rows.append(row)

output = ""
for i, row in enumerate(rows):
    ip = row["ip"]
    mac = row["mac"]
    name = row["name"]

    line1 = f"host {name} " + "{\n"
    line2 = f'  option host-name "{name}";' + "\n"
    line3 = f"  hardware ethernet {mac};" + "\n"
    line4 = f"  fixed-address {ip};" + "\n}"
    output += line1 + line2 + line3 + line4 + "\n\n"

with open("output/dhcp.conf", "w", encoding="utf-8") as f:
    f.write(output)
