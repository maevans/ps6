# Question 1 - Part f 
# Shakespeare’s play Much Ado About Nothing, Act 1 Scene 2

import re
import random 
# Step 1: Write a function that takes as input the data MuchAdo freqs file for PS6 
file = open("csci3104_S2017_PS6_data_muchAdo_freqs.txt", "r")
print file.read()

# Step 2: Outputs a file x that contains n characters drawn randomly but with the given frequencies
with open("csci3104_S2017_PS6_data_muchAdo_freqs.txt", "r") as file:
    data = file.readlines()
    print data

    word = re.match(r"(?P<numbers>[0-9]+)(?P<letters>.+)$")
    word.group('numbers')
    word.group('letters')
    
    a = random.numbers
    b =  random.letters 
    
    with open("fileX.txt", "w")
        fileX.write(a & b)
        print fileX
        
# Step 3: Using your string alignment functions, determine what value of n is required to produce an overlap of 7 characters

from qst1.py import alignStrings(x,y) 
    def overlap(a,b)
        return list(set(a) & set(b))
        print overlap(a, B)
    with alignStrings(x,y) 
        c = overlap(a, b)
        if c > 7
            print c 
        else 
            print none 
