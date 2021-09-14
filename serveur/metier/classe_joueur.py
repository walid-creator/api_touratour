#from serveur.dao.classe_joueur_dao import JoueurDao


########## Classe joueur ###########

class Joueur:
    # initialisation de la classe Joueur
    # attributs : pseudo, mdp (cypher)
    def __init__(self, pseudo):
        self.pseudo = pseudo
    
    def modifier_mdp(self):
        """
        Modifie le mot de passe d'un joueur
        :param nouveauMdp: le nouveau mdp du joueur en question
        :type nouveauMdp: string 
        :return: si la modification a bien été prise en compte
        :rtype: bool
        """
        print('Votre mot de passe doit faire au moins 10 caractères et inférieur \n')
        nouveauMdp = input('Nouveau mot de passe :')
        nouveauMdp = str(nouveauMdp)

        if len(nouveauMdp) < 10:
            print("Votre mot de passe doit être supérieur à 10 caractères")
            return modifier_mdp(self)
        else:
            return JoueurDao.update(self, nouveauMdp)
    
    def supprimer_joueur(self):
        """
        Supprime le compte du joueur
        :param: le joueur connecté
        :type: objet
        :return: si la suppression a bien été prise en compte
        :rtype: bool
        """
        return JoueurDao.delete(self)
