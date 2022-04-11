#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_inp = input("What was to total bill?\n$")
tip_inp = input("How much tip would you like to give? 10%, 12%, or 15%?\n%")
people_inp = input("How many people to split the bill?\n")

# Total should be divided by people_inp, then multiplied by tip_inp to show total for each person
# Create variables for nums

total = float(total_inp)
tip = float(tip_inp)
people = int(people_inp)

# first tip should be calculated, tip / 100 then multiplied by total_inp
tip_calc = tip / 100
tip_final = tip_calc * total

# Calculate final bill
final_bill = total + tip_final

# Divide among people
per_person = final_bill / people

# Print total per person
should_print = (round(per_person, 3))
print(f"Each person should pay: ${should_print}")