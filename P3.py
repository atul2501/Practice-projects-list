#P3.py
#Windchill: Input some numbers, do some simple arithmetic, output results.(Python3)


air_temp=float(input(" enter an air temperature measurement(degree F) : "))
air_speed=float(input("enter a wind speed measurement(MPH)            : "))

wct_index= 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16

wct_index=round(wct_index,5)
print(f"the wind chill temperature index : {wct_index}")


#o/p
'''
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P3.py
 enter an air temperature measurement(degree F) : 10
enter a wind speed measurement(MPH)            : 15
the wind chill temperature index : -6.58953
'''
