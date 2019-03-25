
class Tape():
    def __init__(self, initialString=[], initialPos=0, blank="_"):
        self.initialString= initialString
        self.tape = setUpTape(initialString)
 
    
    def setUpTape(initWord):
        tapeArray = []
        strBuilder = ''
        i = 0
        if initWord=='':
            return tapeArray
        for character in initWord:
            if(character == '#'):
                tapeArray.append('#')
                i = i+1
            else:
                strBuilder = strBuilder + character
                if(len(initWord)==i-1 or initWord[i+1]=='#'):
                    tapeArray.append(strBuilder)
                i = i+1
        print (tapeArray)
        return tapeArray


