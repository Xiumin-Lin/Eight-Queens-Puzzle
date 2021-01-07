from queen_functions import *

# The 3 utility functions requested in the project


# A chessboard display function
def print_board(board_size, board):
    boardStr = ""
    for row in board:
        for col in row:
            boardStr += " " + str(col)
        boardStr += "\n"
    print(boardStr, end='')


# A function indicating if no queen can attack each other
def can_t_attack(board_size, board):
    for y in range(board_size):  # y = row
        for x in range(board_size):  # x = col
            if board[y][x] == 1:
                queen = Queen(y, x, board_size, board)
                if queen.can_attack():
                    return False
    return True


# A function indicating whether the solution has been found and the number of queen.
def is_soluce(board_size, board):
    nb_queens = 0
    for row in board:
        for col in row:
            if col == 1:
                nb_queens += 1

    is_a_soluce = (True if (can_t_attack(board_size, board) and nb_queens == board_size) else False)
    return is_a_soluce, nb_queens
