########## Classe jeu_dao ###########

# Fonctionnalités :
# - obtenir le nom d'un jeu par son id
# - btenir les informations (historique, règles, temps moyen) d'un jeu
# - obtenir tous les jeux disponibles et leur temps moyen
# - obtenir l'identifiant du jeu par son nom
# - mise à jour du temps moyen d'un jeu après la fin d'une partie


import psycopg2
#from classe_abstract_jeu import AbstractJeu
from serveur.dao.pool_connection import PoolConnection
#from serveur.metier.classe_abstract_jeu import AbstarctJeu

class JeuDao():
    
    def read(jeu):
        """
        Obtenir les infos d'un jeu dont on connait le nom.
        :param id: le nom du jeu
        :type id: string
        :return: les informations du jeu avec le bon nom
        :rtype: AbstarctJeu
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT id_jeu, nom, historique, regles, tempsmoyen"
                "\n\t FROM Jeu "
                "\n\t WHERE id_jeu = %d;",
                (jeu.id_jeu,)
                )
            resultat = curseur.fetchone()
            res = None
            # Si résultat obtenu #
            if resultat:
                res = AbstractJeu(id_jeu=resultat[0],
                              nom=resultat[1],
                              historique=resultat[2],
                              regles=resultat[3],
                              tempsMoyen=resultat[4])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res
    

    def read_all():
        """
        Obtenir tous les jeux dans la base de données.
        :return: tous les jeux de la base
        :rtype: list of Jeu
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT id_jeu, nom, historique, regles, tempsmoyen"
                "\n\t FROM Jeu;"
                )
            resultats = curseur.fetchall()
            jeux = []
            for i in resultats:
                jeux.append([
                          i["id_jeu"]
                        , i["nom"]
                        , i["historique"]
                        , i["regles"]
                        , i["tempsmoyen"]]
                )
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return jeux
    

    def update(jeu):
        ### ATTENTION : il faut que la partie soit en statut fin TRUE pour pouvoir prendre en compte le calcul
        ### faire un fonction qui gère le calcul
        """
        Mise à jour du temps moyen d'un jeu après la fin d'une partie.
        :param nome: le jeu dont il faut mettre le temps moyen d'une partie à jour.
        :type nom: AbstractJeu
        :return: si la mise à jour a bien été faite
        :rtype: booléen
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "UPDATE Jeu"
                "\n\t SET tempsmoyen = %f"
                "\n\t WHERE id_jeu = %d;",
                (jeu.tempsMoyen, jeu.id_jeu)
                )
            resultat=True
            # Enregistrement de la transaction #
            connexion.commit()
        except psycopg2.Error as error:
            # La transaction est annulée si une erreur est présente #
            connexion.rollback()
            resultat=False
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return resultat
    
