
class Tape():
    
  
    def __init__(self, initialString, initialPos=0, blank="_"):
    
        self.initialString= initialString
        self.tape = setUpTape(initialString)
 
    
class Transition():
       def __init__(self, curChar, direction,replaceChar):
    
        self.curChar= curChar
        self.replaceChar = replaceChar
        self.direction = direction

def main():
    t = Tape('')
    t2 = Tape('#this#this')

    runSimulation(t.tape)
    print('--------------')
    runSimulation(t2.tape)
def runSimulation(newTape):
    pos = 0
    newTape.append('|_|')
    state1(newTape,pos)

def state1(word,pos):
    print('State 1')

    if(len(word)==1):
        print('empty string')
        accept('1', '|_|')
    elif(word[pos]=='#'):
        
        transition1to2(word, pos)
    else:
        reject('1', word)

def transition1to2(word,pos):
    print('Transition # ---> X , R')
    word[pos]='X'
    pos = pos +1
    state2(word, pos)
def transition2to3(word,pos):
    print('Transition '+word[pos] +' --->'+word[pos]+' , R')
    pos = pos +1
    state3(word, pos)
    
def state2(word, pos):
    print('State 2')
    printLocation(pos, word)
    transition2to3(word,pos)

def state3(word,pos):
    print('State 3')
    for x in range(pos,len(word)):
        printLocation(x, word)
        if word[pos-1]==word[x]:
            reject('3',word)
            break
        elif word[x]=='|_|':
            transiton3to4(word,x)
def transiton3to4(word, pos):
    print('Transition '+word[pos] +' ---> L')
    pos = pos-1





def printLocation(pos, word):
    print('Looking at '+word[pos]+ ' at index '+str(pos))


def accept(previousState,word):
        print('ACCEPT AFTER STATE:'+ previousState )
        print('Final Output of Tape: ')
        print(word)
def reject(previousState,word):
        print('REJECT AFTER STATE: ' + previousState)
        print('Final Output of Tape: ')
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





