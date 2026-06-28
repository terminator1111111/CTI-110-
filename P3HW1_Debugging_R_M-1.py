# P3HW1_Debugging_R_M-1.py
# R_M.



# This program takes six numeric grades, determines lowest, highest, sum,
# average and displays the letter grade for the average.
#Enter the six numeric values of each gade as a float
def get_grade(n):
	while True:
		try:
			g = float(input(f'Enter grade for Module {n}: '))
			if 0 <= g <= 100:
				return g
			print('Please enter a grade between 0 and 100.')
		except ValueError:
			print('Please enter a numeric grade.')

grades = [get_grade(i) for i in range(1, 7)]

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)
#Padd the printed results using "<,>" staements
print("-----Results---------------")
print(f'{"Lowest grade:":<16}{low:<8.1f}')
print(f'{"Highest grade:":<16}{high:<8.1f}')
print(f'{"Sum of grades:":<16}{total:<8.1f}')
print(f'{"Average grade:":<16}{avg:<.2f}')

if avg >= 90:
	letter = 'A'
elif avg >= 80:
	letter = 'B'
elif avg >= 70:
	letter = 'C'
elif avg >= 60:
	letter = 'D'
else:
	letter = 'F'
print("---------------------------")
print(f'Your grade is: {letter}')





