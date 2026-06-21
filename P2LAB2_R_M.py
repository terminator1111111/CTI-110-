# M_R
# June 21, 2024
# P2LAB2_R_M
# Using Dictionaries 

cars = {'Camaro': 18.21, 'Prius':52, 'Model S': 110, 'Silverado': 26}

#Get keys from dict
cars_keys = cars.keys()
print(cars_keys)

print(*cars_keys, sep = ", ")
#Get a car from user
car_name = input("Enter a car: ")

#Get MPG/MPGe for the given car
car_mpg = cars[car_name]
print(f"The {car_name} get {car_mpg} milles per gallon.")

#Get :miles from user
miles_driven = float(input(f"How many miles will you drive the car {car_name}?"))

# Calculate
gallons_needed = miles_driven/car_mpg

#Display results 
print(f"{gallons_needed} gallons(s) of gas are needed to drive the {car_name} {miles_driven} miles")

