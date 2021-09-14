from serveur.metier.classe_joueur import Joueur
from serveur.dao.classe_joueur_dao import JoueurDao


class ServiceModifierMdp:
    def modifMdp(pseudo, nvMdp):
        """
        Vérifie si mdp vérifie les contraintes et modifie mot de passe du joueur
        param nvMdp: nouveau mot de passe à affecter au joueur
        :type nvMdp: chaine de caractères
        :return: 0 ou 2
        :rtype: int
        """
        joueur=Joueur(pseudo)
        JoueurDao.update(joueur,nvMdp)            ### création du joueur dans la base
        if JoueurDao.update(joueur, nvMdp) == True:
            return 2
        else:
            return 0                


