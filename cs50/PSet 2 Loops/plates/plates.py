def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start_with_letters(s) and min_and_max(s) and check_for_number(s) and only_alnum(s):
        return True

def start_with_letters(s):
    if s[0:2].isalpha():
        return True
    else:
        return False
    
def min_and_max(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False
    
def check_for_number(s):
    number_found = False
    for i in s:
        if i.isalpha() and number_found:
            return False
        elif i.isdigit():
            if number_found == False and i == "0":
                return False
            number_found = True
    return True

def only_alnum(s):
    if s.isalnum() == True:
        return True
    else:
        return False

main()