
import fileinput
import re


FIRST_NAME_RE = re.compile("^[A-Z][a-z]{0,9}$")
LAST_NAME_RE = re.compile("^[A-Z][a-z]{0,19}$")


def verify(line):
    first, last, date = (x.strip() for x in line.split(";"))

    name = first.split(":")[1].strip()
    surname = last.split(":")[1].strip()
    year, month, day = date.split(":")[1].strip().split("-")

    if not FIRST_NAME_RE.match(name):
        return 0
    elif not LAST_NAME_RE.match(surname):
        return 1
    else:
        try:
            year = int(year)
            month = int(month)
            day = int(day)

            if year < 1900 or year > 2000 or month < 1 or month > 12 or day < 1 or day > 31:
                return 2
        except:
            return 2

    return 3


def main():
    for line in fileinput.input():
        print(verify(line))

main()
