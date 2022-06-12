class Validator:
    """
    Validator class
    """
    def valid_move(self, x, y, i, j):
        """
        Validates moves
        :param x: old x
        :param y: old y
        :param i: new x
        :param j: new y
        :return:
        """
        if i < 0 or i > 2: #Checks map boundaries
            return False
        if j < 0 or j > 2: #Checks map boundaries
            return False
        if abs(i-x) > 1 or abs(j-y) > 1: #Check if moves are adjacent
            return False

        return True

    def valid_placement(self, i, j):
        if i < 0 or i > 2: #Checks map boundaries
            return False
        if j < 0 or j > 2: #Checks map boundaries
            return False
        return True
