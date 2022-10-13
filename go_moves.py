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

Board = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ]
#The board

Player1row = (input("First move, input 0 for top row, 9 for bottom row"))
Player1column = (input("First move, input 0 for leftmost column, 9 for rightmost"))
for row in Board:
    print()
    for column in row:
            print(".", end=" ")
#THe board is displayed for all players to see
counter = 0
#to see who's turn it is

player_stop = input("You done yet?")
if player_stop != "yes" or "Yes":
    counter += 1
    Playerrow = int(input("The",counter,"th turn, next move, input row"))
    Playercolumn = int(input("next move, input column"))
    #Reprint the board, except with the indexed row and column replaced with a solid black circle
    for row in Board:
        print()
        for column in row:
            if counter // 2 == 0:
                if Playerrow[Playercolumn] == column :
                    print(chr(9679))
                else:
                    print(".", end=" ")
            else:
                if Playerrow[Playercolumn] == column:
                    print(chr(9675)) #clear circle
                else:
                    print(".", end=" ")

    player_stop = input("You done yet?")

