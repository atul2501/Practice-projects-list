#P8.py
#Time Travel: Input some numbers, do some simple arithmetic to calculate travel time between stars, output results.

import math


Alpha_centauri=4.3
Barnards_Star=6
Betelgeuse=309
Andromeda_Galaxy=2000000

Ship_weight=70000
Light_speed=299792458


while True:

	try:


		percentage_speed=int(input("enter a percentage "))

		if percentage_speed>=0 and percentage_speed<100:

			

			if percentage_speed=="q":
				print("thank of testing come back soon")
				break

			#if percentage_speed>=0 and percentage_speed<=100:
			ship_speed=(percentage_speed/100)*Light_speed

			dilation_factor = 1 / math.sqrt(1 - (ship_speed / Light_speed) ** 2)

			new_ship_weight = Ship_weight * dilation_factor


			time_alpha_centauri = Alpha_centauri / dilation_factor
			time_barnards_star = Barnards_Star / dilation_factor
			time_betelgeuse = Betelgeuse / dilation_factor
			time_andromeda_galaxy = Andromeda_Galaxy / dilation_factor

			print(f"\nFor a ship traveling at {percentage_speed}% of the speed of light:")
			print(f"New mass of the ship: {new_ship_weight:.2f} kg")
			print(f"Time to Alpha Centauri: {time_alpha_centauri:.2f} years")
			print(f"Time to Barnard's Star: {time_barnards_star:.2f} years")
			print(f"Time to Betelgeuse: {time_betelgeuse:.2f} years")
			print(f"Time to Andromeda Galaxy: {time_andromeda_galaxy:.2f} years")

		elif percentage_speed==100:
				print("not possible bro 'Imagine you are in ship with speed of light and when you ship expolde now you become speed of light' \n 😂")

		else :
			print("enter a valid number please 0 to 99 only")

	except ValueError:
		print("enter number only")



#output:
'''
(base) atul2501@Atuls-MacBook-Air Python Practice project list % python P8.py
enter a percentage 1

For a ship traveling at 1% of the speed of light:
New mass of the ship: 70003.50 kg
Time to Alpha Centauri: 4.30 years
Time to Barnard's Star: 6.00 years
Time to Betelgeuse: 308.98 years
Time to Andromeda Galaxy: 1999900.00 years
enter a percentage -1
enter a valid number please 0 to 99 only
enter a percentage 100
not possible bro 'Imagine you are in ship with speed of light and when you ship expolde now you become speed of light' 
 😂
enter a percentage s 
enter number only
enter a percentage 25

For a ship traveling at 25% of the speed of light:
New mass of the ship: 72295.69 kg
Time to Alpha Centauri: 4.16 years
Time to Barnard's Star: 5.81 years
Time to Betelgeuse: 299.19 years
Time to Andromeda Galaxy: 1936491.67 years
'''
