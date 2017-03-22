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

