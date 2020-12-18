class Queen:
    value = 1   # la valeur qui représente la reine dans l'échiquier 
    def __init__(self, y, x, board_size, board):
        self.y = y  # l'indice ligne de la reine
        self.x = x  # l'indice colonne de la reine
        self.board_size = board_size
        self.board = board

    # Une fonction qui vérifie si la reine peut attaquer une autre reine
    # Attention, cette fonction ne vérifie que les cases à droite, en bas, en diagonal bas gauche et droit de la reine
    # Utilisez cette fonction avec une boucle qui parcourt le board de gauche à droite et puis de haut en bas
    def can_attack(self):
        if (self.can_attack_right() 
                or self.can_attack_down() 
                or self.can_attack_diag_down_left() 
                or self.can_attack_diag_down_right()):
            return True
        return False


    # Une fonction qui vérifie si la reine peut attaquer (une autre reine) à sa droite
    def can_attack_right(self):
        for i in range(self.x + 1, self.board_size):
            if (self.board[self.y][i] == Queen.value):
                return True
        return False

    # Une fonction qui vérifie si la reine peut attaquer en bas
    def can_attack_down(self):
        for i in range(self.y + 1, self.board_size):
            if (self.board[i][self.x] == Queen.value):
                return True
        return False
         

    # Une fonction qui vérifie si la reine peut attaquer à sa diagonale bas gauche
    def can_attack_diag_down_left(self):
        i = 1
        while((self.board_size - (self.y + i)) > 0 and (self.x - i) >= 0):
            newY = self.y + i
            newX = self.x - i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False


    # Une fonction qui vérifie si la reine peut attaquer à sa diagonale bas droite
    def can_attack_diag_down_right(self):
        i = 1
        while((self.board_size - (self.y + i)) > 0 and (self.board_size - (self.x + i)) > 0):
            newY = self.y + i
            newX = self.x + i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False

    # Une fonction qui vérifie si l'emplacement de la reine n'est pas attaqué
    # Similaire à la function can_attack(self)
    # Attention, cette fonction ne vérifie que les cases à gauche, en diagonal haut gauche et en diagonal bas gauche de la reine
    # Utilisez cette fonction avec une boucle qui parcourt le board de haut en bas et puis de gauche à droite
    def can_be_placed(self):
        if (self.can_attack_left()
                or self.can_attack_diag_up_left() 
                or self.can_attack_diag_down_left()):
            return False
        return True

    # Une fonction qui vérifie si la reine peut attaquer (une autre reine) à sa gauche
    def can_attack_left(self):
        for i in range(self.x):
            if (self.board[self.y][i] == Queen.value):
                return True
        return False

    # Une fonction qui vérifie si la reine peut attaquer à sa diagonale haut gauche
    def can_attack_diag_up_left(self):
        i = 1
        while((self.y - i) >= 0 and (self.x - i) >= 0):
            newY = self.y - i
            newX = self.x - i
            if (self.board[newY][newX] == Queen.value):
                return True
            i += 1
        return False