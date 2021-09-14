from serveur.dao.classe_valeurPartie_dao import ValeurPartieDao

class ServicePion:
    def recup_pion(choix):
        return ValeurPartieDao.recupp(choix)
    def recup_pion1(choix):
        return ValeurPartieDao.recupp1(choix)

