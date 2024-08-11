# SET:COLLECTUON WHICH IS UNORDERED,UNINDEXED .NO DUPLICATE VALUES
kitchen = {"dishes", "tap", 1}
hall = {"sofa", "TV", "dining table"}
bedroom = {"bed", "love", "pillows"}
house = hall.union(kitchen).union(hall, bedroom)
for x in house:
    print(x)
for y in kitchen:
    print(y)
print(kitchen.difference(hall))
print(kitchen.intersection(bedroom))
