#P6.py
#Measurement: Input some numbers, do some simple arithmetic to do silly conversions such as furlongs/fortnight, output results.


try:
	miles=float(input("enter ther miles "))
	hrs=1

	if miles >=1:
		bar=miles/hrs*4561920
		fornight=miles/hrs*2688
		much=(miles/hrs)/767
		light=((miles/hrs)/(670616629))*100

		print(f"Original speed in mph is :{miles}")
		print(f"Converted to barleycorn/day is :{bar}")
		print(f"converted to forlongs/fornight is :{fornight}")
		print(f"Converted to Much number is :{much}")
		print(f"Converted to the  percentage of the speed of light :{light}")
	else:
		print("0 or below zero are not valid")
except:
	print("enter only number")



#o/p
'''
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P6.py
enter ther miles sas
enter only number
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P6.py
enter ther miles 0
0 or below zero are not valid
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P6.py
enter ther miles -12
0 or below zero are not valid
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P6.py
enter ther miles 5
Original speed in mph is :5.0
Converted to barleycorn/day is :22809600.0
converted to forlongs/fornight is :13440.0
Converted to Much number is :0.00651890482398957
Converted to the  percentage of the speed of light :7.455824660142749e-07
(base) atul2501@Atuls-MacBook-Air Python Practice project list % 
'''
