fruits = ["apple", "mango", "guava", "banana"]

for i in fruits:
    print(i)


for i in range(1, 20):
    print(i * 6)


for i in range(0, 28, 3):
    print(i)


# fizz buzz

for i in range(1, 100):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    else:
        pass
