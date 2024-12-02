import pprint

class Test:
    def __init__(self, tokenizedWords):
        self.tokenizedWords = tokenizedWords
        self.dictionary = {}

    def populateDictionary(self):
        for i in range(len(self.tokenizedWords) - 1): # don't include the last word
            word = self.tokenizedWords[i]
            nextWord = self.tokenizedWords[i+1]
            print ("word is : {}".format(word))
            print ("nextWord is : {}".format(nextWord))
            if word not in self.dictionary:
                self.dictionary[word] = {}
            # next Part
            if nextWord in self.dictionary[word]:
                self.dictionary[word][nextWord] += 1
            else:
                self.dictionary[word][nextWord] = 1



if __name__ == "__main__":
    """
    dict = {}
    dict["it"] = {
        "was" : 1
    }
    print(dict["it"])
    print(dict["it"]["was"])
    dict["it"]["has"] = 1
    print(dict["it"])
    dict["it"]["has"] += 1
    print(dict["it"])
    if "was" in dict["it"]:
        print ("'has' really is in 'it'")

    print (myFamily["it"]["was"])
    myFamily["it"]["was"] += 1
    print (myFamily["it"]["was"])
    myFamily = {
        "hello" : {
            "world" : 1
        }
    }
    print (myFamily["hello"])
    myFamily["hello"]["bye"] = 1
    print (myFamily)
    """

    print ("Hello World")
    arr = ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of']
    test = Test(arr)
    # pprint.pprint (test.tokenizedWords)
    test.populateDictionary()
    pprint.pprint(test.dictionary)
    """
    myFamily = {
        "it" : {
            "was" : 2
        }
    }
    # pprint.pprint (myFamily)
    # figure out to update from in here
    """
