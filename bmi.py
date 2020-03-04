#G00387859 DONAL MAHER
"""
This python script code will calculate Bmi for any user.
Any user input will need a try and catch to catch any non int input. 
"""
print("BMI CALCULATER")
try:
    #Ask user for input and convert from string to float
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    #convert height from grams to Kilograms
    height = height/100
    #calculate the bim calculation
    bim = weight/(height**2)#
    #print the result but format the answer to 2 decimal places
    print("BMI is {:2.2f}.".format(bim))
except Exception:
    #This will stop program will not fall over if this user does not enter a integer. 
    print("sorry, something went wrong!")
