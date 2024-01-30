# lists are similar to Strings .but the key difference is lists are mutable .
# Lists are standard data type  and mutable .

# creating lists :
list1 = list(input("Enter a List : "))

print(list1)
# by this method only single elemant can be accessed
# ex ==> i/p:- 45 56 89 12
#        o/p:- ['4', '5', ' ', '5', '6', ' ', '8', '9', ' ', '1', '2']

# general we execute like this using eval method.
# input should be given in '[]' with "," for each element.
list2 = eval(input("Enter a list : "))


print(list2)
# most functiomns are simlar to strings like concatenation,replicating, slices.

# Slicing in lists:
list3 = ["hello", "Iam", "Saikumar", "Hope", "You are", "doing well"]
print(list3[1:4])
