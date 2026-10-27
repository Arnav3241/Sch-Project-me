# Problem 13
new_lines = []

def P13(in_file, out_file):
    with open(in_file, "rt") as f:
        lines=f.readlines()
        
    for line in lines:
        new_l = line.capitalize()
        state=0
        while state==0:
            new_l=new_l.replace("\t", " ")
            if "\t" not in new_l:
                state = 1
        state = 0 #if 0 rerun the code. 1 for process completed
        while state==0:
            new_l=new_l.replace("  ", " ")
            if "  " not in new_l:
                state = 1
        if new_l[0] == " ":
            new_l = new_l.replace(" ", "")
        

                
        new_lines.append(new_l)    
    with open(out_file, "wt") as f:
        for nl in new_lines:
            f.write(nl)
    
                    
if __name__ == "__main__":
    print("Problem: 1st word captialized and remove extra spaces")
#   P13(input("Name of input file: "), input("Name of output file: "))
    P13("P13\\file1.txt", "P13\\file2.txt")
