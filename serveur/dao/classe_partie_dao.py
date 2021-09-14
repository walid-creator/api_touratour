from serveur.dao.pool_connection import PoolConnection
from serveur.metier.classe_partie import Partie
import psycopg2

class PartieDao:

    def read(id_partie):
        """
        Obtenir les infos d'une partie dont on connait l'id.
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
                "SELECT id_partie, parampartie, statutfin, nbjoueurs"
                "\n\t FROM Partie "
                "\n\t WHERE id_partie = %s;",
                (id_partie,)
                )
            resultats = curseur.fetchall()
            len_res = len(resultats)
            result = []
            for res in range(len_res):
                result.append([resultats[res]["id_partie"], resultats[res]["parampartie"], resultats[res]["statutfin"], resultats[res]["nbjoueurs"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return result


    def read2(id_partie):
        """
        Obtenir les infos d'une partie dont on connait l'id.
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
                "SELECT numerotour"
                "\n\t FROM Partie "
                "\n\t WHERE id_partie = %s;",
                (id_partie,)
                )
            resultat = curseur.fetchone()
            result = resultat["numerotour"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return result



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
                "SELECT id_partie, id_jeu, temps, statutfin, parampartie"
                "\n\t FROM Partie;"
            )
            resultats = curseur.fetchall()
            parties = []
            for resultat in resultats:
                parties.append([resultat["id_partie"]
                        , resultat["id_jeu"]
                        , resultat["temps"]
                        , resultat["statutfin"]
                        , resultat["parampartie"]]
                               )
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return parties


    def update(partie): #update du nombre du nb de joueur
        """
        Modifie un participant de la base
        :param Participant: la Participation a modifier
        :type Participant: objet de la classe
        :return: si la modification a été faite
        :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Partie"
                "\n\t SET temps=%s, statutfin=%s, parampartie=%s, nbjoueurs=%s, numerotour=%s"
                "\n\t WHERE id_partie=%s RETURNING id_partie;"
                , (partie.temps, partie.statutfin, partie.parampartie, partie.nbjoueurs, partie.numerotour, partie.id_partie)
            )
            updated = curseur.fetchone()
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return updated


    def update2(id_partie, statutfin): #update du nombre du nb de joueur
        """
        Modifie un participant de la base
        :param Participant: la Participation a modifier
        :type Participant: objet de la classe
        :return: si la modification a été faite
        :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Partie"
                "\n\t SET statutfin=%s"
                "\n\t WHERE id_partie=%s RETURNING id_partie;"
                , (statutfin, id_partie)
            )
            updated = curseur.fetchone()
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return updated




    def update3(id_partie, numerotour):
        """
        Modifie un participant de la base
        :param Participant: la Participation a modifier
        :type Participant: objet de la classe
        :return: si la modification a été faite
        :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Partie"
                "\n\t SET numerotour=%s"
                "\n\t WHERE id_partie=%s RETURNING id_partie;"
                , (numerotour, id_partie)
            )
            updated = curseur.fetchone()
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return updated


    def create(partie):
        """
        Ajouter un participant dans notre base de données.
        :param Participation: la Participation à ajouter
        :type Participation: Objet de classe
        :return: rien
        :rtype: rien
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO Partie (id_partie, id_jeu, temps, statutfin, parampartie, nbjoueurs, numerotour)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_partie;"
                , (partie.id_partie
                   , partie.id_jeu
                   , partie.temps
                   , partie.statutfin
                   , partie.parampartie
                   , partie.nbjoueurs
                   , partie.numerotour))
                # On récupère l'id généré
            res = curseur.fetchone()
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res
    #
    #
    # def delete(partie):
    #     """
    #         Supprime une participant de la base
    #         :param participant: le participation à supprimer
    #         :type participant: objet de classe Participation
    #         :return: si la suppresion a ete faite
    #         :rtype: bool
    #     """
    #     deleted = False
    #     connexion = PoolConnection.getConnexion()
    #     curseur = connexion.cursor()
    #     try:
    #         # On envoie au serveur la requête SQL
    #         curseur.execute(
    #         "DELETE FROM Partie WHERE id_partie=%d;"
    #         , (partie.id_partie,))
    #         # attention quand vous n'avez qu'un champ il faut garder une
    #         # structure de tuple et donc bien mettre un virgule avec
    #         # rien derrière
    #
    #         # on verifie s'il y a eu des supressions
    #         if curseur.rowcount > 0:
    #                 deleted = True
    #
    #             # On enregistre la transaction en base
    #         connexion.commit()
    #     except psycopg2.Error as error:
    #         # la transaction est annulée
    #         connexion.rollback()
    #         raise error
    #     finally:
    #         curseur.close()
    #         PoolConnection.putBackConnexion(connexion)
    #     return deleted

    def read_all_att(X):
        """
        Obtenir toutes les parties en attente de joueurs dans la base de données.
        :return: toutes les parties de 1000B en attente de joueur de la base
        :rtype: liste de parties
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT id_partie, id_jeu, temps, parampartie, statutfin, nbjoueurs "
                "FROM Partie  "
                "WHERE statutfin = 0 AND id_jeu = %s ;"
                , (int(X), )
            )
            resultats = curseur.fetchall()
            parties = []
            for res in resultats:
                parties.append([res["id_partie"], res["id_jeu"], res["temps"], res["parampartie"], res["statutfin"], res["nbjoueurs"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return parties


    def read_all_attM(X):
        """
        Obtenir toutes les parties en attente de joueurs dans la base de données.
        :return: toutes les parties de 1000B en attente de joueur de la base
        :rtype: liste de parties
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT Partie.id_partie, id_jeu, temps, parampartie, statutfin, nbjoueurs, valeurpartie "
                "FROM Partie INNER JOIN valeurpartie ON Partie.id_partie=valeurpartie.id_partie "
                "WHERE statutfin = 0 AND Partie.id_jeu = %s AND valeurpartie.id_parampartie=1;"
                , (int(X), )
            )
            resultats = curseur.fetchall()
            parties = []
            for res in resultats:
                parties.append([res["id_partie"], res["id_jeu"], res["temps"], res["parampartie"], res["statutfin"], res["nbjoueurs"], res["valeurpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return parties
