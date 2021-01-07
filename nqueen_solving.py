from utils_functions import (
    is_soluce, print_board, can_t_attack, Queen
)
import random


# First algorithm: naivety
def solve_n_queen_small(board_size, empty_board):
    banList = {}
    banList["row"] = [False for i in range(board_size)]
    banList["slash"] = [False for i in range(board_size * 2 - 1)]
    banList["backslash"] = [False for i in range(board_size * 2 - 1)]
    board, solved = backtrack(0, board_size, empty_board, banList)
    if(solved):
        return board, True
    return board, False


# Test if it is possible to place a queen on the column number x
# _ Recursively calls the backtrack() function if a queen can be placed in the array.
# but not all the queens have been placed
# The squares of the same diagonal either / or \ have the same value.
# _ When a queen can be placed, the line (y) and its diagonals (/ and \)
#   on which it is placed will be banned and will not be processed further
#   during the "for" until the placed queen is removed.
# _ Return board and True if all queens have been placed.
# _ Return board and False if not all queens have been placed.
def backtrack(x, board_size, previous_board, banList):
    if(x == board_size):
        return previous_board, True
    if(x > board_size or x < 0):
        return previous_board, False
    board = previous_board

    for y in range(board_size):
        bslash_value = (board_size - 1) - x + y
        slash_value = x + y
        can_be_placed = (not banList["row"][y]
                         and not banList["slash"][slash_value]
                         and not banList["backslash"][bslash_value])
        if can_be_placed:
            # we create a copy of the previous board
            board = [row[:] for row in previous_board]

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
# Second algorithm: the best
def solve_n_queen_big(board_size, empty_board):
    for num_config in range(board_size):
        board = [row[:] for row in empty_board]
        listQ = set_queens_on_board(board_size)
        max_step = 1000
        solved = min_conflicts(listQ, board_size, max_step)
        if(solved):
            for x in range(board_size):
                board[listQ[x]][x] = 1
            return board, solved
    return board, solved


def set_queens_on_board(board_size):
    listQ = [0] * board_size
    y = random.randint(0, board_size - 1)
    inc = 3 - (board_size % 2)
    for x in range(board_size):
        listQ[x] = y
        y = (y + inc) % board_size
    return listQ


def min_conflicts(listQ, board_size, max_step):
    for step in range(max_step):
        most_nb_c, most_c_listQ = most_conflicts_listQ(listQ, board_size)
        if(len(most_c_listQ) == 0):
            return True
        # choose a random queen index among the most_c_listQ
        chosen_col = random.choice(most_c_listQ)
        # qy = the row of the chosen queen
        qy = listQ[chosen_col]
        # By default, the square of the chosen queen is the least conflict one
        min_c_rows = [qy]
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
        listQ[chosen_col] = random.choice(min_c_rows)
    return False


def most_conflicts_listQ(listQ, board_size):
    most_conflicts = 0
    most_conflicts_listQ = []
    # we determine the list of queens that have the most conflicts
    for x in range(board_size):
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

    # queens sublist on the left side of the reference queen
    for i in range(refQ_x):
        if(listQ[i] == listQ[refQ_x]):
            if not left_conflit:
                nb_conflits += 1
                left_conflit = True
        elif(listQ[i] < listQ[refQ_x]):
            left_top_sublist.append(i)
        else:
            left_bot_sublist.append(i)

    # queens sublist on the right side of the reference queen
    for j in range(refQ_x + 1, len(listQ)):
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
# Third algorithm: all combinations
def solve_n_queen_all_soluce(board_size, empty_board):
    boards = []
    banList = {}
    banList["row"] = [False for i in range(board_size)]
    banList["slash"] = [False for i in range(board_size * 2 - 1)]
    banList["backslash"] = [False for i in range(board_size * 2 - 1)]

    backtrack_all(0, board_size, empty_board, banList, boards)
    return boards


# Works like the backtrack function, but receives a list (boards) in addition.
# which stores all possible solutions for a given N of the N Queen Puzzle
# Return nothing, the list of all solutions corresponds to the list passed in arg
# If there is no solution, the list will be empty.
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
        can_be_placed = (not banList["row"][y]
                         and not banList["slash"][slash_value]
                         and not banList["backslash"][bslash_value])
        if can_be_placed:
            # we create a copy of the previous board
            board = [row[:] for row in previous_board]
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
