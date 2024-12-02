

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

if __name__ == "__main__":
    words = getDashOut2("cat--person")
    print (words)
    getDashOut2("dog")
    getDashOut2("cat--person")
    getDashOut2("television")
    getDashOut2("make-shift")
    getDashOut2("hat")
