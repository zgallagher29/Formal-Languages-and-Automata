
# coding: utf-8

# In[1]:


import numpy as np

productions = 0



# In[2]:


def main():
    
    start = input("What is the Start Variable? ")
    productions = int(input("What is the number of productions? "))
  
    grammar = np.empty([productions, 12], dtype=object)
    for i in range(0, productions):
        print("Enter a production with a space at the end. Example format: S->aSa|bSb|b|a .")
        prod = input('HEY')
      
        print(prod)
        grammar[i][0] = prod[0]  # before the - in '->'
        grammar[i][1] = prod[1]
        grammar[i][2] = prod[2]
  
        index = 3
        right=prod[3:]
        list1 = right.split('|')
        for term in list1:
            grammar[i][index] = term
            index = index +1
            
            
    print(grammar)
    checkString(grammar)
    
def checkString(grammar):
    
    word = input('What is the string you would like to check? ')
    
    matrix = np.empty([len(word),len(word)], dtype = str)

    for i in range(0, len(word)):
        
        nonTerm = ""
        st=""
        st = st+word[i]
        for j in range(0, productions):
            l = 1 
            while grammar[j][l] != "$":
                  
                if grammar[j][l] ==st:
                    nonTerm = concat(nonTerm,grammar[j][0])
                    
                l = l+1
        matrix[i][i]=nonTerm
    for l in range(1,len(word)):
        for j in range(l,len(word)):
            nonTerm = ""
            for m in range( j-l, j):
                pr = combine(matrix[j-l][m],matrix[m+1][j],grammar)
                nonTerm = concat(nonTerm,pr)
            matrix[j-l][j]=nonTerm
        ##print_results(matrix, word)
    print(matrix)
    if isValidString(word,matrix):
        print("THIS STRING CAN BE GENERATED!")
    else:
        print("THIS STRING CANNOT BE GENERATED!")

def print_results(matrix, word):
    for i in range(0,len(word)):
        x = 0
        k = len(word) - i -1
        for j in range(k,len(word)):
            print(matrix[x][j])
            x =x+1
def isValidString(word, matrix):
    if matrix[0][0].find('S')!=matrix[0][0]:
        return True
    return False
                            
                        
def combine(a,b,grammar):
    pri=a
    re=""
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            pri = ""
            pri = pri+a[i]+b[j]
            re = re + find_production(pri,grammar)
    return re 
                    
def find_production(p,grammar):
    r =""
    for i in range(0,productions):
        l = 1 
        while grammar[i][l]!="$":
            if grammar[i][l] == p:
                r = concat(r,grammar[i][0])
def concat(nonTerm,gram):
    r = nonTerm
    for i in range(0,len(gram)):
        if r.find(gram[i]) > len(r):
            r = r+gram[i]        
    return r
        
        
                    
    
        
        
        
        


# In[ ]:


main()

