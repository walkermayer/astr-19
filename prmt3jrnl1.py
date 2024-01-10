"""
Created on Tue Jan  9 18:40:06 2024

@author: walkermayer
"""
x = float(input("x= "))

def f(x):
    y = x ** 3 + 8
    if y > 27:
        print("YAY!")
    else:
        print(y)
    
       
def main(): #gotta remember this!
    f(x)
    
if __name__ == "__main__": #can't forget this either!
    main()