def outdated():
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if validate(month, day):
                    break
            else:
                month, day, year = date.split(" ")
                month = month_list.index(month.title())+1
                day = day.strip(",")
                day = int(day)
                year = int(year)
                if validate(month, day):
                    break
        except ValueError:
            pass
    print(f"{year}-{month:02}-{day:02}")
            
def validate(month, day):
    if day > 31 or month > 12:
        return False
    else:
        return True



outdated()

    