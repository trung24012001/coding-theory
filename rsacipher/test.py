import prime


if __name__ == "__main__":
    from aks_algo import aks

    p = prime.get_prime(64)
    print(len(str(p)))
    print(aks(p))

    # x = find_primitive(p)
    # print(x)
    # print(find_all_primitive(x, 919))
