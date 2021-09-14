from serveur.dao.classe_valeurPartie_dao import ValeurPartieDao

class ServiceLangue:
    def recup_langue(choix):
        return ValeurPartieDao.recupl(choix)
