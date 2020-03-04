#G00387859 DONAL MAHER
"""
Task: Write a program that asks the user to input any positive integer 
and outputs the successive values of the following calculation. 
At each step calculate the next value by taking the current value and, 
if it is even, divide it by two, but if it is odd, 
multiply it by three and add one. 
Have the program end if the current value is one.
Try and catch should be added here. 
"""
UserSentence = int(input("Please enter a positive integer: "))
# check if the current value is postitive or negitive
#Create a list
list = []
#add  the users input directly into element 0
list.append(UserSentence)
# while the UserSentence is not equal 1
while UserSentence != 1:
    if (UserSentence % 2) == 0:
        UserSentence = UserSentence / 2
        list.append(int(UserSentence))
    else:
        UserSentence = UserSentence * 3 + 1
        list.append(int(UserSentence))
#loop over the list and print on the same line
for x in range(len(list)):
    print(list[x], end = " ")
