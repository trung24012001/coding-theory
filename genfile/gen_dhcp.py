from jinja2 import Environment, FileSystemLoader
import csv

environment = Environment(loader=FileSystemLoader("data/"))
template = environment.get_template("00-installer-config.yaml")

rows = []
with open("data/computers.csv", "r") as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        rows.append(row)

for row in rows:
    name = row["name"]
    ip = row["ip"]
    mac = row["mac"]

    output = template.render(
        ip=ip,
    )

    filename = f"output/00-{name}-installer-config.yaml"
    with open(filename, "w") as f:
        f.write(output)
        print(f"Generated {filename}")
