from serveur.dao.pool_connection import PoolConnection
from serveur.metier.pioche import Pioche
import psycopg2

class PiocheDao:


    def read(paq):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT paquet"
                "\n\t FROM Pioche "
                "\n\t WHERE id_partie = %s;",
                (paq.id_partie,)
                )
            resultat = curseur.fetchone()
            res = resultat["paquet"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res



    def update(paq):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Pioche"
                "\n\t SET paquet=%s"
                "\n\t WHERE id_partie=%s RETURNING paquet;"
                , (paq.pioche, paq.id_partie)
            )
            updated = curseur.fetchone()
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return updated



    def create(paq):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO Pioche (id_partie, paquet) "
                "VALUES (%s, %s) RETURNING paquet;"
                , (paq.id_partie
                   , paq.pioche)
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

    def read_mot(id_participant):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT paquet"
                "\n\t FROM Pioche "
                "\n\t INNER JOIN Partie ON Partie.id_partie = Pioche.id_partie"
                "\n\t INNER JOIN Participant ON Partie.id_partie = Participant.id_partie"
                "\n\t WHERE id_participant = %s;",
                (id_participant,)
                )
            resultat = curseur.fetchone()
            res = resultat["paquet"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res


    def update2(paq, id_partie):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Pioche"
                "\n\t SET paquet=%s"
                "\n\t WHERE id_partie=%s RETURNING paquet;"
                , (paq, id_partie)
            )
            updated = curseur.fetchone()
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return updated