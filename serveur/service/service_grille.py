from serveur.dao.classe_grille_dao import GrilleDao
from serveur.dao.classe_valeurPartie_dao import ValeurPartieDao
class ServiceGrille:
    #def creer(id_partie):
     #   if GrilleDao.initialisation(id_partie)==True:
      #      return 1
       # else:
        #    return 0
    def modifier(id_partie, numcase, valeur):
        if GrilleDao.update(id_partie, numcase, valeur) == True:
            return 1
        else:
            return 0

    def recuperer(id_partie,nb_cases):
        return GrilleDao.read(id_partie,nb_cases)

    def recupPions(id_partie):
        return ValeurPartieDao.readPions(id_partie)

    def pleine(id_partie):
        if GrilleDao.pleine(id_partie)==0:
            return 1
        else:
            return 0

    def aligner(id_partie,pion):
        if GrilleDao.alignementdao(id_partie,pion)==True:
            return 1
        else:
            return 0

    def verif_case(id_partie,numcase):
        if GrilleDao.verif_case(id_partie,numcase)==1:
            return 1
        else:
            return 0