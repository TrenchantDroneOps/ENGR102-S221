
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nicholas Griffin, Zane Akers, David Guess, Sraavya Danala
# Section:      221
# Assignment:   Lab 6
# Date:         4 October 2022
#

from math import *


side = float(input("Enter the side length in meters: "))

layer = int(input("Enter the number of layers: "))


num_squares = (layer/2*(2 + (layer-1)))*3

area = num_squares*(side**2)

top = 0.25*sqrt(3)*(side*layer)**2


print(f'You need {area+top:.2f} m^2 of gold foil to cover the pyramid')

#cool it works