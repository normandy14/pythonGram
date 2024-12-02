# Open file
# Hold as text
# Seperate using space

# remove commas and periods and odd punctuation

DEBUG = True
DEBUG2 = True

def removeCharAtEnd(word):
    print (word[-1])
    print (word[-1].isalpha())
    # if (word[-1].isalpha() != )

def main():
    print ("Hello World")

    text = ""
    with open("taleSmall.txt") as file:
        text = file.read()
    # print (text)
    arr = text.split()
    arrString = []
    for word in arr:
        print (word)
        word2 = word.strip()
        print (word2)
        arrString.append(word)

    # if (DEBUG): print (arr)
    if (DEBUG2): print (arrString)

if __name__ == "__main__":
    # main()
    removeCharAtEnd("Hello")
