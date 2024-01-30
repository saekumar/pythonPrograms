#args:parameter that will pack all arguments into a tuple
#   useful so that a function can accept a varying amount of arguments
def add(*args):
    s=0
    print(args[0])
    for i in args:
        s+=i
    return s
print(add(1,2,3,5)) 