from serveur.dao.classe_joueur_dao import JoueurDao
from serveur.metier.classe_joueur import Joueur

class ServiceConnexion:

    def se_connecter(pseudo, mdp):
        """
        Vérifie si le pseudo et le mot de passe concordent dans la base de données
        :param: pseudo, mdp
        :return: vrai ou faux
        :rtype: bool
        """
        if JoueurDao.read(pseudo, mdp) == pseudo:
            joueur = Joueur(pseudo = pseudo)
            return True
        else:
            return False


