from classe_joueur import Joueur
from classe_jeu import Jeu

class Statistiques:
    def __init__(self,id_statistiques, nivJeu, classementJeu, tempsTours, nbParties):
        self.id_statistiques = id_statistiques
        self.id_joueur = Joueur.id_Joueur
        self.id_jeu = Jeu.id_jeu
        self.nivJeu = nivJeu
        self.classementJeu = classementJeu
        self.tempsTours = tempsTours
        self.nbParties = nbParties
     
        #on considère temps tour une liste de tems de tours moyens de chaque partie
    def calculerNiveau(self):
        return self.nivJeu
    
    def tempstourmoyen(tempsTours):
        tps= 0
        for i in range len(tempsTours):
            tps+= tempsTours[i] #
        return tps/self.nbParties #tempsTours est une liste

