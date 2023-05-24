def add(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result
    
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero"
        else:
            result /= num
    return result
    
    
def get_numbers():
    num_input = input("Enter numbers separated by spaces: ")
    num_list = [float(num) for num in num_input.split()]
    return num_list


print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#take input from the user
choice = int(input("Enter choice(1,2,3,4):"))

numbers = get_numbers()

if choice == 1:
    print(add(numbers)) # Output: sum of the numbers
elif choice == 2:
    print(subtract(numbers))
elif choice == 3:
    print(multiply(numbers)) # Output: product of the numbers
elif choice == 4:
    print(divide(numbers))
