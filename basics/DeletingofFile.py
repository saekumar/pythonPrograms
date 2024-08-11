import os
import shutil
path="folder1"
pa="folder\\copy.txt"
try:
    os.remove(pa)
    #os.rmdir(path)
    shutil.rmtree(path)#IT WILL DEL A DIRECTORY WITH ANY NO.OF FILES AND DATA

except FileNotFoundError:
    print("FILE NOT EXISTS...")
except PermissionError:
    print(" U HAVE TO USE os.rmdir() TO DEL EMPTY FOLDER.. OR HAVE TO IMPORT SHUTIL ND USE shutil.rmtree() to delete all files..")