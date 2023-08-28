def camel():
    name = input("camelCase: ")
    output = ""
    for i in name:
        if i.islower():
            output += i
        else:
            output += "_"
            output += i
    print(output.lower())

camel()
