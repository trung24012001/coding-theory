import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = [random.choice(characters) for _ in range(length)]

    return "".join(password)


day = 1

accounts = "username,password\n"
for i in range(1, 39):
    i = "0" + str(i) if i < 10 else str(i)
    username = "u05" + i
    password = generate_password(12)
    accounts += username + "," + password + "\n"

with open(f"output/accounts{day}.csv", "w") as f:
    f.write(accounts)
    print(f"Generated output/accounts{day}.csv")
