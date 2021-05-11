from cs50 import get_string


def main():
    text = get_string("Text: ")

    l = 0
    w = 1
    s = 0

    for i in range(len(text)):
        if (text[i].isalpha()):
            l += 1
        elif (text[i].isspace()):
            w += 1
        elif (text[i] == '.' or text[i] == '!' or text[i] == '?'):
            s += 1

    L = l / w * 100
    S = s / w * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if (index < 1):
        print("Before Grade 1")
    elif (index > 1 and index < 16):
        print(f"Grade {index}")
    else:
        print("Grade 16+")


main()