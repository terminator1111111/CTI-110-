# M R
# June 27, 2026
# P3LAB
# Python Branching Structures

# This program will demonstrate the use of branching structures in Python.
# Using the // operator | Integer Division

#Get value from user
change = float(input("Enter an amount of money: $"))
print(f"Change Amount: ${change}")

#Converting the value to an integer
#This will allow us to break down each decimal place into a "key value" pair
#The // operator will break down from the largest value to the smallest value
#The largest value is the dollar in our bracketing logic. The smallest value is the penny.
change = round(change * 100)
print(f"Change Amount in cents (centi-based system): {change}")

#This is why we are using the // operator followed by "100" cent-based value to divide the keys by their proper values.
#Determine how many coins are needed
num_dollars = change // 100
change = change -(num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change 

#Use "if" , "else" statements to determine how we are going to print these numbers out 
if num_dollars > 0: 
    if num_dollars == 1:
        print(f"{num_dollars} Dollar") 
    else: 
        print(f"{num_dollars} Dollars")
if num_quarters > 0: 
    if num_quarters == 1:
        print(f"{num_quarters} Quarter") 
    else: 
        print(f"{num_quarters} Quarters")
if num_dimes > 0: 
    if num_dimes == 1:
        print(f"{num_dimes} Dime") 
    else: 
        print(f"{num_dimes} Dimes")
if num_nickels > 0: 
    if num_nickels == 1:
        print(f"{num_nickels} Nickel") 
    else: 
        print(f"{num_nickels} Nickels")
if num_pennies > 0: 
    if num_pennies == 1:
        print(f"{num_pennies} Penny") 
    else: 
        print(f"{num_pennies} Pennies")
