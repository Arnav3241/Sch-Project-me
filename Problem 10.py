# Problem 10
def PrintLinesWith50CharAndMoreThan7Words(file):
    with open(file, "rt") as f:
        lines = f.readlines()
        for content in lines:
            num_characters = len(content)
            words = content.split()

            if len(words) > 8 and num_characters > 50:
                print(content)
                print("Number of Charcters: " + str(num_characters))
                print("Number of words: " + str(len(words))+'\n')


if __name__ == "__main__":
    print("Problem: Print Lines With 50 Characters And More Than 7 Words function")
    PrintLinesWith50CharAndMoreThan7Words(input("Type input file address: "))
