from serveur.dao.classe_statistiques_dao import StatistiquesDao

class ServiceStat:

    def stats_joueur(pseudo):
        return StatistiquesDao.read(pseudo)
