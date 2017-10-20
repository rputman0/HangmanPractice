from random import randint
import linecache

def main():
    print("HANGMAN - Guess the movie title in FIVE tries")

    #read from text file to get random title
    fileName = ("movies.txt")
    word = linecache.getline(fileName, randint(0,400))
    #print(word)

    #abstract the word to the player
    dashes = ""
    for i in range(len(word)):
        if(word[i] == " "):
         dashes += " "
        else:
         dashes += "-"

    print(dashes)

    #python strings are immutable
    #use list() to change strings in place
    guess = list(dashes)

    count = 0
    tries = 0
    wrong = ""
    isInWord = False

    #let the user guess
    while("".join(guess) != word and tries  <= 5):
        userGuess = input("User Guess: ");

        #let user guess the entire word
        if(len(userGuess) > 1 and userGuess == word):
            guess = word
            break
        else:
            letter = userGuess[0]

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

        print("".join(guess))

    #Tell the player if he won or lost
    if(tries >= 5):
        print("You LOST! THE WORD WAS:",word)
    elif("".join(guess) == word):
        print("You Win!!! THE WORD WAS:",word)
        print("You had",tries,"mistakes")

main()
