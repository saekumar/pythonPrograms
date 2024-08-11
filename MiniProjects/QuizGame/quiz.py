print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("Who is the current prime minister of India? ").lower()
if answer == "narendra modi":
    print("Correct!")
else:
    print("Sorry! Try Again")
