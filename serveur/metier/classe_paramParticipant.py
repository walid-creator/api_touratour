class ParamParticipant:
    def __init__(self, id_paramParticipant, id_jeu, nomParamParticipant):
        self.id_paramJoueur = id_paramJoueur 
        self.id_jeu = id_jeu
        self.nomParamParticipant = nomParamParticipant 
    def __str__(self):
        return("id_jeu : {} //  nomParam : {} // valeur : {}".format(self.id_jeu, self.nomParamParticipant))    

class ParamsParticipant:
    def __init__(self, id_jeu):
        self.liste=[]
        self.id_jeu = id_jeu
    def __str__(self):
        for i in range(len(self.liste)):
            print(self.liste[i])
    def ajouParam(self,ParamParticipant):
        self.liste.append(ParamParticipant)
        return Parametres_joueur_dao.create(Parametre_joueur)
