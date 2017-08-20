


def main():
    s = input()
    chars = set(s)

    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in chars:
            print(chr(i))
            break
    else:
        print('None')


if __name__ == '__main__':
    main()
