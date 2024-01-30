# Strings are immutable we cannot alter the string values

string1 = str(input("enter a string: "))

# printing of strings
print(string1)

for i in string1:
    print(i, "~", end=" ")

print()

# concatenation
string2 = "hello"
print(string2 + " " + string1)

# We cannot change the string values
# string2[3] = "h"
# # this cannot be done...
# print(string2)
# we will get this error :
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Downloads\PythonTutorial\strings\traversing.py", line 18, in <module>
#     string2[3] = "h"
#     ~~~~~~~^^^
# TypeError: 'str' object does not support item assignment


# but we can do this like adding two or more strings and pointing to already presented string
string1 = "hi! " + string2 + " " + string1
print(string1)


# "in"  and "not in" functions

z = "hello"
# "in " returns true if sub string presents in string else false

print("a" in string1)
print("z" in string1)
print(z in string1)

# "not in " returns true if sub string is not in  string else false


print("a" not in string1)
print("z" not in string1)

print(z not in string1)


# "ord()" and "chr()" functions

# "ord()" function takes a char value as input and returns ascii value of that character
# "chr()" function tales integer value s input and returns character value of that integer

print(ord(string2[2]))
print(chr(65))
