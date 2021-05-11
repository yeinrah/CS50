from cs50 import get_float


def main():
    c = prompt()

    c = round(c * 100)

    n = 0
    while (0 < c):
        if (25 <= c):
            c -= 25
            n += 1
        elif (10 <= c):
            c -= 10
            n += 1
        elif (5 <= c):
            c -= 5
            n += 1
        elif (1 <= c):
            c -= 1
            n += 1

    print(n)


def prompt():
    c = 0
    while True:
        c = get_float("How mush do I owe you?")
        if (c > 0):
            break
    return c


main()