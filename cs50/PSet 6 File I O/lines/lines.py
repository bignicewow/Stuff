import sys
import os

def main():
    arg_validator()
    argument = sys.argv[1]
        
    if not argument.endswith(".py"):
        sys.exit("Not a python file")

    if not os.path.exists(argument):
        sys.exit("File does not exist")
    
    code_lines = 0
    
    with open(argument, "r") as file:
        for line in file:
            stripped_line = line.lstrip()

            if not stripped_line or stripped_line.startswith("#"):
                continue

            code_lines += 1
    print(code_lines)


def arg_validator():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    elif len(sys.argv) == 2:
        return True
    

if __name__ == "__main__":
    main()