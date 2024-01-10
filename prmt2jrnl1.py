# -*- coding: utf-8 -*-
while True: #input stuff to make sure it's a float
    try:
        x = float(input("Please input a float: "))
        y = float(input("Please input another float: "))
        break
    except ValueError:
        print("Uh oh that's not a float")
        
while True: #more input stuff to make sure it's an int
    try:
        a = int(input("Please input an integer: "))
        b = int(input("Please input another integer: "))
        break
    except ValueError:
        print("Uh oh that's not an integer")
        
        
def AddTwoFloats(x,y): #Adding the two floats together
    z = x + y
    print("The sum of your numbers is: " , z, type(z))
    
def SubtractTwoInts(a,b):  #Subtracting the integers 
    c = a - b
    print("The difference between your integers is: "  , c , type(c) )

def MultiplyIntandFloat(x,a): # multiplying them together
    d = x * a
    print("The product between your first int and first float is: " , d, type(d))

def main():  #Can't forget this!
    AddTwoFloats(x,y)
    SubtractTwoInts(a,b)
    MultiplyIntandFloat(x,a)

if __name__ == "__main__": #can't forget this either!
    main()
    