from queen_functions import *

# Les 3 fonctions utilitaires demandé dans le projet

# Une fonction d’affichage du plateau
def print_board(board_size, board): #Steven
    boardStr = ""
    for row in board:
        for col in row:
            boardStr += " " + str(col)
        boardStr += "\n"
    print(boardStr, end='')

# Une fonction indiquant si aucune reine ne peut se frapper
def can_t_attack(board_size, board):
    for y in range(board_size):     # y = row
        for x in range(board_size): # x = col
            if board[y][x] == 1:
                queen = Queen(y, x, board_size, board)
                if queen.can_attack():
                    return False
    return True


# Une fonction indiquant si la solution a été trouvée ainsi que le nombre de reine.
def is_soluce(board_size, board):
    nb_queens = 0
    for row in board:
        for col in row:
            if col == 1:
                nb_queens += 1

    is_a_soluce = True if (can_t_attack(board_size, board) and nb_queens == board_size) else False
    return is_a_soluce, nb_queens
