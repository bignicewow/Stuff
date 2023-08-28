def camel():
    name = input("camelCase: ")
    for i in name:
        if i.islower():
            print(i, end="")
        else:
            print("_", i.lower(), end="")

camel()