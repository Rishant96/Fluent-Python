"""
 Sometimes we need to initialize a list with a certain number of
 nested lists, for example, to distribute to distribute students
 in a list of teams, or to represent squares on a game board.

 The best way of doing so is with a list comprehension.
"""

# A list with 3 lists of length 3 can represent a Tic-tac-toe board
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board, '\n')

# Wrong shortcut -
weird_board = [['_'] * 3] * 3  # 1
print(weird_board)
weird_board[1][2] = 'O'  # 2
print(weird_board)

"""
 1 - The outer list is made of three references to the same inner list.
     While it is unchanged, all seems right.

 2 - Placing a mark in row 1, column 2 reveals that all rows are aliases
     referring to the same object
"""

# Explanation:

# Wrong board
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)  # 1
# 1 - The same 'row' is appended 3 times to board.

# Correct board
board = []
for i in range(3):
    row = ['_'] * 3  # 1
    board.append(row)
print(board)
board[2][0] = 'X'
print(board)  # 2

"""
 1 - Each iteration builds a new 'row' and appends it to 'board'.
 2 - Only row 2 is changed, as expected.
"""
