#str.format()=optional method that gives users more control when displaying output
animal="cow"
item="moon"
print("the "+animal+"jumped over the "+item)
print("the {} jumped over the {} ".format(animal,item))
print("the {} jumped over the {} ".format("cow","moon"))
te="the {} jumped the over {} "
print(te.format(animal,item))
print("HEllo my name is {:10}. hiii...its nice to meet uu..".format(animal))