#copyfile()=copies content of a file
#copy()=copyfile()+permission mode+destination can be a directory
#copy2()=copy()+copies metadata(files creation and modification times)
import shutil
shutil.copyfile('sai.txt','copy.txt')
shutil.copy()