# M R
# June 21, 2026
# P2HW1
# Python String Programming 

print("This program calculates and displays travel expenses")

Location = str(input("Enter your travel destination\n"))
Initial_Budget = float(input("Enter Budget\n"))
Fuel = float(input("How much do you think you will spend on gas?:\n"))
Accomodation = float(input("Approximately, how much will you need for accomodation/hotel?\n"))
Food = float(input("Last, how much do you need for food?:\n"))

print("--------------Travel_Expenses--------------")
print(f"Location: {Location}")

labels = ["Initial Budget:", "Fuel:", "Accomodation:", "Food:"]
values = [Initial_Budget, Fuel, Accomodation, Food]
max_label_len = max(len(label) for label in labels)

for label, value in zip(labels, values):
    print(f"{label:<{max_label_len}} ${value:.2f}")

print("--------------------------------------------\n")

Remaining_Balance = Initial_Budget - Fuel - Accomodation - Food
print(f"{'Remaining Balance':<{max_label_len}} ${Remaining_Balance:.2f}")
      
