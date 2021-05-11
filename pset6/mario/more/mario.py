from cs50 import get_int


def main():
    i = get_positive_int()
    for a in range(1, i + 1):
        print(" " * (i - a) + "#" * a + "  " + "#" * a)
        a += 1


def get_positive_int():
    h = 0
    while True:
        h = get_int("Height: ")
        if (1 <= h and h <= 8):
            break
    return h


main()