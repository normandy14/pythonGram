# Open file
# Hold as text
# Seperate using space

# remove commas and periods and odd punctuation
# look out for special -- condition
# an even more special case: way--in

# The next part:
# Some type of dictionary
# What about edge case: the last word? # maybe it isn't logged in the dictionary

# Remember to manage:
# with open("taleSmall.txt") as file:
# with open("taleMed.txt") as file:
# its best to use taleSmall.txt in the beginning

import pprint

DEBUG = False
DEBUG2 = False
DEBUG3 = False
DEBUG4 = False
DEBUG5 = False
DEBUG6 = False
DEBUG7 = True

# Future Bug:  if its way-- and check if [-1] is -, then check word [-2] for -, and then remove

class App:
    def __init__(self, fileName):
        self.tokenizedWords = []
        self.fileName = fileName
        self.oneGramDict = None


    def seperateDashWords(self, word):
        i = 0
        for c in word:
            if c == '-':
                if (DEBUG6) : print ("Word 1 is: {}".format(word[:i]))
                if (DEBUG6) : print ("Word 2 is: {}".format(word[i+2:]))
                word1 = word[:i]
                word2 = word[i+2:]
                return [word1, word2]
            i += 1

    def removeCharAtEnd(self, word):
        if (DEBUG4): print (word[-1])
        if (DEBUG4): print (word[-1].isalpha())
        if (word[-1].isalpha() != True):
            word = word[:-1]
            if (DEBUG4): print (word)
        return word

    def makeLowerCase(self, word):
        word = word.lower()
        return word

    def app(self):
        text = ""
        with open(self.fileName) as file:
            # with open("taleMed.txt") as file:
            text = file.read()
        # print (text)
        arr = text.split()
        arrString = []
        for word in arr:
            # print (word)
            if (DEBUG3): print ("word before transformation is: {}".format(word))
            newWord = self.removeCharAtEnd(word)
            if (DEBUG3): print ("word after remove at end is: {}".format(newWord))
            newWord2 = self.makeLowerCase(newWord)
            # if (DEBUG4): print ("word after lowercase is: {}".format(newWord2))
            arrString.append(newWord2)
        if (DEBUG5): print (arrString)
        arrString2 = []
        for word in arrString:
            if "--" in word:
                if (DEBUG6) : print ("Dash in Word: {}".format(word))
                words = self.seperateDashWords(word)
                arrString2.append(words[0])
                arrString2.append(words[1])
            else:
                arrString2.append(word)
        if (DEBUG6) : print (arrString2)
        # if (DEBUG7) : pprint.pprint(arrString2)
        self.tokenizedWords = arrString2

    def makeOneGram(self):
        tokenizedWords = self.tokenizedWords
        self.oneGramDict = {}

        for i in range(len(tokenizedWords) - 1):
            currentWord = tokenizedWords[i]
            # print (currentWord)

            nextWord = tokenizedWords[i+1]
            # print (nextWord)

            if currentWord not in self.oneGramDict:
                self.oneGramDict[currentWord] = {} # to get to {'cat': {}}
                if nextWord not in self.oneGramDict[currentWord]:
                    self.oneGramDict[currentWord][nextWord] = 1
                    # print (oneGramDict)
                else: # nextWord really is in oneGramDict[currentWord]
                    self.oneGramDict[currentWord][nextWord] += 1
                    # print (oneGramDict)
            else:
                if nextWord not in self.oneGramDict[currentWord]:
                    self.oneGramDict[currentWord][nextWord] = 1
                    # print (oneGramDict)
                else: # nextWord really is in oneGramDict[currentWord]
                    self.oneGramDict[currentWord][nextWord] += 1
        # print (self.oneGramDict)


if __name__ == "__main__":
    app = App("taleSmall.txt")
    app.app()
    # pprint.pprint(app.tokenizedWords)
    # print (app.tokenizedWords)
    app.makeOneGram()
    print (app.oneGramDict)
