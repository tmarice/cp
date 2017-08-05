


vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w']


def print_melodious(n, s, prev):
    if n == 0:
        print s
    else:
        if prev == 1: # do consonants
            for c in consonants:
                print_melodious(n-1, s+c, 0)
        else: # do vowels
            for v in vowels:
                print_melodious(n-1, s+v, 1)


n = int(raw_input())

print_melodious(n, "", 0)
print_melodious(n, "", 1)



