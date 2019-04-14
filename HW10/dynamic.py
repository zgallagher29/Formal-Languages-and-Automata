
# coding: utf-8

# In[1]:

import time
import numpy as np





# In[2]:
prods = ['S->AB|BC','A->BA|a','B->CC|b','C->AB|a']
nums = 4
def main():
    
    
  #  productions = int(input("What is the number of productions? "))
    productions =4
    grammar = np.empty([productions, 12], dtype=object)
    for i in range(0, productions):
        print("Enter a production. Example format: S->aSa|bSb|b|a .")
        prod = prods[i]
      
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
            
        grammar[i][index]="$"
    
    for i in range(0,productions):
        for j in range(0,12):
            if grammar[i][j] is None:
                grammar[i][j]= ""
    print(grammar)
    checkString(grammar,productions)
    
def checkString(grammar,productions):
    
    #word = input('What is the string you would like to check? ')
    word = "baaba"
    matrix = np.empty([len(word),len(word)], dtype = object)
    for x in range(len(word)):
        for y in range(len(word)):
            matrix[x][y]='x'
    x=0
    nonTerm = ""
    for letter in word:
       
        for prod in range(0,productions):
            right = 3
            while grammar[prod][right]!='$':
                if grammar[prod][right] ==letter:
                    nonTerm = nonTerm+grammar[prod][0]

                right = right +1
        
      
        matrix[x][x] = nonTerm
        nonTerm = ""
        x=x+1
    print(matrix)
    nonTerm=""
    for k in range(1, len(word)):
        for j in range(k, len(word)):
            nonTerm = ""
            for m in range(j-k, j):
                print("j ", j)
                print("k", k)
                print("m", m)
                print (matrix)
                enter = input("Press enter to keep going")

                pr = search_combo(matrix[j-k][m],matrix[m+1][j],grammar,productions)

                nonTerm =nonTerm+pr
            unique = ""
            for z in range(0,len(nonTerm)):
                if nonTerm[z] in unique:
                    print("")
                else:
                    unique = unique+nonTerm[z]

            matrix[j-k][j] = unique

        # matrix row 2 two letters: check if row below  


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
                            
                        
def search_combo(a,b,grammar,productions):
    pri=a
    re=""
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            pri = ""
            pri = pri+a[i]+b[j]
            print('HEPRLLFSA',pri)
            re =re +find_production(pri,grammar,productions)
            
    return re 
                    
def find_production(p,grammar,productions):
    r =""
 

    for i in range(0,productions):
        l = 3 
        while grammar[i][l]!="$":
            if grammar[i][l] == p:
                r=r + grammar[i][0]
            l = l+1
    return r
def concat(nonTerm,gram):
    r = nonTerm
    for i in range(0,len(gram)):
        if r.find(gram[i]) > len(r):
            r = r+gram[i]   
    print('CONCAT R ',r)     
    return r
        
        
                    
    
        
        
        
        


# In[ ]:


main()

