from serveur.dao.classe_jeu_dao import JeuDao

class Service_Tache:

    def retrouveTousLesNoms() -> [str]:
        return JeuDao.read_all()