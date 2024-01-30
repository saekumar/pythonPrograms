# Methods are mainly

list1 = [45, 12, 23, 56, 78, 89, 46, 16, 75, 169]

# append(item)
list1.append(745)
print(list1)
# inserts item to the end of the list.Just updates doent create a new list

# del list[n:m]  ===> deletes particular elements from n to m indices
del list1[8:10]
print(list1)


# Maing copy

k = list1
print(k)  # but it doesn't copy the list it just ppints to the original list,So
k = list(list1)  # this creates another copy of original list
print(k)
