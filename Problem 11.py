# Problem 11
def P11(file):
    counter = 0
    with open(file, "rt") as f:
        lines = f.readlines()
        for content in lines:
            num_characters = len(content)
            words = content.split()

            for word in words:
                if "sh" in word:
                    counter += 1
                    print(f"{counter}. {word}")

    print(f"Number of times sh was present in a word: {counter}")
                    
if __name__ == "__main__":
    print("Problem: Copy and paste function")
    P11("file1.txt")
