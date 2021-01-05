from utils_functions import *

# Premier algorithme : la naiveté
def solve_n_queen_small(board_size, empty_board):
    banList= {}
    banList["row"] = [False for i in range(board_size)]
    banList["slash"] = [False for i in range(board_size * 2 - 1)]
    banList["backslash"] = [False for i in range(board_size * 2 - 1)]
    board, solved = backtrack(0, board_size, empty_board, banList)
    if(solved):
        return board, True
    return board, False

# Test s'il est possible de placé une reine sur la colonne numéro x
# _ Appele récursivement la fonction backtrack() si une reine peut etre placé dans le tableau
#   mais que tous les reines n'ont pas été placées
# _ Les cases d'une même diagonale que ce soit / ou \ ont la même valeur
# _ Lorsqu'une reine peut être posé, la ligne (y) et ses diagonales (/ et \) sur laquelle elle est placée 
#   seront bannies et ne seront plus traitées durant la bourcle for tant que la reine placée sera présent
# _ Return le board et True si le tout les reinse ont été placées
# _ Return le board et False si le tout les reinse ont été placées et/ou aucune reine a pu etre placé sur la colonne
def backtrack(x, board_size, previous_board, banList):
    if(x == board_size):
        return previous_board, True
    if(x > board_size or x < 0):
        return previous_board, False
    board = previous_board

    for y in range(board_size):
        bslash_value = (board_size - 1) - x + y
        slash_value = x + y
        can_be_placed = not banList["row"][y] and not banList["slash"][slash_value] and not banList["backslash"][bslash_value]
        if can_be_placed:
            board = [row[:] for row in previous_board] # on crée une copie du board d'avant

            board[y][x] = Queen.value
            banList["row"][y] = True
            banList["slash"][slash_value] = True
            banList["backslash"][bslash_value] = True

            new_board, solved = backtrack(x + 1, board_size, board, banList)
            if(solved):
                return new_board, solved
            
            board[y][x] = "0"
            banList["row"][y] = False
            banList["slash"][slash_value] = False
            banList["backslash"][bslash_value] = False
    return board, False

################################################
# Deuxième algorithme : le meilleur
def solve_n_queen_big(board_size, board):
    solved = False
    return board, solved

################################################
# Troisième algorithme : toutes les combinaisons
def solve_n_queen_all_soluce(board_size, empty_board):
    boards = []
    banList= {}
    banList["row"] = [False for i in range(board_size)]
    banList["slash"] = [False for i in range(board_size * 2 - 1)]
    banList["backslash"] = [False for i in range(board_size * 2 - 1)]

    backtrack_all(0, board_size, empty_board, banList, boards)
    return boards

# Fonctionne de la même manière que la fonction backtrack(), mais reçoit en plus une liste (boards) 
# qui stocke tous les solutions possibles pour un N donné du N Queen Puzzle 
# _ Ne retourne rien, la liste de toute les solutions correspond à la liste passé en paramètre
# _ S'il n'existe aucune solution, la liste sera vide
def backtrack_all(x, board_size, previous_board, banList, boards):
    if(x == board_size):
        boards.append(previous_board)
        return True
    if(x > board_size or x < 0):
        return False

    board = previous_board

    for y in range(board_size):
        bslash_value = (board_size - 1) - x + y
        slash_value = x + y
        can_be_placed = not banList["row"][y] and not banList["slash"][slash_value] and not banList["backslash"][bslash_value]
        if can_be_placed:
            board = [row[:] for row in previous_board] # on crée une copie du board d'avant

            board[y][x] = Queen.value
            banList["row"][y] = True
            banList["slash"][slash_value] = True
            banList["backslash"][bslash_value] = True

            solved = backtrack_all(x + 1, board_size, board, banList, boards)
            if(not solved):
                board[y][x] = "0"

            banList["row"][y] = False
            banList["slash"][slash_value] = False
            banList["backslash"][bslash_value] = False
    return False