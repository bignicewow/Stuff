import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern1 = r'^(\d{1,2}:\d{2})\s+(AM|PM)\s+to\s+(\d{1,2}:\d{2})\s+(AM|PM)$'
    pattern2 = r'^(\d{1,2})\s+(AM|PM)\s+to\s+(\d{1,2})\s+(AM|PM)$'

    match1 = re.match(pattern1, s)
    match2 = re.match(pattern2, s)

    if match1:
        hour1 = int(match1.group(1).split(':')[0])
        minute1 = int(match1.group(1).split(':')[1])
        meridiem1 = match1.group(2)
        hour2 = int(match1.group(3).split(':')[0])
        minute2 = int(match1.group(3).split(':')[1])
        meridiem2 = match1.group(4)
    elif match2:
        hour1 = int(match2.group(1))
        minute1 = 0
        meridiem1 = match2.group(2)
        hour2 = int(match2.group(3))
        minute2 = 0
        meridiem2 = match2.group(4)
    else:
        raise ValueError("Invalid input format")

    if not (0 <= hour1 <= 12) or not (0 <= hour2 <= 12) or not (0 <= minute1 < 60) or not (0 <= minute2 < 60):
        raise ValueError("Invalid time")

    if meridiem1 == 'PM' and hour1 != 12:
        hour1 += 12
    elif meridiem1 == 'AM' and hour1 == 12:
        hour1 = 0

    if meridiem2 == 'PM' and hour2 != 12:
        hour2 += 12
    elif meridiem2 == 'AM' and hour2 == 12:
        hour2 = 0

    return f"{hour1:02d}:{minute1:02d} to {hour2:02d}:{minute2:02d}"


if __name__ == "__main__":
    main()
