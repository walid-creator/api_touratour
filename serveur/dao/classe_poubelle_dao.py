from serveur.dao.pool_connection import PoolConnection
from serveur.metier.poubelle import Poubelle
import psycopg2

class PoubelleDao:


    def read(id_partie):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT paquet"
                "\n\t FROM Poubelle "
                "\n\t WHERE id_partie = %s;",
                (id_partie,)
                )
            resultat = curseur.fetchone()
            res = resultat["paquet"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res



    def update(paquet, id_partie):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Poubelle"
                "\n\t SET paquet=%s"
                "\n\t WHERE id_partie=%s RETURNING paquet;"
                , (paquet, id_partie)
            )
            updated = curseur.fetchall()
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
                "INSERT INTO Poubelle (id_partie, paquet) "
                "VALUES (%s, %s) RETURNING paquet;"
                , (paq.id_partie
                   , paq.paquet)
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
