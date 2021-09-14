from serveur.dao.pool_connection import PoolConnection
from serveur.metier.pioche import Pioche
import psycopg2

class MainDao:


    def read(id_participant):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT mainjoueur"
                "\n\t FROM Main "
                "\n\t WHERE id_participant = %s;",
                (id_participant,)
                )
            resultat = curseur.fetchone()
            res = resultat["mainjoueur"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res



    def update(mano, id_partie):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Main"
                "\n\t SET mainjoueur=%s"
                "\n\t WHERE id_participant=%s RETURNING mainjoueur;"
                , (mano, id_partie)
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



    def create(mano):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO Main (id_participant, mainjoueur) "
                "VALUES (%s, %s) RETURNING mainjoueur;"
                , (mano.id_participant
                   , mano.mot)
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