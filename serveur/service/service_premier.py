from serveur.dao.classe_valeurPartie_dao import ValeurPartieDao

class ServicePremier:
    def recup_premier(choix):
        return ValeurPartieDao.recuppremier(choix)
