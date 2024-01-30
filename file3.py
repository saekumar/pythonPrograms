try:
    with open('C:\\Users\\ASUS\\Downloads\\PythonTutorial\\fre.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("There is no such file...")