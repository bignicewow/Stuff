def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    percentage = x / y * 100
    rounded_percentage = int(percentage)
    return rounded_percentage
    

def gauge(rounded_percentage):
    if rounded_percentage <= 1:
        return "E"
    elif rounded_percentage >= 99:
        return "F"
    else:
        return f"{rounded_percentage}%"


if __name__ == "__main__":
    main()