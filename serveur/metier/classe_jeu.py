from classe_abstract_jeu import *

########## Classes Morpion et 1000Bornes ###########

class Morpion(AbstractJeu):
    
    def __init__(self, id_jeu, nom, regles, historique, tempsMoyen):
        AbstractJeu.__init__(id_jeu, nom, regles, historique, tempsMoyen)


class MilleBornes(AbstractJeu):

    def __init__(self, id_jeu, nom, regles, historique, tempsMoyen):
        AbstractJeu.__init__(id_jeu, nom, regles, historique, tempsMoyen)
