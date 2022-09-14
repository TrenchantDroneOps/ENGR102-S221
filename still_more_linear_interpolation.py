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
#hi
 
#x0, y0, z0 are starting positions
#x1, y1, z1 are ending positions
#t0 is starttime, t1 is end time
 
 
t0 = float(input("Enter time 1: "))
x0 = float(input("Enter the x position of the object at time 1: "))
y0 = float(input("Enter the y position of the object at time 1: "))
z0 = float(input("Enter the z position of the object at time 1: "))
 
t1 = float(input("Enter time 2: "))
x1 = float(input("Enter the x position of the object at time 2: "))
y1 = float(input("Enter the y position of the object at time 2: "))
z1 = float(input("Enter the z position of the object at time 2: "))
print()
 
 
delta_t = t1-t0
delta_x = x1-x0
delta_y = y1-y0
delta_z = z1-z0
t_interval = delta_t / 4
 
t=t0
new_x = delta_x/delta_t * (t-t0) + x0
new_y = delta_y/delta_t * (t-t0) + y0
new_z = delta_z/delta_t * (t-t0) + z0
print(f'At time {t:.2f} seconds the object is at ({new_x:.3f}, {new_y:.3f}, {new_z:.3f})')
 
t=t+t_interval
new_x = delta_x/delta_t * (t-t0) + x0
new_y = delta_y/delta_t * (t-t0) + y0
new_z = delta_z/delta_t * (t-t0) + z0
print(f'At time {t:.2f} seconds the object is at ({new_x:.3f}, {new_y:.3f}, {new_z:.3f})')
 
t=t+t_interval
new_x = delta_x/delta_t * (t-t0) + x0
new_y = delta_y/delta_t * (t-t0) + y0
new_z = delta_z/delta_t * (t-t0) + z0
print(f'At time {t:.2f} seconds the object is at ({new_x:.3f}, {new_y:.3f}, {new_z:.3f})')
 
t=t+t_interval
new_x = delta_x/delta_t * (t-t0) + x0
new_y = delta_y/delta_t * (t-t0) + y0
new_z = delta_z/delta_t * (t-t0) + z0
print(f'At time {t:.2f} seconds the object is at ({new_x:.3f}, {new_y:.3f}, {new_z:.3f})')
 
t=t+t_interval
new_x = delta_x/delta_t * (t-t0) + x0
new_y = delta_y/delta_t * (t-t0) + y0
new_z = delta_z/delta_t * (t-t0) + z0
print(f'At time {t:.2f} seconds the object is at ({new_x:.3f}, {new_y:.3f}, {new_z:.3f})')
 
 

