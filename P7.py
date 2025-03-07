#P7.py
#Population: Input some numbers, do some simple arithmetic to estimate today's U.S. population, output results.

try:
	population=307357870

	every_sec_birth=7
	every_sec_death=13
	every_sec_new_immigrant=35

	year=365
	hrs=24
	min=60
	sec=60

	total_secs_in_year=year*hrs*min*sec 

	year_population=int(input("How many year :"))
	if year_population>=0:
		sec_year=year_population*total_secs_in_year

		birth=sec_year/every_sec_birth
		death=sec_year/every_sec_death
		immigrant=sec_year/every_sec_new_immigrant

		New_population=population+birth-death+immigrant

		print(f"New population in {year_population} whill chnage to {New_population}")
	else:
		print("number should not be negative")

except ValueError:
	print(f"inter a valid number and number only")

#o/p
'''
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :-1
number should not be negative
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :s
inter a valid number and number only
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :-1
number should not be negative
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :sh
inter a valid number and number only
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :12
New population in 12 whill chnage to 343121773.2967033
(base) atul2501@Atuls-MacBook-Air Python Practice project list % 
'''
