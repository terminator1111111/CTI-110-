# M R
# June 21, 2026
# P2HW2
# Python Dictionary Key-Value Pairs, Lists, and Min/Max Functions

#Have the user enter their grade for modules 1-6

Modules = {'Module_1': 0, 'Module_2': 0, 'Module_3': 0, 'Module_4': 0, 'Module_5': 0, 'Module_6': 0}

#Editing a Value for an Existing Key via user input

Module_1 = float(input("Enter grade for Module 1: "))
Module_2 = float(input("Enter grade for Module 2: "))
Module_3 = float(input("Enter grade for Module 3: "))
Module_4 = float(input("Enter grade for Module 4: "))
Module_5 = float(input("Enter grade for Module 5: "))
Module_6 = float(input("Enter grade for Module 6: "))

#Results are printed with min and max functions for length of the list

print("------------------Results------------------")
print(f"{'Lowest grade:':<30} {min(Module_1, Module_2, Module_3, Module_4, Module_5, Module_6):.2f}")
print(f"{'Highest grade:':<30} {max(Module_1, Module_2, Module_3, Module_4, Module_5, Module_6):.2f}")
print(f"{'Sum of all grades:':<30} {Module_1 + Module_2 + Module_3 + Module_4 + Module_5 + Module_6:.2f}")
print(f"{'Average grade:':<30} {(Module_1 + Module_2 + Module_3 + Module_4 + Module_5 + Module_6) / 6:.2f}")
print("------------------------------------------ ")



