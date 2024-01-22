"""
Created on Mon Jan 22 13:12:25 2024

@author: walkermayer
"""
import numpy as np
import math

a = np.linspace(0,2*math.pi, 1000)

def main():
    for i in a:
        print(f'x: {i:6.4f}  sin(x):  {math.sin(i):6.4f} \n')
        
if __name__ == "__main__":
    main()