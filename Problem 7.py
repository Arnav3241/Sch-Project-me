Books = {"Book 01": 69.0, "Book 02": 690.0, "Book 03": 6.9, "Book 04": 609.0, "Book 05": 6009.0, "Book 06": 6699.0}
def AddBook(BookName, Price):
    Books.update({BookName: Price})
    
def RemoveBook(Bookname):
    try: Books.pop(str(Bookname))
    except: print("Book name appears to be wrong.")
    
def ChangePrice(Bookname, price):
    Booknames = []
    for i,v in Books.items():
        Booknames.append(str(i)) 
    if Bookname in Booknames: Books[str(Bookname)]=float(price)
    else: print("Book name appears to be wrong.")
    
def PrintBookSortHigher(HigherThan):
    count=0
    for i,v in Books.items(): #i is id(book name) and v is value(price)
        if float(v)>float(HigherThan):
            print(str(i)+" of price $" + str(v))
            count+=1
    print(f"Total number of books higher than ${float(HigherThan)} is/are {count}.")

    
def PrintBookSortLower(LowerThan):
    count=0
    for i,v in Books.items(): #i is id(book name) and v is value(price)
        if float(v)<float(LowerThan):
            print(str(i))
            count+=1
        print(f"Total number of books lower than ${float(LowerThan)} is/are {count}.")

def HighestAndLowest():
    Highest=0
    HighestName=""
    Lowest=99999999999
    Lowestname=""
    for i,v in Books.items():
        if v<Lowest:
            Lowestname=i
            Lowest=v
        if v>Highest:
            HighestName=i
            Highest=v
    print(f"The price of the most expensive book is {HighestName} with price ${Highest}")
    print(f"The price of the least expensive book is {Lowestname} with price ${Lowest}")
    
        
if __name__ == "__main__":
    print("Here are the elements of the Books List and their prices")
    for i,v in Books.items():
        print(f"{i}: ${v}")
    print("\nYou may perform operation on this list by typing the corresponding number:")
    print("Type 0 for print the list of books.")
    print("Type 1 for adding a book.")
    print("Type 2 for removing a book.")
    print("Type 3 for changing the price a book.")
    print("Type 4 for sorting by higher or lower prices.")
    print("Type 5 for getting the name of the highest and lowest prices.\n")
    
    while True:
        try:
            operation = input("\nOperation Code Number: ")
            if int(operation)==0:
                for i,v in Books.items():
                    print(f"{i}: ${v}") 
            elif int(operation)==1:
                AddBook(str(input("What is the name of your book: ")), float(input("What is the price of the book in $: ")))
            elif int(operation)==2:
                RemoveBook(str(input("Type the name of the book with taking care of upper and lower cases: ")))
            elif int(operation)==3:
                ChangePrice(str(input("Type the name of the book with taking care of upper and lower cases: ")), float(input("What is the new price of the book in $: ")))
            elif int(operation)==4:
                print("For sort higher type 1")
                print("For sort lower type 0")
                sortcode = input("Type sort code: ")
                if int(sortcode) == 0:
                    PrintBookSortHigher(int(input("Sort books higher than price in $: ")))
                elif int(sortcode) == 1:
                    PrintBookSortLower(int(input("Sort books lower than price in $: ")))
                else: print("Invalid sort code")
            elif int(operation)==5:
                HighestAndLowest()
            else:
                print("Operation does not exist.")
    

            
