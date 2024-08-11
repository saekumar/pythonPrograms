# [print(ch + "") for ch in input("") if ch not in "aeiou"]


# li = [ch if ch not in "aeiou" else "k" for ch in "saikumar"]
# print(li)


print([(ord(ch) - ord("a") + 1) if ch in "aeiou" else ch for ch in input("")])
