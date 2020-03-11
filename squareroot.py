#G00387859 DONAL MAHER
"""
Write a program that takes a positive floating-point number as input and outputs an 
approximation of its square root. 
You should create a function called sqrt that does this.
Reference: Found this very useful, https://www.youtube.com/watch?v=OAmAwSV5EGk  
"""
import math

def sqrt1(num):
    #this method create for comparsion
    #recreate the math 
    #sqrtR = math.sqrt(num)
    sqrtR= num**(1.0/2)
    return sqrtR
#The function below will use Newtons Square Root approximation. 
def sqrt(n):
    guess = n /2
    count = 1
    while count != 10: # larger values do not get any much closer to the actual square root 
        guess = (guess + (n/guess))/2 # Calculate the guess formula.
        count +=1 # increment the counter
    return "The square root of {} is approx. {}.".format(n,round(guess,1)) # format the output.  

num = float(input("Please enter a positive number: "))
print(sqrt(num))