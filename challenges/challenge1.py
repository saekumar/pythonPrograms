#  Create a greeting for your program

#  Ask for the user for the name of a pet

#   Ask for the user for the name of a his city

#  Combine the pet name with the word cyber as a new twitter handle and then add the city they mentioned.

# The output should look like this "your new twitter handle and bio @cybercat from Delhi"


pet = str(input("Enter the name of pet: "))
city = str(input("Enter the name of your city: "))

twitterhandle = "@cyber" + pet
print(f"Your new Twitter handle is {twitterhandle} from {city}")
