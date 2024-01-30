import os
pa="C:\\Users\\ASUS\\Documents\\text1.txt"
if os.path.exists(pa):
    print(" YESS...IT EXISTS")
    if os.path.isfile(pa):
        print("IT IS OF FILE TYPE..")

    elif os.path.isdir(pa):
        print("IT IS A FOLDER...")

else:
    print("NO IT DOESNT EXIST..")