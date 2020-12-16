class Queen:
    value = 1   # la valeur qui représente la reine dans l'échiquier 
    def __init__(self, y, x, board_size, board):
        assert board[y][x] == Queen.value
        self.y = y  # l'indice de la ligne
        self.x = x  # l'indice de la colonne
        self.board_size = board_size
        self.board = board

    # Une fonction qui vérifie si la reine peut attaquer une autre reine
    def can_attack(self):
        if (self.can_attack_right() 
                or self.can_attack_down() 
                or self.can_attack_diag_left() 
                or self.can_attack_diag_right()):
            return True
        return False


    # Une fonction qui vérifie si la reine peut attaquer (une autre reine) à sa droite
    def can_attack_right(self): #Steven
        for i in range(self.x + 1, self.board_size):
            if (self.board[self.y][i] == Queen.value):
                print(str(self.y) + " " + str(i))
                return True
        return False

    # Une fonction qui vérifie si la reine peut attaquer en bas
    def can_attack_down(self): #Steven
        for i in range(self.y + 1, self.board_size):
            if (self.board[i][self.x] == Queen.value): 
                print(str(i) + " " + str(self.x))
                return True
        return False
         

    # Une fonction qui vérifie si la reine peut attaquer à sa diagonale gauche
    def can_attack_diag_left(self): #Steven
        i = 1
        while((self.board_size - (self.y + i)) > 0 and (self.x - i) >= 0):
            newY = self.y + i
            newX = self.x - i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False


    # Une fonction qui vérifie si la reine peut attaquer à sa diagonale droite
    def can_attack_diag_right(self): #Steven
        i = 1
        while((self.board_size - (self.y + i)) > 0 and (self.board_size - (self.x + i)) > 0):
            newY = self.y + i
            newX = self.x + i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False
