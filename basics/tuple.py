#TUPLE:COLLECTION WHICH IS UNCHANGEABLE AND ORDERED USED TO GROUP TOGETHER RELATED DATA
student=("SAIKUMAR",2100032358,"MALE","CSE")
print(student.count("saikumar"))

for i in range(len(student)):
    print(student[i])
    
if "SAIKUMAR" in student:
    if "CSE" in student:
        print("YEAHH HE BELONGS TO CSE..")
        

    