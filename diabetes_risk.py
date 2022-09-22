# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nicholas Griffin, Zane Akers, David Guess, Sraavya Danala
# Section:      221
# Assignment:   Lab 5.3
# Date:         22 September 2022
#

from math import *

#Ask for user input for sex, age, BMI, medHypertension, steroids, smoke and familyHistory
#If/elif/else statements to convert the user input values to numbers to calculate n
#Use the user input and plug it into the n equation to find the value of n
#Plug in n to find the user’s risk of developing type - 2 diabetes

#converting sex to number
sex = input("Enter your sex (M/F):\n")
if sex == "M" or sex == 'm':
    sexValue = 0
elif sex == "F" or sex == 'f':
    sexValue = 0.879

age = float(input("Enter your age (years):\n"))   #ask for user age

#converting BMI range to number 
BMI = float(input("Enter your BMI:\n"))
if BMI < 25:
    BMIValue = 0
elif BMI < 27.5:
    BMIValue = 0.699 
elif BMI < 30:
    BMIValue = 1.97
elif BMI >= 30:
    BMIValue = 2.518

#converting if on medication for hypertension to number
medHypertension = input("Are you on medication for hypertension (Y/N)?\n")
if medHypertension == 'Y' or medHypertension == 'y':
    medHypertensionValue = 1.222
elif medHypertension == 'N' or medHypertension == 'n':
    medHypertensionValue = 0

#converting if on steroids to number
steroids = input("Are you on steroids (Y/N)?\n")
if steroids == 'Y'or steroids == 'y':
    steroidsValue = 2.191
elif steroids == 'N' or steroids == 'n':
    steroidsValue = 0

#converting if smoker or used to smoke to number
smoke = input("Do you smoke cigarettes (Y/N)?\n")
if smoke == "N" or smoke == 'n':
    usedToSmoke = input("Did you used to smoke (Y/N)?\n")
    if usedToSmoke == "Y" or usedToSmoke == 'y':
        smokeValue = -0.218
    elif usedToSmoke == "N" or usedToSmoke == 'n':
        smokeValue = 0
elif smoke == "Y" or smoke == 'y':
    smokeValue = 0.855
    
#converting if have family history of diabetes to number
familyHistory = input("Do you have a family history of diabetes (Y/N)?\n")
if familyHistory == "N" or familyHistory == 'n':
    familyHistoryValue = 0
elif familyHistory == "Y" or familyHistory == 'y':
    whoFamily = input("Both parent and sibling (Y/N)?\n")
    if whoFamily == "N" or whoFamily == 'n':
        familyHistoryValue = 0.728
    elif whoFamily == "Y" or whoFamily == 'y':
        familyHistoryValue = 0.753
        
#calculate n from previous values
n = 6.322 + sexValue - (0.063*age) - BMIValue - medHypertensionValue - steroidsValue - smokeValue - familyHistoryValue

riskDiabetes = 100/(1 + e**n) 

#print("Your risk of developing type-2 diabetes is", riskDiabetes)
print(f"Your risk of developing type-2 diabetes is {riskDiabetes:.1f} %")
