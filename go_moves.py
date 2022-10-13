# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nicholas Griffin, Zane Akers, David Guess, Sraavya Danala
# Section:      221
# Assignment:   Lab 7
# Date:         12 October 2022
#

Board = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ]

for row in Board:
    print()
    for column in row:
        print(".", end=" ")

player_stop = input("You done yet?")

if player_stop != "yes" or "Yes":
    Player1row = (input("First move, input 0 for top row, 9 for bottom row"))
    Player1column = (input("First move, input 0 for leftmost column, 9 for rightmost"))
    for row in Board:
        print()
        for column in row:
            if Player1row[Player1column] == row[column]:
                print(chr(9679), "HELLLO")
            else:
                print(".", end=" ")

    player_stop = input("You done yet?")

