#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:07:03 2024

@author: walkermayer
"""
class favanimal:
    def __init__(self, armlength, leglength, numeyes, tail, furry):  #initialization function
        self.armlength = armlength
        self.leglength = leglength
        self.numeyes = numeyes
        self.tail = tail
        self.furry = furry


lion = favanimal(4,8,2,True, True)

def info():
    print("Arm length is:" , lion.armlength)
    print("Leg length is:" , lion.leglength)
    print("The lion has" , lion.numeyes , "eyes")
    print("The lion has a tail:" , lion.tail)
    print("The lion is furry:" , lion.furry)





def main():
    info()
    
    
if __name__ == "__main__":
    main()