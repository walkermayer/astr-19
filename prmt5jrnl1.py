"""
Created on Mon Jan 22 13:12:25 2024

@author: walkermayer
"""
import numpy as np
import math
from astropy.table import Table    #importing needed functions



a = np.linspace(0,2*math.pi, 1000)   #creating the arrays for x and sin(x)
y = np.sin(a)


def make_table():
    data_table = Table()
    data_table["x"] = a
    data_table["sin(x)"] = y
    
    data_table["x"].format = "{:.3f}"    #formating to only display 3 decimal points
    data_table["sin(x)"].format = "{:.3f}"
    print(data_table)
    
    
def main():
    make_table()
        
if __name__ == "__main__":
    main()