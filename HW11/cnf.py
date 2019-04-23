

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
    for c in range(0,len(clauses)-1):
        for j in range(1,len(clauses)):
            for vc in range(0,len(clauses[c])):
                for vj in range(0,len(clauses[j])):
                    
                    if clauses[c][vc] == clauses[j][vj]:
                        print(clause[c][vc-1]+clauses[j][vj-1])
                        if (clauses[c][vc-1] =='|' and clauses[j][vj-1] !='|'):
                            
                            temp = '('+clauses[c][:vc-1]+'V'+ clauses[c][vc+1:]
                            temp = temp + "V"+clauses[c][:vj]+clauses[c][vj+1:]+')'
                            resClause.append(temp)
                            temp =""
                        
                            newClause = True
                            


                        elif(clauses[c][vc-1] !='|' and clauses[j][vj-1] =='|'):
                       
                            temp = '('+clauses[j][:vj-1]+clauses[j][vj+1:]

                            temp = temp +"V"+clauses[c][:vj]+clauses[c][vj+1:]+')'
                         
                            resClause.append(temp)
                            temp =""
                        
                            newClause = True
                           
        if newClause == False:
            resClause.append(clauses[c])
        else:
            newClause == False
    if not resClause:
        print('unsatified')
    print(resClause)

                        
                            
                    
                            



main()