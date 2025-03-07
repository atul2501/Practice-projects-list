#P7.py
#Population: Input some numbers, do some simple arithmetic to estimate today's U.S. population, output results.

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

sec_year=year_population*total_secs_in_year

birth=sec_year/every_sec_birth
death=sec_year/every_sec_death
immigrant=sec_year/every_sec_new_immigrant

New_population=population+birth-death+immigrant

print(f"New population in {year_population} whill chnage to {New_population}")

#o/p
'''
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :1
New population in 1 whill chnage to 310338195.2747253
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :100
New population in 100 whill chnage to 605390397.4725275
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P7.py
How many year :100
New population in 100 whill chnage to 605390397.4725275
'''
