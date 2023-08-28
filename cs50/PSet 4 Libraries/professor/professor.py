import random


def main():
    correct_answers = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        wrong_answers = 0
        while wrong_answers < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != z:
                    wrong_answers += 1
                    if wrong_answers == 3:
                        print(f"{x} + {y} = {z}")
                    else:
                        print("EEE")
                else:
                    correct_answers += 1
                    break
            except ValueError:
                pass
    print(f"Score: {correct_answers}")
        

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass
    

def generate_integer(level):
    if level == 1:
        new_integer = random.randint(1,9)
    elif level == 2:
        new_integer = random.randint(10,99)
    else:
        new_integer = random.randint(100,999)
    return new_integer


if __name__ == "__main__":
    main()