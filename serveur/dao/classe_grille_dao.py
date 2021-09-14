from serveur.metier.classe_grille import Grille
import psycopg2
from serveur.dao.pool_connection import PoolConnection
from math import *
from serveur.dao.classe_valeurPartie_dao import ValeurPartieDao

class GrilleDao:
    def read(id_partie,nb_cases):
        
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT numcase, valeur "
                "FROM grille WHERE id_partie=%s;",(id_partie,)
            )
            resultat = curseur.fetchall()

            imax = int(sqrt(nb_cases))
            
            res = Grille(imax, id_partie).initialisation()
            #Si résultat obtenu
            jeux = []
            for t in resultat:
                for i in range(0, imax):
                    for j in range(0, imax):
                        if t["numcase"]==i*imax+j:
                            res[i][j]= t["valeur"]


        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res

    def update(id_partie, numcase, valeur):
        
        resultat = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO grille VALUES (%s, %s, %s);",
                (id_partie,numcase,valeur))

            if curseur.rowcount > 0:
                resultat = True
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
    

    def pleine(id_partie):
        nb_cases=int(ValeurPartieDao.recup(id_partie)[0][0])
        grille = GrilleDao.read(id_partie,nb_cases)
        c=0
        nbr=int(sqrt(nb_cases))
        for i in range(nbr):
            for j in range(nbr):
                if grille[i][j]== ' ':
                    c=1
        return c

    def verif_case(id_partie,numcase):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT numcase "
                "FROM grille WHERE id_partie=%s;", (id_partie,)
            )
            resultat = curseur.fetchall()
            table = []
            for i in resultat:
                table.append([i["numcase"]])
            c=0
            for i in range(len(table)):
                if numcase==int(table[i][0]):
                    c=1

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return c


    def alignementdao(id_partie,pion):
        nb_cases=int(ValeurPartieDao.recup(id_partie)[0][0])
        grille=GrilleDao.read(id_partie,nb_cases)
        pion1= ValeurPartieDao.recupp1(id_partie)[0][0]
        pion2= ValeurPartieDao.recupp(id_partie)[0][0]
        if pion==pion1:
            pion3=pion2
        else:
            pion3=pion1

        if Grille.alignement(grille, pion) ==True:
            return 1
        elif Grille.alignement(grille, pion3) ==True:
            return 2
        else:
            return 0
