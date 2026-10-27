# Problem 12

def P12(in_file, out_file):
    state = 1 #1 means Uppercase and 0 menas lower case 
    with open(in_file, "rt") as f:
        lines = f.readlines()
    with open(out_file, "wt") as f:
        for line in lines:
            if state==1:
                f.write(str(line).upper())
                state=0
            else:
                f.write(str(line).lower())
                state=1
                    
if __name__ == "__main__":
    print("Problem: Alternate uppercase and lowercase")
#   P12(input("Name of input file: "), input("Name of output file: "))
    P12("P12\\file1.txt", "P12\\file2.txt")
