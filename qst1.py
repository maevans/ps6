# CSCI 3104 - Algorithms

# Answers to Question 1 of Problem Set #6 

# Part 1: Align Strings Function 
# Mahalia Evans

import random

  #Prompt the user for two words 
  word1 = input('First word: ')
  word2 = input('Second word: ')
  
  #Align the inputs
  align = alignStrings(word1, word2)

def alignStrings(x,y):
  
  #Intialize table & variables   
    S = [[0 for i in xrange(len(x)+1)] for j in xrange(len(y)+1)] 
    back = [[0 for i in xrange(len(x)+1)] for j in xrange(len(y)+1)] #To backtrack through the string 
  
  #Create a scoring matrix 
    for i in xrange(1, (len(x)+1)):
      for j in range(1, (len(y)+1)): 
        score = (S[i-1][j] - 1) , (S[i][j-1] - 1), (S[i-1][j-1] + [-1,1]x[i-1] == y[j-1]) #Base Cases
        S[i][j] = max(score)
        back[i][j] = score.index(S[i][j])
  
  #Initialize Dynamic programming Calculation 
  #Get max score of shortest word 
    i = max(enumerated(S[level][j] for level in xrange(len(y), len(x))), (key = lambda x: x[1]), ([0] + len(y))
    j = len(y)
    maxScore = str(S[i][j]) #Maximum score for the end of the shortest word 
  
  #Calculate matrix 
    x_align = x[:i]
    y_align = y[:j]
    
    swapIdeal = lambda string, i: string[:i] + '  ' + string[i:] #Swap for Ideals 
  
  #Trace Back & Create Alignment 
    while i & j != 0: 
      if back[i][j] == 0: 
        i -= 1
        y_align = swapIdeal(y_align, j)
      elif back[i][j] == 1: 
        j -= 1
        x_align = swapIdeal(x_align, i) 
      elif back[i][j] == 2: 
        i -= 1
        j -= 1
        
  return maxScore, x_align, y_align  #Return Matrix  
  
  print 'Matrix: ', maxScore, '  ', x_align, '  ', y_align  
#End of function    

#Print Alignment 
print 'Alignment: ', align



def extractAlignment(S, x, y):
    i = len(S)-1
    j = len(S[0])-1
    a = []
    while (i, j) != (0, 0):
        a.append(determineOptimalOp(S, i, j, x, y))
        newind = updateIndices(S,i,j, a)
        i = newind[0]
        j = newind[1]
    a = list(reversed(a))
    print a

def determineOptimalOp(S, i, j, x, y):
    subcost = 1
    indelcost = 1
    swapcost = 1
    potentialops = []
    if (S[i-1][j-1] + subcost == S[i][j]):
        potentialops.append("Sub")
    if (S[i][j-1] +indelcost == S[i][j]):
        potentialops.append("Indel")
    if (S[i-1][j] + indelcost == S[i][j]):
        potentialops.append("Indel")
    if (S[i-2][j-2] + swapcost == S[i][j] and x[i-1] == y[j-2]):
        potentialops.append("Swap")
    if (S[i-1][j-1] == S[i][j] and x[i-1] == x[j-1]):
        potentialops.append("No-op")

    return (random.choice(potentialops))


def updateIndices(S, i, j, a):
    if a[len(a)-1] == "No-op":
        i = i-1
        j = j-1
        return(i,j)
    elif a[len(a)-1] == "Indel":
        if (S[i][j-1] == S[i][j] - 1):
            j = j-1
            return (i,j)
        else:
            i = i-1
            return(i,j)
    elif a[len(a) - 1] == "Sub":
        i = i-1
        j = j-1
        return(i,j)
    elif a[len(a) - 1] == "Swap":
        i = i-2
        j = j-2
        return(i,j)

arr = [[0,1,2,3],[1,1,2,3],[2,2,2,3],[3,3,3,2],[4,4,3,3]]
print determineOptimalOp(arr,1,1, "step", "ape")
extractAlignment(arr, "step", "ape")

#def commonSubstrings(x, L, a):
 #   commonstrings = []
  #  for i in range (0, len(a)):
   #     if (a[i] == "No-op"):
    #        commonstrings.append(recstring(i))
#    def recstring(start):
 #       string = x[i]
  #      if (a[i+1] == "No-op"):
   #
    #    if (a[i+1] == noo

