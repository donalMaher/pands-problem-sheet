#G00387859 DONAL MAHER
"""
Version 2. Edited based on retorspective and review comments.
# Write a program that takes askes a user
# to input a string  and outputs every seconnd letter in reverse order.
# References: 1. w3Schools.2020. How to reverse a string. 1st edition. O'Reiliy Media. Sebastopol, CA United States of America.
              2.Jake VanderPlas.2016.A whirlwind Tour of Python  https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf  
"""
print("Loop over String program ")
try:
    def revString(userInput):
        # return every second letter
        return userInput[::-2]
    userInput = input("Please enter a sentence:")
    print(revString(userInput))

except Exception:
    #This will catch the excecption. The program will not fall over if this user does not enter string values. 
    print("sorry, somthing went wrong!")
