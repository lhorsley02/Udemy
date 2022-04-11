# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if you are 20 years old, you have 70 years left.
# to get months, multiply 70 by 12
# to get weeks, multiply 70 by 52
# do get days, multiply 70 by 365

yrs_left = 90 - int(age)
# print(yrs_left)
months = yrs_left * 12
weeks = yrs_left * 52
days = yrs_left * 365


print(f"You have {days} days, {weeks} weeks, and {months} months left.")