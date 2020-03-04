#G00387859 DONAL MAHER
"""
Write a program that takes a positive floating-point number as input and outputs an 
approximation of its square root. 
You should create a function called sqrt that does this.
"""
import math

def sqrt(num):
    #recreate the math 
    #sqrtR = math.sqrt(num)
    sqrtR= num**(1.0/2)
    return sqrtR

num = float(input("Please enter a positive number: "))
result = round(sqrt(num),1)
print("The square root of " + str(num)+" is approx. "+str(result)+".")