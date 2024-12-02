# Open file
# Hold as text
# Seperate using space

# remove commas and periods and odd punctuation
# look out for special -- condition
# an even more special case: way--in

DEBUG = False
DEBUG2 = False
DEBUG3 = False
DEBUG4 = False
DEBUG5 = True
DEBUG6 = True

# Future Bug:  if its way-- and check if [-1] is -, then check word [-2] for -, and then remove

def seperateDashWords(word):
    i = 0
    for c in word:
        if c == '-':
            if (DEBUG6) : print ("Word 1 is: {}".format(word[:i]))
            if (DEBUG6) : print ("Word 2 is: {}".format(word[i+2:]))
            word1 = word[:i]
            word2 = word[i+2:]
            return [word1, word2]
        i += 1

def removeCharAtEnd(word):
    if (DEBUG4): print (word[-1])
    if (DEBUG4): print (word[-1].isalpha())
    if (word[-1].isalpha() != True):
        word = word[:-1]
    if (DEBUG4): print (word)
    return word

def makeLowerCase(word):
    word = word.lower()
    return word

def main():
    text = ""
    with open("taleSmall.txt") as file:
        text = file.read()
    # print (text)
    arr = text.split()
    arrString = []
    for word in arr:
        print (word)
        if (DEBUG3): print ("word before transformation is: {}".format(word))
        newWord = removeCharAtEnd(word)
        if (DEBUG3): print ("word after remove at end is: {}".format(newWord))
        newWord2 = makeLowerCase(newWord)
        # if (DEBUG4): print ("word after lowercase is: {}".format(newWord2))
        arrString.append(newWord2)
    if (DEBUG5): print (arrString)
    '''
    arrString2 = []
    for word in arrString:
        if "--" in word:
            if (DEBUG6) : print ("Dash in Word: {}".format(word))
            words =  seperateDashWords(word)
            arrString2.append(words[0])
            arrString2.append(words[1])
        else:
            arrString2.append(word)
    if (DEBUG6) : print (arrString2)
    '''

if __name__ == "__main__":
    main()
    # removeCharAtEnd("Hello!")
