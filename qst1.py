# CSCI 3104 - Algorithms 

# Answers to Question 1 of Problem Set #6 

# Part 1: Align Strings Function 
# Mahalia Evans 

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
            
            
