# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:       Nicholas Griffin, Sravvya Danala, David Guess, Zane Akers
# Section:      221
# Assignment:   Lab 4.14.1
# Date:         17 September 2022

#this is a program
from math import *



A = int(input('Please enter the coefficient A: '))
B = int(input('Please enter the coefficient B: '))
C = int(input('Please enter the coefficient C: '))

if A==0:
    A = 0
elif A == 1:
    A = 'x^2'
elif A == -1:
    A = '- x^2'
elif A < 0:
    A = '-', abs(A)
else:
    A = f'{A}x^2'

if B==0:
    B=0
elif B == 1:
    if A==0:
        B = 'x'
    else:
        B = '+ x'  
elif B == -1:
    B = '- x'
elif B < 0:
    B = f'- {abs(B)}x'
else:
    if A==0:
        B = f'{B}x'
    else:
        B = f'+ {B}x'
if C == 0:
    C=0
elif C < 0:
    C = f'- {abs(C)}'
else:
    if A==B==0:
        C = f'{C}'
    else:
        C = f'+ {C}'

    
if A==B==C==0:
    print ('The quadratic equation is 0 = 0')
elif A==B==0:
    print ('The quadratic equation is',C,'= 0')
elif A==C==0:
    print ('The quadratic equation is',B,'= 0')
elif B==C==0:
    print ('The quadratic equation is',A,'= 0')
elif A==0:
    print ('The quadratic equation is',B,C,'= 0')
elif B==0:
    print ('The quadratic equation is',A,C,'= 0')
elif C==0:
    print ('The quadratic equation is',A,B,'= 0')
else:
    print ('The quadratic equation is',A,B,C,'= 0')
