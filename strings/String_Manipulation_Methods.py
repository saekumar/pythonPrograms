# some in built string mnipulation methods

# string.capitalize() ==> return string with first char capitalized

string = str(input("Enter a String : "))
# string ="hello saikumar"
print(string.capitalize())
# Hello saikumar

# string.find(sub,m,n) ==> returns lowest index of string where sub string sub is found within the slicerange
# if not found returns -1

print(string.find("hello", 0, 9))
# returns 0

# strinng.isalnum()===> returns true if the characters in string are alpha or nummeric
# string.isalpha()====> returns true if the characters in string are alphabets
# string.isdigit() ====> returns true if chars are numeric

string2 = "HelloSaikumar1234"
print(string2.isalnum())  # returns True
print(string2.isdigit())  # returns False
print(string2.isalpha())  # returns False

# string.islower() ==>returns true if all chars in string are lower
# string.isupper() ==> returns true if all chars in string are upper

print(string.islower())
print(string.isupper())
print()
print(string2.islower())  # False
print(string2.isupper())  # False


# strng.lower()==> returns a copy string that converts all chars in original string with lower case
# strng.upper()==> returns a copy string that converts all chars in original string with upper case
print(string2.lower())

print(string2.upper())


# string.lstrip(arg) ===>removes all possible sun strings of args in the string from leading side like left side
# string.rstrip(arg) ===>removes all possible sun strings of args in the string from rear side like right side


string3 = "saregamapadanisa"
print(
    string3.rstrip("nisa")
)  # returns "saregamapada" as sub string "nisa" itself is on right side of string3.
