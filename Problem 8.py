# Problem 8
def CopylinesStartingFromVovels(copy_file, paste_file):
    with open(copy_file, "rt") as cf:
        content = cf.readlines()
        print(f"Copied Content from {copy_file}: {content}")
    with open(paste_file, "w") as pf:
        for line in content:
            if line[0].lower() in "aeiou0123456789":
                print("Pasting line: " + line)
                pf.write(line)
                print(f"Paste successful from {paste_file}")

if __name__ == "__main__":
    print("Problem: Copy and paste function")
    CopylinesStartingFromVovels(input("Type Copy file address: "), input("Type Paste file address: "))
