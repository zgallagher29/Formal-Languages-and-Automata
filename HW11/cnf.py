

def main():
    clause = '(AVB)^(|BVC)'
    clauses = []
    clauseBuilder = ''
    for i in range(0,len(clause)):
        if clause[i] == ')':

            clauses.append(clauseBuilder)
            clauseBuilder=""
        elif clause[i] == '^'or clause[i]=='(' or clause[i]=='V':
            continue
        else:
            clauseBuilder = clauseBuilder+clause[i]

    resClause = []
    newClause = False
    for c in clauses:
        for j in range(1,len(clauses)-1):
            for vc in range(0,len(c)):
                for vj in range(0,len(clauses[j])):
                    if c[vc] == clauses[j][vj]:
              
                        if (c[vc-1] =='|' and clauses[j][vj-1] !='|'):
                            
                            temp = c.replace(c[vc-1],"")
                            temp = temp +clauses[j]
                            temp = temp.replace(c[vc],"")
                        
                            resClause.append(temp)
                            temp =""
                        
                            newClause = True
                            


                        elif(c[vc-1] !='|' and clauses[j][vj-1] =='|'):
                            temp = clauses[j].replace(clauses[j][vj-1],"")
                            temp = temp +clauses[j]
                            temp = temp.replace(c[vc],"")
                            newClause = True
                           
        if newClause == False:
            resClause.append(c)
        else:
            newClause == False

    print(resClause)

                        
                            
                    
                            



main()