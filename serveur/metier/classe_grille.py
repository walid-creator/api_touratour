class Grille:
    def __init__(self, imax,id_partie):
        self.imax = imax
        self.id_partie = id_partie

    def initialisation(self):
        grille = []
        for i in range(0, self.imax):
            grille.append([])
            for j in range(0, self.imax):
                grille[i].append(' ')
        return grille

    def alignement(grille, pion):
        cases = len(grille)
        x = []
        for i in range(cases):
            x.append(pion)

        if cases == 3:
            if grille[0] == x or grille[1] == x or grille[2] == x or [grille[0][0],grille[1][0],grille[2][0]] == x or [grille[0][1],grille[1][1],grille[2][1]] == x or [grille[0][2],grille[1][2],grille[2][2]] == x or [grille[0][0],grille[1][1],grille[2][2]] == x or [grille[0][2],grille[1][1],grille[2][0]] == x:
                return True
            else:
                return False

        elif cases == 4:
            if grille[0] == x or \
                grille[1] == x or \
                grille[2] == x or \
                grille[3] == x or \
                [grille[0][0],grille[1][0],grille[2][0],grille[3][0]] == x or \
                [grille[0][1],grille[1][1],grille[2][1],grille[3][1]] == x or \
                [grille[0][2],grille[1][2],grille[2][2],grille[3][2]] == x or \
                [grille[0][3],grille[1][3],grille[2][3],grille[3][3]] == x or \
                [grille[0][3],grille[1][2],grille[2][1],grille[3][0]] == x or \
                [grille[0][0],grille[1][1],grille[2][2],grille[3][3]] == x:
                return True

            else:
                return False

        elif cases == 5:
            if grille[0] == x or \
                    grille[1] == x or \
                    grille[2] == x or \
                    grille[3] == x or \
                    grille[4] == x or \
                    [grille[0][0],grille[1][0],grille[2][0],grille[3][0],grille[4][0]] == x or \
                    [grille[0][1],grille[1][1],grille[2][1],grille[3][1],grille[4][1]] == x or \
                    [grille[0][2],grille[1][2],grille[2][2],grille[3][2],grille[4][2]] == x or \
                    [grille[0][3],grille[1][3],grille[2][3],grille[3][3],grille[4][3]] == x or \
                    [grille[0][4],grille[1][4],grille[2][4],grille[3][4],grille[4][4]] == x or \
                    [grille[0][4],grille[1][3],grille[2][2],grille[3][1],grille[4][0]] == x or \
                    [grille[0][0],grille[1][1],grille[2][2],grille[3][3],grille[4][4]] == x:
                return True
            else:
                return False


            
