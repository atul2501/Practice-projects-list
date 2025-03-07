#P2.py
#Richter Scale: Input some numbers, do some simple arithmetic, output results.(Python3)
import math

magnitude=float(input("Richter Scale Magnitude value: "))

energy = 10**(1.5 * magnitude +4.8)
energy=round(energy,2)

tnt= energy/(4.184*10**9)
tnt=round(tnt,2)

print(f"Richter Scale value '{magnitude}'")
print(f"equivalent amount of energy in joules :'{energy}'")
print(f"equivalent amount of energy in TNT : '{tnt}'")



#o/p
'''
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P2.py
Richter Scale Magnitude value: 5
Richter Scale value '5.0'
equivalent amount of energy in joules :'1995262314968.88'
equivalent amount of energy in TNT : '476.88'
'''
