import random

def main():
    while True:
        try:
            level = validator("Level: ")      
            break
        except ValueError or TypeError:
            pass
    correct_guess = random.randint(1, level)
    while True:
        try:
            guess = validator("Guess: ")
            if guess == correct_guess:
                print("Just right!")
                break
            elif guess < correct_guess:
                print("Too small!")
                pass
            elif guess > correct_guess:
                print("Too large!")
                pass
        except ValueError or TypeError:
            pass

def validator(x):
        number = int(input(x))
        if number > 0:
            return number
        else:
            raise ValueError

main()
