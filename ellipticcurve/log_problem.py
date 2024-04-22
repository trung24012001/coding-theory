def find_log(a, b, p):
    x = 1
    for k in range(1, p):
        x = x * a % p
        if x == b:
            return k
    return -1


if __name__ == "__main__":
    print(find_log(106, 12375, 24691))  # log106(12375) mod 24691
    print(find_log(6, 248388, 458009))  # log6(248388) mod 458009
