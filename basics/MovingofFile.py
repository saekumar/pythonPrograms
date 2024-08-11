import os
import shutil
src="sai.txt"
des="C:\\Users\\ASUS\\Desktop\\sai.txt"
try:
    if os.path.exists(des):
        
        print("FILE ALREADY EXISTS...✌")
        
       
    else:



        os.replace(src,des)
        print(src+" NOW IT IS REPLACED..U CAN CHECK IT..😎")



except FileNotFoundError:
    print(src+" ITS  NOT HERE...ERROR 404 🤷‍♂️")

