
class Tape():
    
  
    def __init__(self, initialString, initialPos=0, blank="_"):
    
        self.initialString= initialString
        self.tape = setUpTape(initialString)
 
    

def main():
    t = Tape('')
    t2 = Tape('this will fail yay')
    runSimulation(t.tape)
    runSimulation(t2.tape)
def runSimulation(newTape):
    pos = 0
    state1(newTape,pos)

def state1(word,pos):
   
    if(len(word)==0):
        accept('1', '|..|')
    elif(word[pos]=='#'):
        print('working on it')
    else:
        reject('1', word)
        
def accept(previousState,word):
        print('ACCEPT AFTER STATE:'+ previousState )
        print('Final Output of Word: ')
        print(word)
def reject(previousState,word):
        print('REJECT AFTER STATE: ' + previousState)
        print('Final Output of Word: ')
        print(word)
    
def setUpTape(initWord):
        tapeArray = []
        strBuilder = ''
        i = 0
        last =0
        if initWord=='':
            return tapeArray
        for character in initWord:
            if(character == '#'):
                tapeArray.append('#')
               
                i = i+1
                last =i
            else:
                strBuilder = strBuilder + character
                i = i+1
                if(len(initWord)==i):
                    tapeArray.append(strBuilder)
                    
                elif(initWord[i]=='#'):
                    tapeArray.append(strBuilder)
                    strBuilder=''
               
    
        return tapeArray
main()





