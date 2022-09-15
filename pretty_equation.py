# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nicholas Griffin, Zane Akers, David Guess, Sraavya Danala
# Section:      221
# Assignment:   Lab 3.16
# Date:         13 September 2022
#

from math import *
from re import T
from sympy import *
from sympy.plotting import (plot,plot_parametric)


#find the coefficients
A = str(input("Please enter the coefficient A: "))
B = str(input("Please enter the coefficient B: "))
C = str(input("Please enter the coefficient C: "))

x = symbols('x')

if A == 0:
    print("The quadratic equation is ", B + "x", "+", C, "=0")
if B == 0:
    print("The quadratic equation is ", A + "x^2", "+", C, "=0")
if C == 0:
    print("The quadratic equation is ", A + "x^2", "+", B + "x", "=0")



print("The quadratic equation is ", A+"x^2", "+", B+"x", "+", C, "=0")


