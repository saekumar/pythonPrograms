import hashlib


def calculate(input_string):
    hash = hashlib.md5()
    hash.update(input_string.encode("utf-8"))
    hex = hash.hexdigest()
    return hex


input_string = str(input(" enter a string : "))
md5_res = calculate(input_string)
print("MD5 Result is " + md5_res)
