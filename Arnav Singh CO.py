
#Problem 2:
def Cube(a):
    return a*a*a, 6*a*a

def Cuboid(a,b,c):
    return a*b*c, 2*a*b + 2*b*c +2*c*a

def Sphere(r):
    return 4/3*3.14*r*r*r, 4*3.14*r*r

def Cylinder(r,h):
    return 3.14*r*r*h, 3.14*2*r*r + 2*3.14*r*h

#Problem 3: Create a function DICE 1 to 6 till user exits
def Dice():
    from random import randint
    return randint(1,6)




#Probem 4: function to check if string is a pallinrome











#Prob;em 

#Main Executable
while True:
    problem=input("Which Problem: ")
    if problem=="2":
        shape = input("Select shape out of Cube, Cuboid, Sphere and Cylinder or Type exit to exit the loop: ")
        a= True
        while True:
            if shape == "Cube" or shape=="cube":
                vol, sa = Cube(float(input("Enter Side length: ")))
                print(f"Volume: {vol} \nSurface Area:{sa}")
            elif shape == "Cuboid" or shape=="cuboid":
                a=float(input("Enter 1st Side length: "))
                b=float(input("Enter 2nd Side length: "))
                c=float(input("Enter 3rd Side length: "))
                vol, sa = Cuboid(a,b,c)
                print(f"Volume: {vol} \nSurface Area:{sa}")
            elif shape=="Sphere":
                r=float(input("Enter Radius: "))
                vol, sa = Sphere(r)
                print(f"Volume: {vol} \nSurface Area:{sa}")
            elif shape=="Cylinder":
                r=float(input("Enter Radius: "))
                h=float(input("Enter Height: "))
                vol, sa = Cylinder(r,h)
                print(f"Volume: {vol} \nSurface Area:{sa}")
            elif: shape=="exit":
                a=False
            else:
                print("Invalid Shape type selected")
        print("/n/n")
    elif problem=="3":
        print(f"Your dice has begun rolling. press enter to continue rolling. Type exit to exit the loop")
        a=True
        while a:
            print(f"Your number is: {Dice()}", end="")
            if input()=="exit":
                a=False
        print("/n/n")
        
