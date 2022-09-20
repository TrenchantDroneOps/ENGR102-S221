# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:       Nicholas Griffin, Sravvya Danala, David Guess, Zane Akers
# Section:      221
# Assignment:   Lab 4.15
# Date:         18 September 2022

#this is a program

############ Part A ############
a = input('Enter True or False for a: ')
b = input('Enter True or False for b: ')
c = input('Enter True or False for c: ')

if a == 'True' or a == 'T' or a == 't':
    a = True
elif a == 'False' or a == 'F' or a == 'f':
    a = False
else:
    print('Invalid input for a')

if b == 'True' or b == 'T' or b == 't':
    b = True
elif b == 'False' or b == 'F' or b == 'f':
    b = False
else:
    print('Invalid input for b')

if c == 'True' or c == 'T' or c == 't':
    c = True
elif c == 'False' or c == 'F' or c == 'f':
    c = False
else:
    print('Invalid input for c')

############ Part B ############
print('a and b and c:', bool(a and b and c))
print('a or b or c:', bool(a or b or c))

############ Part C ############
print('XOR:', bool((not(a) and b) or (not(b) and a)))
print('Odd number:', bool((a and b and c) or (not(a) and not(b) and c) or (not(a) and b and not(c)) or (a and not(b) and not(c))))

############ Part D ############
print('Complex 1:', bool((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)))
print('Complex 2:', bool((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b 
and c) or (a and ((b and not c) or (not b)))) ))
print('Simple 1:', bool(not(b) or (not(a) and not(c))))
print('Simple 2:', bool(a or (not(b) and c)))
 