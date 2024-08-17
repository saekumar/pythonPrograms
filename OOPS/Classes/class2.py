import re

print(["vowel" if ch in "aeiou" else "consonant" for ch in input("")])


# def check(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     return sum


# def che(n):
#     return sum(int(digit) for digit in str(n))


def onlyChars(s):
    res = re.sub(r"[]", "", s)
    print(res)


# res = che(2245)
# print(res)

onlyChars("Hello123!@# World456$%^")
