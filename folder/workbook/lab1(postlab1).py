import datetime


birthdate_str = input("Enter your birthdate (yyyy-mm-dd): ")
birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')

now = datetime.datetime.now()
age = now - birthdate
years = age.days // 365
days = age.days % 365
hours, remainder = divmod(age.seconds, 3600)
minutes, seconds = divmod(remainder, 60)


print(f"You are {years} years, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old.")


color = input("What is your favorite color? ")
print(f"{color} is a great color! It can be calming, energizing, or even romantic, depending on the shade. What do you like most about {color}?")
