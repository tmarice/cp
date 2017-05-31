
import random


with open('test.in', 'w') as f:
    f.write('4\n')

    for _ in range(4):
        f.write("500 500\n")

        for _ in range(500):
            for _ in range(500):
                f.write(str(random.randint(1, 1000000)))
                f.write(" ")
            f.write("\n")


