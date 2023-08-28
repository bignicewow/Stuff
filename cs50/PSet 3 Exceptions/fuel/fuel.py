def fuel_gauge():
    while True:
        fuel = input("Fraction: ")
        x, y = fuel.split("/")
        try:
            x = int(x)
            y = int(y)
            if x > y:
                pass
            else:
                break 
        except (ValueError, ZeroDivisionError):
            pass
    percentage = x / y * 100
    rounded_percentage = int(percentage)
    if rounded_percentage >= 99:
        print("F")
    elif rounded_percentage <= 1:
        print("E")
    else:
        print(f"{rounded_percentage}%")

                
            
fuel_gauge()

