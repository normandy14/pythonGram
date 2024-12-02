# Open file
# Hold as text
# Seperate using space

# remove commas and periods and odd punctuation

DEBUG = False
DEBUG2 = False
DEBUG3 = True
DEBUG4 = False

# Future Bug:  if its way-- and check if [-1] is -, then check word [-2] for -, and then remove

def removeCharAtEnd(word):
    if (DEBUG4): print (word[-1])
    if (DEBUG4): print (word[-1].isalpha())
    if (word[-1].isalpha() != True):
        word = word[:-1]
    if (DEBUG4): print (word)
    return word

def main():
    text = ""
    with open("taleSmall.txt") as file:
        text = file.read()
    # print (text)
    arr = text.split()
    arrString = []
    for word in arr:
        # word = word.strip() # an extra precaution
        if (DEBUG3): print ("word before is: {}".format(word))
        newWord = removeCharAtEnd(word)
        if (DEBUG3): print ("word after is: {}".format(newWord))
        arrString.append(word)

    # if (DEBUG): print (arr)
    if (DEBUG2): print (arrString)

if __name__ == "__main__":
    main()
    # removeCharAtEnd("Hello!")
