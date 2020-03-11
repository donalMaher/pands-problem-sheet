#G00387859 DONAL MAHER
"""
This python script will take 2 arguments when running.
The python filename and the .txt file. 
reference 1: http://www.java2s.com/Code/Python/File/Openafileandreadcharbychar.htm
"""
import sys
filename = sys.argv[1]
countE = 0 # DECLARE A VARIBLE TO HOLD THE COUNT

with open(filename, 'r') as f:
   while 1: # continous loop 
      letter = f.read(1)# read every single characher in the file
      if(letter == 'e'):# compare the current characher to 'e',  
         countE+=1           #if the condition is true increment the variable counter
      if(not letter):         # if the next char is empty then break.
         break
   f.close
print(countE)

