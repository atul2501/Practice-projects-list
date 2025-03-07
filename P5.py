#P5.py
#Gasoline: Input some numbers, do some simple arithmetic on gas and oil quantities, output results.


gallon=float(input("Enter the number of gasoline : "))
if gallon >=1:
	billsFloat = 4
	liters=gallon*3.78541
	barrel=gallon/19.5
	pound=gallon*20
	ethanol=1.519154*gallon
	bills=billsFloat*gallon

	print(f"original numbers of gallon {gallon}")
	print(f"{gallon} gallon of gasoline '{barrel}' barrels of oil")
	print(f"{gallon} gallon of gasoline '{pound}' pounds of C02")
	print(f"{gallon} gallon of gasoline '{ethanol}'' gallons of ethanol")
	print(f"{gallon} gallon of gasoline '{bills}' Us dollar")
else:
	print(f"gallon is 0 or below zero is not valid")


#o/p
'''
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P5.py
Enter the number of gasoline : 2
original numbers of gallon 2.0
2.0 gallon of gasoline '0.10256410256410256' barrels of oil
2.0 gallon of gasoline '40.0' pounds of C02
2.0 gallon of gasoline '3.038308'' gallons of ethanol
2.0 gallon of gasoline '8.0' Us dollar
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P5.py
Enter the number of gasoline : 0
gallon is 0 or below zero is not valid
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P5.py
Enter the number of gasoline : 0.1
gallon is 0 or below zero is not valid
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P5.py
Enter the number of gasoline : 100000
original numbers of gallon 100000.0
100000.0 gallon of gasoline '5128.205128205128' barrels of oil
100000.0 gallon of gasoline '2000000.0' pounds of C02
100000.0 gallon of gasoline '151915.4'' gallons of ethanol
100000.0 gallon of gasoline '400000.0' Us dollar
(base) atul2501@Atuls-MacBook-Air Python Practice project list % 
'''
