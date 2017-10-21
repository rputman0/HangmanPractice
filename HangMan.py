from random import randint
import linecache

#read from text file to get random movie title
def getWord():
    fileName = ("movies.txt")
    movieNumber = randint(0,403) #the length of the file
    word = linecache.getline(fileName,movieNumber)
    word = word.rstrip('\n')

    return word

#abstract the word to the player
def convertToDashes(word):
    dashes = ""
    for i in range(len(word)):
        if(isSpecialCharacter(word[i])):
            dashes += word[i]
        else:
            dashes += "-"

    return dashes

def isSpecialCharacter(letter):
    isSpecial = False
    specialCharacters = " '!.,/&[]():0123456789"
    for i in range(len(specialCharacters)):
        if(specialCharacters[i] == letter):
            isSpecial = True
            break

    return isSpecial

def toString(guessList):
    return "".join(guessList)

def isEqualTo(guess,word):
    return guess == word

def main():
    print("HANGMAN - Guess the movie title in SIX tries")
    count,tries = 0,0
    wrong = ""
    isInWord = False
    
    word = getWord()
    dashes = convertToDashes(word)
    print(word)
    print(dashes)
    
    #python strings are immutable, use list() to change strings in place
    guess = list(dashes)

    #let the user guess
    while( not isEqualTo(guess,word) and tries <= 5):
        userGuess = input("User Guess: ")
            
        #let user guess the entire word, or just a letter
        if(len(userGuess) > 1 and isEqualTo(userGuess,word)):
            guess = word
            break
        elif(len(userGuess) == 1):
            letter = userGuess[0]
        else:
            letter = " " #catches wrong input
            print("Please guess a character or movie title\n")

        #check if the letter is in the word
        for i in range(len(word)):
            if(letter == word[i]):
                guess[i] = letter
                isInWord = True

        #check if the player's guess is right or wrong
        if(not isInWord):
            # var++ doesn't work in python
            count += 1
            tries += 1
            wrong += letter + ","
            print("Wrong Letter:",wrong)
            print("You have",(6-tries),"tries remaining")
        else:
            print("Correct Letter")
            isInWord = False #set the boolean back to false

        print(toString(guess))

    #Tell the player if he won or lost
    if(tries >= 5):
        print("You LOST! THE WORD WAS:",word)
    elif( isEqualTo(guess,word) and tries == 0):
        print("You WON WITH ZERO MISTAKES!!! THE WORD WAS:",word)
    elif( isEqualTo(guess,word) ):
        print("You Win!!! THE WORD WAS:",word)
        print("You had",tries,"mistakes")

main()
