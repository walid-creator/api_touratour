class ValeurPartie:
    def __init__(self, id_valeurPartie, id_paramPartie, id_partie, ordrevaleurPartie, valeurPartie):
        self.id_valeurPartie = id_valeurPartie
        self.id_paramPartie = id_paramPartie
        self.id_partie = id_partie 
        self.ordrevaleurPartie = ordrevaleurPartie  
        self.valeurPartie = valeurPartie 
    def __str__(self):
        return("id_paramPartie : {} //  id_partie : {} // ordre_apparition : {}  // valeur : {}".format(self.id_paramPartie, self.id_partie, self.ordrevaleurPartie, self.valeurPartie))

class ValeursPartie:
    def __init__(self, id_partie, id_jeu, id_parametres):
        self.id_partie = id_partie
        self.id_jeu = id_jeu
        self.id_paramPartie = id_paramPartie
        self.liste = []
    def __str__(self):
        for i in range(len(self.liste)):
            print(self.liste[i])    
    def ajoutvalparam(self,Parametre_valeur):
        if Parametre_valeur.id_partie == self.id_partie and Parametre_valeur.id_jeu == self.id_jeu and Parametre_valeur.id_paramPartie == self.id_paramPartie:
            self.liste.append(Parametre_valeur)
            return valParametre_dao.createvaleur(Parametre_valeur)
        
