#  Create a greeting for your program

# Create a word List
# randomly choose a word from the list you have created
#  ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in that random word
import random

print("Hello there!,Welcome to Cyber Challenges ")

wordList = ["Saikumar", "Lokesh", "Ganesh", "Manikanta", "Raju", "Teja", "Pradeep"]

randomWord = random.choice(wordList)
print(randomWord)

letter = str(input("Guess a letter ")).lower()

print(letter)
for i in randomWord:
    if i == letter:
        print("Right")
        break
else:
    print("Wrong")
