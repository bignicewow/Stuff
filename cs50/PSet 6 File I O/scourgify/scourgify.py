import sys
import os
import csv


def main():
    arg_validator()
    csv_file = sys.argv[1]

    if not csv_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(csv_file):
        sys.exit("File does not exist")

    data = read_csv(csv_file)
    write_csv(data)

    
def read_csv(csv_file):
    data = []
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last_name, first_name = row["name"].split(",")
            data.append({"last name":last_name, "first name":first_name, "house":row["house"]})
    return data
          

def write_csv(data):
    with open(sys.argv[2], "w", newline='') as file:
        fieldnames = ["first name", "last name", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def arg_validator():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        return True
    

if __name__ == "__main__":
    main()