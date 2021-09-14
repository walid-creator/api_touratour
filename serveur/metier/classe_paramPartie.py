class ParamPartie:
    def __init__(self, id_parametres, id_jeu, nomParam):
        self.id_paramPartie = id_paramPartie
        self.id_jeu = id_jeu
        self.nomParamPartie =nomParamPartie
    def __str__(self):
        return("id_parametres : {} //  id_jeu : {} // nomParamPartie : {}".format(self.id_paramPartie, self.id_jeu, self.nomParamPartie))


    


class ParametresPartie:
    def __init__(self, id_jeu):
        self.liste = []
        self.id_jeu = id_jeu
    def __str__(self):
        for i in range(len(self.liste)):
            print(self.liste[i])    
    def addparam(self,Parametre):
        self.liste.append(ParamPartie)
        return ParametreDao.create(ParamPartie)
