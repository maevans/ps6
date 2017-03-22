# CSCI 3104 - Algorithms

# Answers to Question 1 of Problem Set #6 

# Part 1: Align Strings Function 
# Mahalia Evans

import random

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

def alignStrings(x, y):
    S = [[0 for i in range(0, len(y) + 1)] for j in range(0, len(x) + 1)]
    costsub = 1
    costindel = 1
    costswap = 1

    for i in range (0,len(x)+1):
        S[i][0] = i
    for j in range (0, len(y)+1):
        S[0][j] =j
    for j in range (1, len(y)+1):
        nextoptions=[]
        i = 1
        nextoptions.append(S[i-1][j-1] +costsub)
        nextoptions.append(S[i-1][j]+costindel)
        nextoptions.append(S[i][j-1]+costindel)
        if (x[i-1]==y[j-1]):
            nextoptions.append(S[i-1][j-1])
        S[i][j] = min(nextoptions)

    for i in range (1, len(x)+1):
        nextoptions=[]
        j = 1
        nextoptions.append(S[i - 1][j - 1] + costsub)
        nextoptions.append(S[i - 1][j] + costindel)
        nextoptions.append(S[i][j - 1] + costindel)
        if (x[i-1] == y[j-1]):
            nextoptions.append(S[i - 1][j - 1])
        S[i][j] = min(nextoptions)


    for j in range(2, len(y)+1):
        for i in range(2, len(x)+1):
            nextoptions=[]
            nextoptions.append(S[i - 1][j - 1] + costsub)
            nextoptions.append(S[i - 1][j] + costindel)
            nextoptions.append(S[i][j - 1] + costindel)
            if (x[i-1] == y[j-1]):
                nextoptions.append(S[i - 1][j - 1])
            if (x[i-1] == y[j-2]):
                nextoptions.append(S[i-2][j-2]+costswap)
            S[i][j] = min(nextoptions)
    return S
extractAlignment(alignStrings("step", "ape"), "step", "ape")

#arr = [[0,1,2,3],[1,1,2,3],[2,2,2,3],[3,3,3,2],[4,4,3,3]]
#print determineOptimalOp(arr,1,1, "step", "ape")
#extractAlignment(arr, "step", "ape")

# Part 3: Common Sub Strings Function 
# Ryan Shuman 
            
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