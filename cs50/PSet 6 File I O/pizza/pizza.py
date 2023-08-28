import sys
import os
import csv
from tabulate import tabulate
    
    
def main():
    arg_validator()
    csv_file = sys.argv[1]
        
    if not csv_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(csv_file):
        sys.exit("File does not exist")

    data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    table = tabulate(data, headers="firstrow", tablefmt="grid")
    print(table)


def arg_validator():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    elif len(sys.argv) == 2:
        return True
    

if __name__ == "__main__":
    main()