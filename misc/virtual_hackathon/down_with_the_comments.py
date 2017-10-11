
import fileinput


def decommentify(text):
    open_multi = False
    open_single = False

    i = 0
    end = len(text) - 1

    while i < end:
        c1 = text[i]
        c2 = text[i + 1]

        if c1 == '/' and c2 == '*':
            open_multi = True
            i += 2
        elif c1 == '*' and c2 == '/':
            open_multi = False
            i += 2
        elif c1 == '/' and c2 == '/':
            open_single = True
            i += 2
        elif open_single and c1 == '\n':
            open_single = False


        if not open_multi and not open_single:
            print(text[i], end='')

        i += 1


def main():
    text = "".join(fileinput.input())

    decommentify(text)

main()
