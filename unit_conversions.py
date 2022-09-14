# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:       Zane Akers, Nicholas Griffin, Sraavya Danala, David Guess
# Section:      221
# Assignment:   Lab 3.15
# Date:         8 September 2022


#a) Pounds (force) to Newtons
#b) Meters to feet
#c) Atmospheres to kilopascals (kPa)
#d) Watts to BTU per hour
#e) Liters per second to US gallons per minute
#f) Degrees Celsius to degrees Fahrenheit



x = float(input("Please enter the quantity to be converted:"))

#####------(a)--------#########
print(f'{x:.2f} pounds force is equivalent to {x/0.22480894387:.2f} Newtons')

#####------(b)--------#########
print(f'{x:.2f} meters is equivalent to {x*3.2808399:.2f} feet')

#####------(c)--------#########
print(f'{x:.2f} atmospheres is equivalent to {x*101.325:.2f} kilopascals')

#####------(d)--------#########
print(f'{x:.2f} watts is equivalent to {x*3.412143591:.2f} BTU per hour')

#####------(e)--------#########
print(f'{x:.2f} liters per second is equivalent to {x*15.85032879:.2f} US gallons per minute')

#####------(f)--------#########
print(f'{x:.2f} degrees Celsius is equivalent to {x*(9/5)+32:.2f} degrees Fahrenheit')









