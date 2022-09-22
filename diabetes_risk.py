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

sex = input("Enter your sex (M/F):\n")
age = float(input("Enter your age (years):\n"))
BMI = float(input("Enter your BMI:\n"))
medHypertension = input("Are you on medication for hypertension (Y/N)?\n")
steroids = input("Are you on steroids (Y/N)?\n")
smoke = input("Do you smoke cigarettes (Y/N)?\n")
#if smoke == "Y":
usedToSmoke = input("Did you used to smoke (Y/N)?\n")
familyHistory = input("Do you have a family history of diabetes (Y/N)?\n")

#defining all input number values to 0
sexValue = 0
BMIValue = 0
medHypertensionValue = 0
steroidsValue = 0
smokeValue = 0
familyHistoryValue = 0


#converting sex to number
if sex == "F":
    sexValue = 0.879
else:
    sexValue = 0
    
#converting BMI range to number  
if BMI < 25:
    BMIValue = 0
    
elif 25 <= BMI <= 27.49:
    BMIValue = 0.699
    
elif 27.5 <= BMI <= 29.99:
    BMIValue = 1.97
    
elif BMI >=  30:
    BMIValue = 2.518
    
#converting if on medication for hypertension to number
if medHypertension == "Y":
    medHypertensionValue = 1.222
    
else:
    medHypertensionValue = 0
    
#converting if on steroids to number
if steroids == "Y":
    steroidsValue = 2.191
    
else:
    steroidsValue = 0
    
#converting if smoker or used to smoke to number
if smoke == "N" :
    smokeValue = 0
    if usedToSmoke == "Y":
        smokeValue = -0.218
    elif usedToSmoke == "N":
        smokeValue = 0
elif smoke == "Y":
    smokeValue = 0.855
    
#converting if have family history of diabetes to number
if familyHistory == "N":
    familyHistoryValue = 0
elif familyHistory =="Y":
    whoFamily = input("Both parent and sibling (Y/N)?\n")
    if whoFamily == "N":
        familyHistoryValue = 0.728
    elif whoFamily == "Y":
        familyHistoryValue = 0.753
        

n = 6.322 + sexValue - (0.063*age) - BMIValue - medHypertensionValue - steroidsValue - smokeValue - familyHistoryValue


riskDiabetes = 100/(1 + exp(n))


#print("Your risk of developing type-2 diabetes is", riskDiabetes)

print(f"Your risk of developing type-2 diabetes is {riskDiabetes:3.1f} %")
