from serveur.dao.pool_connection import PoolConnection
import psycopg2

class StatutDao:

    def read(id_participant):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT id_participant, borne, feu, limite, essence, crevaison, accident, botte_pompier, botte_citerne, botte_roue, botte_volant"
                "\n\t FROM Statut "
                "\n\t WHERE id_participant = %s;",
                (id_participant,)
                )
            resultat = curseur.fetchall()
            #res = [resultat["borne"], resultat["feu"], resultat["limite"], resultat["essence"], resultat["crevaison"], resultat["accident"], resultat["botte_pompier"], resultat["botte_citerne"], resultat["botte_roue"], resultat["botte_volant"]]
            res = []
            for i in resultat:
                res.append([i["borne"], i["feu"], i["limite"], i["essence"], i["crevaison"], i["accident"], i["botte_pompier"], i["botte_citerne"], i["botte_roue"], i["botte_volant"]])
                #res = [resultat[1], resultat[2], resultat[3], resultat[4], resultat[5], resultat[6], resultat[7], resultat[8], resultat[9], resultat[10]]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res

    def read2(id_participant):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT id_participant, borne, feu, limite, essence, crevaison, accident, botte_pompier, botte_citerne, botte_roue, botte_volant"
                "\n\t FROM Statut "
                "\n\t WHERE id_participant = %s;",
                (id_participant,)
                )
            resultat = curseur.fetchall()
            #res = [resultat["borne"], resultat["feu"], resultat["limite"], resultat["essence"], resultat["crevaison"], resultat["accident"], resultat["botte_pompier"], resultat["botte_citerne"], resultat["botte_roue"], resultat["botte_volant"]]
            res = []
            for i in resultat:
                res.append([i["id_participant"], i["borne"], i["feu"], i["limite"], i["essence"], i["crevaison"], i["accident"], i["botte_pompier"], i["botte_citerne"], i["botte_roue"], i["botte_volant"]])
                #res = [resultat[1], resultat[2], resultat[3], resultat[4], resultat[5], resultat[6], resultat[7], resultat[8], resultat[9], resultat[10]]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res[0]



    def update(id_participant, statut):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Statut"
                "\n\t SET id_participant = %(id)s, borne = %(bor)s, feu = %(feu)s, limite = %(lim)s, essence = %(ess)s, crevaison = %(cre)s, accident = %(acc)s, botte_pompier = %(bo1)s, botte_citerne = %(bo2)s, botte_roue = %(bo3)s, botte_volant = %(bo4)s "
                "\n\t WHERE id_participant = %(id)s RETURNING id_participant;",
                {"id": str(statut[0]),
                 "bor": str(statut[1]),
                 "feu": str(statut[2]),
                 "lim": str(statut[3]),
                 "ess": str(statut[4]),
                 "cre": str(statut[5]),
                 "acc": str(statut[6]),
                 "bo1": str(statut[7]),
                 "bo2": str(statut[8]),
                 "bo3": str(statut[9]),
                 "bo4": str(statut[10])}
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



    def create(liste):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO Statut (id_participant, borne, feu, limite, essence, crevaison, accident, botte_pompier, botte_citerne, botte_roue, botte_volant) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_participant;"
                , (liste.statut[0], liste.statut[1], liste.statut[2], liste.statut[3], liste.statut[4], liste.statut[5], liste.statut[6], liste.statut[7], liste.statut[8], liste.statut[9], liste.statut[10]))
            res = curseur.fetchone()
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res







    def update2(id_participant, statut):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Statut"
                "\n\t SET borne = %(bor)s"
                "\n\t WHERE id_participant = %(id)s RETURNING id_participant;"
                ,
                {"id": str(statut[0]),
                 "bor": str(statut[1])}
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