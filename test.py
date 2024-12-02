import pprint

class Test:
    def __init__(self, tokenizedWords):
        self.tokenizedWords = tokenizedWords
        self.dictionary = {}

    def populateDictionary(self):
        for i in range(len(self.tokenizedWords) - 1): # don't include the last word
            word = self.tokenizedWords[i]
            print (word)

if __name__ == "__main__":
    print ("Hello World")
    arr = ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness', 'it', 'was', 'the', 'epoch', 'of', 'belief', 'it', 'was', 'the', 'epoch', 'of', 'incredulity', 'it', 'was', 'the', 'season', 'of', 'light', 'it', 'was', 'the', 'season', 'of', 'darkness', 'it', 'was', 'the', 'spring', 'of', 'hope', 'it', 'was', 'the', 'winter', 'of', 'despair', 'we', 'had', 'everything', 'before', 'us', 'we', 'had', 'nothing', 'before', 'us', 'we', 'were', 'all', 'going', 'direct', 'to', 'heaven', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 'way', 'in', 'short', 'the', 'period', 'was', 'so', 'far', 'like', 'the', 'present', 'period', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 'insisted', 'on', 'its', 'being', 'received', 'for', 'good', 'or', 'for', 'evil', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only']
    test = Test(arr)
    # pprint.pprint (test.tokenizedWords)
    test.populateDictionary()

"""
def getDashOut(word):
    if "-" in word:
        print ("dash in word")
    else:
        print ("no dash in word")

def getDashOut2(word):
    if "--" in word:
        print ("Dash in Word: {}".format(word))
        i = 0
        for c in word:
            if c == '-':
                print ("Word 1 is: {}".format(word[:i]))
                print ("Word 2 is: {}".format(word[i+2:]))
                word1 = word[:i]
                word2 = word[i+2:]
                return [word1, word2]
            i += 1

    else:
        print ("no dash in word")
"""

"""
if __name__ == "__main__":
    words = getDashOut2("cat--person")
    print (words)
    getDashOut2("dog")
    getDashOut2("cat--person")
    getDashOut2("television")
    getDashOut2("make-shift")
    getDashOut2("hat")
"""
