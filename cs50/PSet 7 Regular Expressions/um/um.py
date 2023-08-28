import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    counter = len(re.findall(pattern, s, re.IGNORECASE))
    return counter


if __name__ == "__main__":
    main()