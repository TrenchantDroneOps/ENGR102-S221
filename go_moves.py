# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nicholas Griffin, Zane Akers, David Guess, Sraavya Danala
# Section:      221
# Assignment:   Lab 7
# Date:         12 October 2022
#

Board = [['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.']]
#The board

for i in range(len(Board)):
    for j in range(len(Board[i])):
        print(Board[i][j], end='')
    print()

keepGoing = input('Ready to start?')
while keepGoing != 'no' and keepGoing != 'No':
    row = int(input('Black, please enter a row 1-9: '))
    col = int(input('Black, please enter a column 1-9: '))
    while Board[9-row][col-1] != '.':
        print('That space has already been played on. Try again.')
        row = int(input('Black, please enter a row 1-9: '))
        col = int(input('Black, please enter a column 1-9: '))
    Board [9-row][col-1] = '*'
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            print(Board[i][j], end='')
        print()
    row = int(input('White, please enter a row 1-9: '))
    col = int(input('White, please enter a column 1-9: '))
    while Board[9-row][col-1] != '.':
        print('That space has already been played on. Try again.')
        row = int(input('White, please enter a row 1-9: '))
        col = int(input('White, please enter a column 1-9: '))
    Board [9-row][col-1] = '@'
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            print(Board[i][j], end='')
        print()
    keepGoing = input('Keep going?')
