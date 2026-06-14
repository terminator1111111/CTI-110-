# M R
# June 14, 2026
# P1HW2
# calculate addition and subrtraction

print("This program calculates and displays travel expenses")

num1 = int(input("Enter your budget: "))
num2 = str(input("Enter your travel destination: "))
num3 = int(input("How much do you think that you will spend on gas? "))
num4 = int(input("Approximately, how much will you need for an accomodation/hotel? "))
num5 = int(input("Lastly, how much do you need for food? "))

print("-------------Travel Expenses--------------")
print("Location: ", num2)
print("Initial Budget: ", num1)

print("Fuel", num3)
print("Accomodation: ", num4)
print("Food: ", num5)

print("Remaining Balance: ", num1 - num3 - num4 - num5)

