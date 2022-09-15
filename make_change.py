# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nicholas Griffin, Zane Akers, David Guess, Sraavya Danala
# Section:      221
# Assignment:   Lab 4.13
# Date:         15 September 2022
#



from math import *

pay = float(input('How much did you pay?'))
cost = float(input('How much did it cost?'))
change = int(round((pay - cost)*100))
if change >= 100:
    change = change % 100
print (f'You received ${change/100:.2f} in change. That is...')
if change >= 25:
    num_q = change // 25                                        #num_q is number of quarters
    if num_q == 1:
        print (num_q, 'quarter')
    else:
        print (num_q, 'quarters')
    change = change % 25

if change >= 10:
    num_d = change // 10                                        #num_d is number of dimes
    if num_d == 1:
        print (num_d, 'dime')
    else:
        print (num_d, 'dimes')
    change = change % 10

if change >= 5:
    num_n = change // 5                                         #num_n is number of nickels
    if num_n == 1:
        print (num_n, 'nickel')
    else:
        print (num_n, 'nickels')
    change = change % 5

if change >= 1:
    num_p = change // 1                                         #num_p is number of pennies
    if num_p == 1:
        print (num_p, 'penny')
    else:
        print (num_p, 'pennies')
