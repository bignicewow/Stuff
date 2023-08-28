def deep():
    x = input("What's the answer to the Great Question of Life, the Universe and Everything? ").lower().replace("-", " ")
    if x == "42" or x == "forty two":
        print("Yes")
    else:
        print("No")

deep()