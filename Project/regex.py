import re
import unittest
patterns = {'email':"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", 'mention': "(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9_]+)"}


def main():
    userInput = '1'
    while userInput == '1':
        userInput = input('Enter your string you would like to input: ')
        runChecks(userInput)
        userInput = input('Enter 1 to check another string or 0 to quit: ')

def runChecks(inputRun):
   for key, value  in patterns.items(): 
       if checkValid(value,inputRun): print(inputRun + ' is a valid '+ key)

def checkValid(pattern,checkInput ):
    return re.match(pattern,checkInput )




main()
