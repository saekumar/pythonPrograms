# The main functions are l.index(item),l.append(item),l.extend(l2),
# l.insert(pos,item),l.pop(),l.remove(item),l.clear(),l.count(),l.reverse(),l.sort()


list1 = [45, 2, 12, 23, 456, 78, 89, 7, 79, 42, 53, 62, 51, 84]
list2 = [123, 456, 897, 753, 753, 753]


print(list1)
print(list2)

k = list1.index(45)
print(k)

list1.append(7548)
print(list1)


list1.extend(list2)
print(list1)

list1.insert(3, 1452)
print(list1)

list2.pop()
print(list2)


list1.remove(78)
print(list1)

c = list2.count(753)
print(c)

list1.reverse()
print(list1)

list2.sort()
print(list2)
