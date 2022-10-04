# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nicholas Griffin, Sravvya Danala, Zane Akers, David Guess
# Section:      221
# Assignment:   Lab 6.11
# Date:         4 October 2022

# comment
from math import *
from fractions import Fraction

side = float(input('Enter the side length in meters: '))
layer = int(input('Enter the number of layers: '))

area = 0
for i in range(layer):
    n = i + 1
    area += 3*n*side**2 + (sqrt(3)/4)*(n*side)**2 - (sqrt(3)/4)*(i*side)**2

print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')