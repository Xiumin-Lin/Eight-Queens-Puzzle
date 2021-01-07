class Queen:

    value = 1   # the value that represents the queen in the chessboard

    def __init__(self, y, x, board_size, board):
        self.y = y  # queen's row index
        self.x = x  # queen's column index
        self.board_size = board_size
        self.board = board

    # Checks if the queen can attack another queen
    # Warning, this only checks the
    # right, bottom, bottom left and right diagonal squares of the queen
    # Use this with a loop that runs from left to right and then up and down the board.
    def can_attack(self):
        if (self.can_attack_right()
                or self.can_attack_down()
                or self.can_attack_diag_down_left()
                or self.can_attack_diag_down_right()):
            return True
        return False

    # Checks if the queen can attack (another queen) to her right
    def can_attack_right(self):
        for i in range(self.x + 1, self.board_size):
            if (self.board[self.y][i] == Queen.value):
                return True
        return False

    # Checks if the queen can attack down
    def can_attack_down(self):
        for i in range(self.y + 1, self.board_size):
            if (self.board[i][self.x] == Queen.value):
                return True
        return False

    # Checks if the queen can attack at her bottom left diagonal
    def can_attack_diag_down_left(self):
        i = 1
        while((self.board_size - (self.y + i)) > 0 and (self.x - i) >= 0):
            newY = self.y + i
            newX = self.x - i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False

    # Checks if the queen can attack at her bottom right diagonal
    def can_attack_diag_down_right(self):
        i = 1
        while((self.board_size - (self.y + i)) > 0
              and (self.board_size - (self.x + i)) > 0):
            newY = self.y + i
            newX = self.x + i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False
