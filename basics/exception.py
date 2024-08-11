try:
    numera=int(input("enter a nmbr to divide: "))
    denomi=int(input("enter a nmbr to divide by: "))
    res=numera/denomi
except ZeroDivisionError as k:
    print(k)
    print("U CANT WRITE DENOMINATOR AS 0 YOU IDOTT...😒")
except ValueError as k:
    print(k)
    print(" DONT UU KNOW TO ENTER ONLY NMBRS...🤷‍♂️😪")
except Exception:
    print("THERE IS SOMETHING WENT WRONG..😪")
else:
    
    print("Result is "+str(res))
finally:
    print("I WILL BE ALWAYS WITH UU..💖💋")
