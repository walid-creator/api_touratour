from serveur.dao.classe_statistiques_dao import StatistiquesDao

class Service_Classement:

    def retrouveStatsMorpion() -> [str]:
        return StatistiquesDao.read_all_Morpion()

    def retrouveStats1000B() -> [str]:
        return StatistiquesDao.read_all_1000B()
