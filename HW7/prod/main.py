
class Tape():
    
  
    def __init__(self, initialString, initialPos=0, blank="_"):
    
        self.initialString= initialString
        self.tape = setUpTape(initialString)
 

def main():
    t = Tape('')
    t2 = Tape('#10#111#10#111111')
    t3 = Tape('#1000#100101#100#111111111#000000')
    t4 = Tape('#100101')
    runSimulation(t.tape)
    print('--------------')
    runSimulation(t2.tape)
    print('--------------')
    runSimulation(t3.tape)
    print('--------------')
    runSimulation(t4.tape)

def runSimulation(newTape):
    pos = 0
    newTape.append('|_|')
    state1(newTape,pos)

def state1(word,pos):
    print('')
    print('State 1')
    print(word)
    if(word[pos]=='|_|'):
        accept('1', word)
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
    print('')
    print('State 2')
    print(word)
    printLocation(pos, word)
    if(word[pos]=='|_|'):
        reject('2',word)
    else:
        transition2to3(word,pos)

def state3(word,pos):
    print('')
    print('State 3')
    print(word)
    for x in range(pos,len(word)):
    
        printLocation(x, word)
        if word[pos-1]==word[x]:
            reject('3',word)
            break
        elif word[x]=='|_|':
            transiton3to4(word,x)
            break
    
def transiton3to4(word, pos):
    print('Transition '+word[pos] +' ---> L')
    pos = pos-1
    state4(word,pos)

def state4(word,pos):
    print('')
    print('State 4')
    print(word)
    printLocation(pos, word)
    for i in range(pos,-1,-1):
        
        
        if(word[i]=='X'):
            pos=i
            transition4to5(word, pos)
            break
            
def transition4to5(word,pos):
    print('Transition '+word[pos] +' --->'+word[pos] + ', R')
    pos = pos+1
    state5(word,pos)

def state5(word,pos):
    print('')
    print('State 5')
    print(word)
    printLocation(pos, word)
    if word[pos] == 'X':
        accept('5', word)
    else:
        transition5to1(word,pos)
def transition5to1(word,pos):
     print('Transition '+word[pos] +' ---> X' + ', R')
     word[pos]='X'
     pos = pos+1
     state1(word,pos)




def printLocation(pos, word):
    print('Looking at '+word[pos]+ ' at index '+str(pos))


def accept(previousState,word):
        print('')
        print('ACCEPT AFTER STATE:'+ previousState )
        print('Final Output of Tape: ')
        print(word)
def reject(previousState,word):
        print('')
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





