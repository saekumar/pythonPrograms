#**kwargs:parameter that will pack all arguments into a dictionary
#   useful so that a function can accept a varying amount of keyword of argumen
def  helo(**kw):
    print("hello..!",end=" ")
    for key,value in kw.items():
        print(value,end=" ")
helo(tit="Mr..😎",name=" saikumar...",sirname="puppala")