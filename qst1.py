# CSCI 3104 - Algorithms

# Answers to Question 1 of Problem Set #6 

import random

def extractAlignment(S, x, y):
    #start in bottom right corner
    i = len(S)-1
    j = len(S[0])-1
    #list that will be given optimal operations
    a = []
    #iterate through cost matrix by tracing back the most recent operation
    # and updating the indices as such.
    #ties are broken randomly by making a list of the potential
    #tracebacks and randomly selecting one.
    while (i, j) != (0, 0):
        a.append(determineOptimalOp(S, i, j, x, y))
        newind = updateIndices(S,i,j, a)
        i = newind[0]
        j = newind[1]
    a = list(reversed(a))
    print a
    return a

#determines the optimal operation in the traceback of the optimal cost matrix
#costs of operations can be changed to account for different scenarios
#ties are broken randomly
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
    if (S[i-1][j-1] == S[i][j] and x[i-1] == y[j-1]):
        potentialops.append("No-op")

    return (random.choice(potentialops))

#updates the i and j indices during the traceback based on what operation was taken
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

#returns the optimal cost matrix for 2 given strings
def alignStrings(x, y):
    S = [[0 for i in range(0, len(y) + 1)] for j in range(0, len(x) + 1)]
    #costs can be changed to whatever desired
    costsub = 1
    costindel = 1
    costswap = 1

    #fills in the first row
    for i in range (0,len(x)+1):
        S[i][0] = i

    #fills in the first column
    for j in range (0, len(y)+1):
        S[0][j] =j

    #fills in the second row(Swap will be out of range)
    for j in range (1, len(y)+1):
        nextoptions=[]
        i = 1
        nextoptions.append(S[i-1][j-1] +costsub)
        nextoptions.append(S[i-1][j]+costindel)
        nextoptions.append(S[i][j-1]+costindel)
        if (x[i-1]==y[j-1]):
            nextoptions.append(S[i-1][j-1])
        S[i][j] = min(nextoptions)

    #fills in the second column(Swap will be out of range)
    for i in range (1, len(x)+1):
        nextoptions=[]
        j = 1
        nextoptions.append(S[i - 1][j - 1] + costsub)
        nextoptions.append(S[i - 1][j] + costindel)
        nextoptions.append(S[i][j - 1] + costindel)
        if (x[i-1] == y[j-1]):
            nextoptions.append(S[i - 1][j - 1])
        S[i][j] = min(nextoptions)

    #fills in the rest of the matrix where Swap is in range
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

#I feel the writeup is somewhat unclear on what this function should do
#As it is implemented now, it returns any substrings that line up
#when the two strings, x and y are aligned by their first letter
def commonSubstrings(x, L, a):
    commonstrings = []
    stringindex = 0

    #iterate through the optimal operations, recording substring for no-ops
    i = 0
    while (i < len(a)):
       if (a[i] == "Indel"):
           i = i+1
           stringindex = stringindex +1
       elif (a[i] == "Sub"):
           i=i+1
           stringindex = stringindex+1
       elif (a[i] == "Swap"):
           i=i+1
           stringindex = stringindex+2
       elif (a[i] == "No-op"):
            b = recstring("",x,stringindex,a,i)
            commonstrings.append(b[0])
            i = b[1]
            stringindex = b[2]
    for item in commonstrings:
        if (len(item) < L):
            commonstrings.remove(item)
    print commonstrings

#recursively builds substring if there are multiple no-ops in a row
def recstring(string1, xstring, stringindex1, a1, opsindex):
    string1 = string1 + xstring[stringindex1]
    if (opsindex == len(a1)-1 or a1[opsindex+1] != "No-op"):
        return (string1, opsindex+1, stringindex1+1)
    else:
        return recstring(string1, xstring, stringindex1 +1, a1,opsindex+1)

#Running the following will yield the exact output in the example
#from the lecture notes
x ="the white house office of the press secretary for immediate release march 06, 2017 president trump congratulates exxon mobil for job-creating investment program  washington, d.c. -- president donald j. trump today congratulated exxon mobil corporation on its ambitious $20 billion investment program that is creating more than 45,000 construction and manufacturing jobs in the united states gulf coast region.  president trump made a promise to bring back jobs to america. the spirit of optimism sweeping the country is already boosting job growth, and it is only the beginning.  “this is exactly the kind of investment, economic development and job creation that will help put americans back to work,” the president said. “many of the products that will be manufactured here in the united states by american workers will be exported to other countries, improving our balance of trade. this is a true american success story. in addition, the jobs created are paying on average $100,000 per year.”  darren w. woods, chairman and chief executive officer of exxon mobil announced the company’s investment program during a keynote speech today to an oil and gas industry conference in houston, texas.  “investments of this scale require a pro-growth approach and a stable regulatory environment and we appreciate the president’s commitment to both,” said woods. “the energy industry has proven it can operate safely and responsibly. private sector investment is enhanced by this administration’s support for smart regulations that support growth while protecting the environment.”  exxon mobil is strategically investing in new refining and chemical-manufacturing projects in the united states gulf coast region to expand its manufacturing and export capacity. the company’s growing the gulf program consists of 11 major chemical, refining, lubricant and liquefied natural gas projects at proposed new and existing facilities along the texas and louisiana coasts. investments began in 2013 and are expected to continue through at least 2022.  exxon mobil’s projects, once completed and operating at mature levels, are expected to have far-reaching and long-lasting benefits. projects planned or under way are expected to create more than 35,000 construction jobs and more than 12,000 full-time jobs. these are full-time manufacturing jobs that are mostly high-skilled and high-paying, and have annual salaries ranging from $75,000 to $125,000. these jobs will have a multiplier effect, creating many more jobs in the community that service these new investments.
"
a = extractAlignment(alignStrings("step", "ape"),"step", "ape")
commonSubstrings("step", 1, a)



            
