string = str(input("Enter a String : "))
# let string ="hello saikumar",

# String Slice: if we give string[n:m] where n and m are integers it will return sub string from index 'n' to 'm'.

k = string[2:5]

print(k)
# it will return "llo"(index values of 2,3,4).

z = string[27:35]
print(z + " " + str(len(z)))
# if we give out of bound indices it will return empty string and its length will be "0"


# note:for any integer n string[:n]+string[n:] will return original string
# Example:

print(str(string[:-7] + string[-7:]))
# returns originl string


# easy way to reverse a string string[: : -1]
print(string[::-1])
