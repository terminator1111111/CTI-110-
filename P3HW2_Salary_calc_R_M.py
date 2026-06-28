#P3HW2
#Salary Calculator
#R_M
#June 28, 2026

#request employee info
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))


#Evaluate Overtime
if hours > 40:
    #Caculate Overtime
    overtime_hours = hours - 40
    #Calculate Overtime Pay
    overtime_pay = overtime_hours * rate * 1.5
    #Calculate salary for regular hours
    regular_pay = 40 * rate
    #Calculate Gross Pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours * rate
    gross_pay = hours * rate

#Display Results
print(f"Employee Name: {name}")
print(f"Hours Worked: {hours}")
print(f"Pay Rate: ${rate:.2f}")
print("----------------------------------")
print(f"Employee Name: {name:<20}\n")
print(f"{'HoursJohn  Worked':<15}{'Pay Rate':<15}{'Overtime Hours':<20}{'Overtime Pay':<20}{'Regular Pay':<20}{'Gross Pay':<20}")
print("_" * 100)
print(f"{hours:<15}{rate:<15.2f}{overtime_hours:<20}{overtime_pay:<20.2f}{regular_pay:<20.2f}{gross_pay:<20.2f}")