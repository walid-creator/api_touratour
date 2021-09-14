########## Classe joueur_dao ###########

# Fonctionnalités :
# - créer un joueur
# - obtenir tous les joueurs
# - mettre à jour le mot de passe (pas le pseudo qui lui est définitif)


import psycopg2
from serveur.service.hachage import hash_mdp as h
from serveur.metier.classe_joueur import Joueur
from serveur.dao.pool_connection import PoolConnection


class JoueurDao():
    
    
    def create(id_joueur, pseudo, mdp):
        """
        Ajouter un joueur dans la base de données.
        :param joueur: joueur à ajouter
        :type joueur: Joueur
        :return: pseudo
        :rtype: Joueur
        """
        pseudo = str(pseudo)
        mdp = str(mdp)
        #id_joueur = int(id_joueur)
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO Joueur (id_joueur, pseudo, mdp)"
                " VALUES (%(id)s, %(pseudo)s, %(h)s)"
                "RETURNING pseudo;",
                {"id" : id_joueur,
                "pseudo" : pseudo,
                 "h" : h(mdp, pseudo)}
                )
            res = curseur.fetchone()
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res
  
    
    def read(pseudo, mdp):
        """
        Vérifier les informations sur un joueur.
        :param pseudo: pseudo du joueur
        :type pseudo: str
        :param mdp: mot de passe du joueur
        :type mdp: str
        :return: si la connexion est bonne
        :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT pseudo"
                "\n\t FROM Joueur "
                "\n\t WHERE pseudo = %s AND mdp = %s;",
                (pseudo, h(mdp, pseudo))    #h --> fonction de hashage avec salt=pseudo
                )
            resultat = curseur.fetchone()
            res = None
            # Si résultat obtenu #
            if resultat:
                res = resultat['pseudo']
                joueur = Joueur(pseudo = pseudo)
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res
    
    
    def read_all():
        """
        Obtenir tous les joueurs dans la base de données.
        :return: tous les joueurs de la base
        :rtype: list of Joueur
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT id_joueur, pseudo"
                "\n\t FROM Joueur;"
                )
            resultats = curseur.fetchall()
            len_res = len(resultats)
            joueurs = []
            for res in range(len_res):
                joueurs.append([resultats[res]["id_joueur"], resultats[res]["pseudo"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return joueurs


    def update(joueur, nvMdp):
        """
        Mettre à jour un mot de passe dans la base de données "Joueur". 
        Mise à jour de la ligne correspondant au joueur
        :param: le joueur dont il faut mettre le mot de passe à jour
        :type: Joueur
        :return: si la mise à jour a été faite
        :rtype: bool
        """
        resultat=False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "UPDATE Joueur"
                "\n\t SET mdp = %s"
                "\n\t WHERE pseudo = %s;",
                (h(nvMdp, joueur.pseudo), joueur.pseudo)
                )
            if curseur.rowcount > 0:
                resultat=True
            # Enregistrement de la transaction #
            connexion.commit()
        except psycopg2.Error as error:
            # La transaction est annulée si une erreur est présente #
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return resultat
