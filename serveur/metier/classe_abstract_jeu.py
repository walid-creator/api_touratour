########## Classe abstract_jeu ###########

class AbstractJeu:
    
    def __init__(self, id_jeu, nom, regles, historique, tempsMoyen):
        self.id_jeu = id_jeu
        self.nom = nom
        self.regles = regles
        self.historique = historique
        self.tempsMoyen = tempsMoyen
    
    def calculer_tempsMoyen(self, nbPartie, moyenneTempsTour):
        self.tempsMoyen = moyenneTempsTour / nbPartie
        return self.tempsMoyen
