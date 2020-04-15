import random

words = ["soba", "dino", "alan", "aparat", "uzas", "neprijatelj", "otac", "jovan", "krevet", "deka", "fotograf", "advokat", "profesor", "ucenik", "klupa", "skola", "jasmin konic"]

word = random.choice(words)
wordList = []

pokusaj = 5
counter = len(word)
listOfLetters = []

doubleLetter = 0

for i in range(len(word)):
    if(word[i] == " "):
        wordList.append(" ")
        counter -= 1
    else:
        wordList.append("-")

win = "\n\n                             !!!!!    WIN    !!!!!\n"

print("Word is >> " + "".join(wordList))

while(pokusaj > -1):
    novoSlovo = input("Enter a letter : ")
    
    if(novoSlovo == word):
        print(win.center(120))
        break

    if((novoSlovo in word) and (novoSlovo not in listOfLetters)):
        listOfLetters.append(novoSlovo) 
        for i in range(len(word)):
            if(novoSlovo == word[i]):
                wordList[i] = novoSlovo
                print("Correct!, your result >> " + "".join(wordList))
                pokusaj += 1

        doubleLetter = wordList.count(novoSlovo)
        counter -= doubleLetter

    if(novoSlovo not in word):
        print("Miss, tries = " + str(pokusaj))

    if(counter < 1):
        print(win.center(120))
        break

    pokusaj -= 1