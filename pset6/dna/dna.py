from csv import reader, DictReader
from sys import argv, exit


def main():
    # check for appropriate command
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit()

    # extract data for counting
    with open(argv[1]) as datafile:
        datareader = reader(datafile)
        for row in datareader:
            sequence_data = row
            sequence_data.pop(0)
            break

    # extract dna data
    with open(argv[2]) as dnafile:
        dnareader = reader(dnafile)
        for row in dnareader:
            dnalist = row

    # stringify dna data
    dna = dnalist[0]

    # initialize a dictionary for counting
    sequences = {}
    for item in sequence_data:
        sequences[item] = 0

    # count
    for key in sequences:
        l = len(key)
        tmp = 0
        tmpMax = 0
        for i in range(len(dna)):
            while tmp > 0:
                tmp -= 1
            if dna[i:i + l] == key:
                tmp = 1
                while dna[i - l:i] == dna[i:i + l]:
                    tmp += 1
                    i += l
                if tmp > tmpMax:
                    tmpMax = tmp
        sequences[key] += tmpMax

    # compare & print
    with open(argv[1]) as peoplefile:
        people = DictReader(peoplefile)
        for person in people:
            match = 0
            for dna in sequences:
                if sequences[dna] == int(person[dna]):
                    match += 1
            if match == len(sequences):
                print(person["name"])
                exit()
        print("No Match")


main()