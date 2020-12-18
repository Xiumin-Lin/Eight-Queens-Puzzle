from utils_functions import *

# Premier algorithme : la naiveté
def solve_n_queen_small(board_size, empty_board):
    for firstY in range(board_size):
        
        board = [[0 for x in range(board_size)] for y in range(board_size)] # on reset le board à 0
        board[firstY][0] = Queen.value
        nbQueenTotal = 1

        board, solved = backtrack(0, board_size, board, nbQueenTotal)
        if(solved):
            return board, True

    return board, False

# Test s'il est possible de placé une reine sur la colonne previous_x + 1
# _ Appele récursivement la fonction backtrack() si une reine peut etre placé
#   mais que tous les reines n'ont pas été placées
# _ Return le board et True si le tout les reinse ont été placées
# _ Return le board et False si le tout les reinse ont été placées et/ou aucune reine a pu etre placé sur la colonne
def backtrack(previous_x, board_size, previous_board, nbQueenTotal):
    current_x = previous_x + 1
    board = previous_board

    if(current_x >= board_size):
        return board, False
    
    for y in range(board_size):
        board = [row[:] for row in previous_board] # on copie du board original
        queen = Queen(y, current_x, board_size, board)

        if(queen.can_be_placed()):
            board[y][current_x] = Queen.value
            nbQueenTotal += 1
            if(nbQueenTotal == board_size):
                return board, True

            new_board, solved = backtrack(current_x, board_size, board, nbQueenTotal)
            if(solved):
                return new_board, solved
            nbQueenTotal -= 1
            board[y][current_x] = "0"
    return board, False

# Deuxième algorithme : le meilleur
def solve_n_queen_big(board_size, board):
    solved = False
    return board, solved


# Troisième algorithme : toutes les combinaisons
def solve_n_queen_all_soluce(board_size, board):
    solved = False
    return board, solved
