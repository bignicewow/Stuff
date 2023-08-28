from datetime import date, datetime
import inflect
import sys

def main():
    birth_date = input("Date of birth: ")
    age_in_minutes = calculate_age(birth_date)
    in_words = convert_to_words(age_in_minutes)
    print(f"{in_words} minutes")


def calculate_age(birth_date):
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format")
    today = date.today()
    today_datetime = datetime.combine(today, datetime.min.time())
    birth_datetime = datetime.combine(birth_date, datetime.min.time())
    age = today_datetime - birth_datetime
    age_in_minutes = round(age.total_seconds() / 60)
    return age_in_minutes


def convert_to_words(age_in_minutes):
    p = inflect.engine()
    words = p.number_to_words(age_in_minutes, andword="").capitalize()
    return words


if __name__ == "__main__":
    main()