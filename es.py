#G00387859 DONAL MAHER
"""
This python script will take 2 arguments when running.
The python filename and the .txt file. 
"""
import sys
filename = sys.argv[1]
k = 0 # DECLARE A VARIBLE TO HOLD THE COUNT

myList = [] # DECLARE A EMPTY LIST
with open(filename, 'r') as f: # READ THE FILE
   # LOOP OVER THE CHARS IN THE FILE AND ASSIGN TO A LIST  
    while 1: 
       char = f.read(1)
       if not char: break # BREAK OUT OF THE WHILE LOOP IF THERE ARE NO MORE CHARS
       myList.append(char) # APPEND EACH CHAR TO THE LIST
#LOOP OVER THE LIST AND COMPARE EACH CHAR TO THE REQUESTED CHAR
for x in myList:
        if(x == 'e'):
            k+=1
print(k)

