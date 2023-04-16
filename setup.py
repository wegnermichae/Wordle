import random

my_file = open("valid-wordle-words.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")
my_file.close()
listSize = len(data_into_list) 
targetWord = data_into_list[random.randint(0, listSize-1)] #generates the targeted word for the user to guess from the word list
notGuessed = True #initiated notGuessed to True to allow the game loop to run
guessCount = 0
targetWordList = list(targetWord)

while(notGuessed):
    print(targetWordList)
    if guessCount < 6:
        guess = input("Enter a guess: ")
    if len(guess) != 5:
        print("Not a valid guess, Please enter a guess that is 5 letters long")
    elif guess not in data_into_list:
        print("Not a word")
    elif guess == targetWord:
        print("Congrates you got it in " + str(guessCount) + " guesses!")
        notGuessed = False
    elif guessCount == 6:
        print()
        print("Max guesses reached!")
        print("GameOver")
        print("Target Word was: " + str(targetWord))
        notGuessed = False
    else:
        for i in range(len(guess)):
            if list(guess)[i] == targetWordList[i]:
                print(str(i+1) + "th letter is in correct location")
            elif targetWordList.__contains__(list(guess)[i]):
                print(str(i+1) + "th letter is in the word but not correct location")

        print(guess)
        guessCount = guessCount + 1
        notValidGuess = False
