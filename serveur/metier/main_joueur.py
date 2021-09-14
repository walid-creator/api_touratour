

class Main:

    def __init__(self, id_participant, mot):
        self.id_participant = id_participant
        self.mot = mot

    def retourner_main(self):
        # fonction qui retourne les cartes dans une liste (scinde le mot en cartes de taille 4 lettres)
        L = []
        for i in range(int(len(self.mot)/4)):
            L += [self.mot[4*i:4*i+4]]
        return L