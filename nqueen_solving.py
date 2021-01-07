from utils_functions import *
import random

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
def solve_n_queen_big(board_size, empty_board):
    for num_config in range(board_size):
        # print("config -> " + str(num_config))
        board = [row[:] for row in empty_board]
        listQ = set_queens_on_board(board_size, board)
        # print_board(board_size, board)
        # print(listQ)
        max_step = 1000
        solved = min_conflicts(listQ, board_size, max_step)
        # print(listQ)
        if(solved):
            for x in range(board_size):
                board[listQ[x]][x] = 1
            return board, solved
    return board, solved

def set_queens_on_board(board_size, board):
    listQ = [0] * board_size
    y = 2 # random.randint(0, board_size - 1)
    inc = 3 - (board_size % 2)
    for x in range(board_size):
        # board[y][x] = 1 #Queen.value, en vrai pas necessaire de travailler avec le board, listQ suffit
        listQ[x] = y
        y = (y + inc) % board_size
    return listQ

def min_conflicts(listQ, board_size, max_step):
    for step in range(max_step):
        # print("--------------------------------------- step = " + str(step))
        # print("listQ = ")
        # print(listQ)
        most_nb_c, most_c_listQ = most_conflicts_listQ(listQ, board_size)
        if(len(most_c_listQ) == 0):
            return True
        # print("m_c_l = ")
        # print(most_c_listQ)
        chosen_col = random.choice(most_c_listQ)     # on choisi au hasard la colonne d'une reine qui a le plus de conflits (si yen a plusieur)
        qy = listQ[chosen_col]                  # qy = la ligne de la reine choisie
        min_c_rows = [qy]                       # on considère par défaut que la case ayant le moins de conflit est celle de la reine choisie
        # print("chosen_col = " + str(chosen_col))
        # print("min_c_rows before = " + str(min_c_rows))
        for row in range(board_size):
            tmp_listQ = listQ[:]
            tmp_listQ[chosen_col] = row
            if(row != qy):
                case_nb_conflits = get_nb_conflits(tmp_listQ, chosen_col, board_size)
                if(most_nb_c == case_nb_conflits):
                    min_c_rows.append(row)
                elif(most_nb_c > case_nb_conflits):
                    min_c_rows = [row]
                    most_nb_c = case_nb_conflits
        # print("min_c_rows after = " + str(min_c_rows))
        listQ[chosen_col] =  random.choice(min_c_rows)
        # print(listQ)
        # print("--------------------------------------- End step = " + str(step))
    return False


def most_conflicts_listQ(listQ, board_size):
    most_conflicts = 0
    most_conflicts_listQ = []
    for x in range(board_size): # on détermine la liste des reines qui ont le + de conflits
        q_conflicts = get_nb_conflits(listQ, x, board_size)
        if(most_conflicts == q_conflicts and q_conflicts > 0):
            most_conflicts_listQ.append(x)
        elif(most_conflicts < q_conflicts):
            most_conflicts_listQ = [x]
            most_conflicts = q_conflicts
    return most_conflicts, most_conflicts_listQ

def get_nb_conflits(listQ, refQ_x, board_size):
    nb_conflits = 0
    left_conflit = False
    right_conflit = False
    left_top_sublist = []
    left_bot_sublist = []
    right_top_sublist = []
    right_bot_sublist = []

    for i in range(refQ_x): # queens sublist on the left side of the reference queen
        if(listQ[i] == listQ[refQ_x]):
            if not left_conflit:
                nb_conflits += 1
                left_conflit = True
        elif(listQ[i] < listQ[refQ_x]):
            left_top_sublist.append(i)
        else:
            left_bot_sublist.append(i)

    for j in range(refQ_x + 1, len(listQ)): # queens sublist on the right side of the reference queen
        if(listQ[j] == listQ[refQ_x]):
            if not right_conflit:
                nb_conflits += 1
                right_conflit = True
        elif(listQ[j] < listQ[refQ_x]):
            right_top_sublist.append(j)
        else:
            right_bot_sublist.append(j)

    nb_conflits += (subBoard_slash(right_top_sublist, listQ, refQ_x)
                    + subBoard_slash(left_bot_sublist, listQ, refQ_x)
                    + subBoard_backslash(left_top_sublist, listQ, refQ_x, board_size)
                    + subBoard_backslash(right_bot_sublist, listQ, refQ_x, board_size))
    # à retirer
    # print(left_top_sublist) 
    # print("left_top = " + str(subBoard_backslash(left_top_sublist, listQ, refQ_x, board_size)))
    # print(left_bot_sublist)
    # print("left_bot = " + str(subBoard_slash(left_bot_sublist, listQ, refQ_x)))
    # print(right_top_sublist)
    # print("right_top = " + str(subBoard_slash(right_top_sublist, listQ, refQ_x)))
    # print(right_bot_sublist)
    # print("right_bot = " + str(subBoard_backslash(right_bot_sublist, listQ, refQ_x, board_size)))

    return nb_conflits

def subBoard_slash(sublistQ_idx, listQ, refQ_x):
    slash_value_ref = listQ[refQ_x] + refQ_x
    for col in sublistQ_idx:
        s_value = listQ[col] + col
        if(slash_value_ref == s_value):
            return 1
    return 0

def subBoard_backslash(sublistQ_idx, listQ, refQ_x, board_size):
    backslash_value_ref = listQ[refQ_x] - refQ_x + (board_size - 1)
    for col in sublistQ_idx:
        bs_value = listQ[col] - col + (board_size - 1)
        if(backslash_value_ref == bs_value):
            return 1
    return 0

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