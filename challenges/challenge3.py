#  Create a greeting for your program

# Create a word List
# randomly choose a word from the list you have created
# replace every letter in the word with "_".
#  ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in that random word
# if it is replace the "-" with that guessed letter

import random

print("Hello there!,Welcome to Cyber Challenges ")

wordList = ["Saikumar", "Lokesh", "Ganesh", "Manikanta", "Raju", "Teja", "Pradeep"]

randomWord = random.choice(wordList)
print(randomWord)
empty = []
for lett in randomWord:
    empty += "_"

num = 0

gameOver = False
while not gameOver:
    guess = str(input("Guess a letter "))
    if guess not in randomWord:
        num += 1
        if num >= 5:
            print(f"You took {num} chances.")
            print("You Lose")
            gameOver = True
    for i in range(len(randomWord)):
        lett = randomWord[i]
        if lett == guess:
            empty[i] = lett

    print("".join(empty))
    if "_" not in empty:
        print("You win")
        gameOver = True
