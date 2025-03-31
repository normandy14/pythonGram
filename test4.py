# This is for a 2-Gram

tokenizedWords = ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']

superHash = {}

print ("----------------")
for i in range(len(tokenizedWords) - 2):
    currentWord = tokenizedWords[i]

    nextWord = tokenizedWords[i+1]
    nextNextWord = tokenizedWords[i+2]

    nextWords = nextWord + " " + nextNextWord

    print ("current word: {}".format(currentWord))
    # print ("next word: {}".format(nextWord))
    # print ("next next word: {}".format(nextNextWord))
    print ("next words: {}".format(nextWords))
    print ("----------------")

    if currentWord not in superHash:
        superHash[currentWord] = {}
        if nextWords not in superHash[currentWord]:
            superHash[currentWord][nextWords] = 1
            # print (superHash)
        else: # nextWord really is in superHash[currentWord]
            superHash[currentWord][nextWords] += 1
            # print (superHash)
    else:
        if nextWords not in superHash[currentWord]:
            superHash[currentWord][nextWords] = 1
            # print (superHash)
        else: # nextWord really is in superHash[currentWord]
            superHash[currentWord][nextWords] += 1

print (superHash)
