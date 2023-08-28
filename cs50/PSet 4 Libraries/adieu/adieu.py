import inflect

def adieu():
    p = inflect.engine()
    namelist = []
    while True:
        try:
            namelist.append(input("Name: "))

        except KeyboardInterrupt:
            break
    formatted_list = p.join(namelist)
    print("Adieu, adieu, to", formatted_list)

adieu()