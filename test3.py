tokenizedWords = ["cat", "dog", "cat", "dog", "cat", "dog", "elephant", "dog"]

superHash = {}

for i in range(len(tokenizedWords) - 1):
    currentWord = tokenizedWords[i]
    # print (currentWord)

    nextWord = tokenizedWords[i+1]
    # print (nextWord)

    if currentWord not in superHash:
        superHash[currentWord] = {} # to get to {'cat': {}}
        if nextWord not in superHash[currentWord]:
            superHash[currentWord][nextWord] = 1
            # print (superHash)
        else: # nextWord really is in superHash[currentWord]
            superHash[currentWord][nextWord] += 1
            # print (superHash)
    else:
        if nextWord not in superHash[currentWord]:
            superHash[currentWord][nextWord] = 1
            # print (superHash)
        else: # nextWord really is in superHash[currentWord]
            superHash[currentWord][nextWord] += 1
            # print (superHash)

print (superHash)
print (superHash['cat'])
