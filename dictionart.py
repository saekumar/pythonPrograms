#DICTIONARY:A changeable,unorderd collection of unique key:value pairs
#fast because they using hashing ,allow us to access a value quickly
capitals={'usa':'wasington','india':'delhi','china':'beijing','russia':'moscow'}
print(capitals['india'])
print(capitals.get('germany'))
print(capitals.keys())
print(capitals.items())
print(capitals.update({'germany':'berlin'}))
for key,value in capitals.items():
     print(key,value)


    