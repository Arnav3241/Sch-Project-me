# Problem 9
def FindWord(file, word):
    counter = 0
    with open(file, "rt") as f:
        content = f.read()
        words = content.split()
        for w in words:
            if w.lower() == word.lower():
                counter += 1
    print(counter)

if __name__ == "__main__":
    print("Problem: Word finder function")
    FindWord(input("Type input file address: "), input("What is the word you want to count: "))
