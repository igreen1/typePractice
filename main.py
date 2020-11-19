"""
I made a very hacky program to practice my typing
Made this is less than 20 minutes so ,,, its HACKY
"""

import linecache
import random
import msvcrt #this will only work on windows :/ 
import math
import datetime

MAXLINE = 292132
FILENAME = "words.txt"

#TODO add backspace for incorrect types
#otherwise, it like,, works lol

def main():
      while(True): #I'm hacking this together to practice my typing. CTRL+C to exit ha
            #create a sentence to type
            sentenceArr = []
            for i in range(0,random.randint(6,10)):
                    sentenceArr.append(linecache.getline("words.txt", random.randint(0,MAXLINE)).rstrip())
                    sentenceArr.append(" ")
            #find number of words
            numOfWords = len(sentenceArr)
            #turn array into one string
            sentence = ''.join(sentenceArr)
            sentence = sentence.rstrip() # Remove the space at the end
            print("\n\n")
            print(sentence)
            
            #ask user to type
            done = False
            currChar = 0
            correct = 0
            incorrect = 0
            start_time = datetime.datetime.now()
            while(currChar < len(sentence)):
                #wait for user input
                userIn = str(msvcrt.getwch()) #grabs on character and echoes it
                if ( userIn == '\000' or userIn == '\xe0' ) : 
                    continue
                elif ( userIn == '\x03' ):
                    return
                elif ( userIn == sentence[currChar] ): #correct
                    msvcrt.putwch(userIn)
                    correct += 1
                    currChar += 1
                else:
                    incorrect += 1
            end_time = datetime.datetime.now()
            print(f"\nCorrect Rate {math.floor(100*correct/(incorrect+correct))}")
            deltaT = ((end_time-start_time).total_seconds())/60 #in minutes
            print(f"WPM: {numOfWords/deltaT}")
          
          
if __name__ == "__main__":
    main()