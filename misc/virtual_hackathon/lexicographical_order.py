

def lex(words, alpha):
    indices = {}
    new_words = []

    for i, c in enumerate(alpha):
        indices[c] = i


    for w in words:
        word = [indices[c] for c in w]
        new_words.append((word, w))

    for _, word in sorted(new_words):
        print(word)

    print()


def main():
    t = int(input())

    for _ in range(t):
        alpha = input().strip()

        n = int(input())
        words = []

        for _ in range(n):
            words.append(input().strip())

        lex(words, alpha)
        input()

main()
