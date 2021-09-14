from serveur.dao.classe_valeurPartie_dao import ValeurPartieDao

class ServiceCase:
    def recup_nbcases(id_partie):
        return ValeurPartieDao.recup(id_partie)
