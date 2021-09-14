from abstract_jeu import AbstractJeu
from dao.classe_jeu_dao import JeuDao


class ServiceJeux:

    @staticmethod
    def get_all_monstres_from_db():
        """
        Récupère tous les jeux et leurs caractéristiques en base
        :return: une liste de jeux
        :rtype: list of AbstractJeu
        """
        return JeuDao.read_all()
    def recuper_grille():
        return GrilleDao.readall()
    def modifier_grille():
        if GrilleDao.update()==True:
            return 1
        else:
            return 0
    def supprimer_grille(self):
        return GrilleDao.delete()

    def verifier_sontour():
        return###