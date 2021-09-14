from serveur.dao.pool_connection import PoolConnection
import psycopg2


class StatistiquesDao:

    def read_all_Morpion():
        """
        Afficher tous les stat du morpion
        :param : rien
        :type id: rien
        :return: les stat des joeurs du jeu
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  pseudo, nivjeu, classementjeu, tempstour, nbpartie "
                "FROM Statistiques INNER JOIN Jeu ON Statistiques.id_jeu = Jeu.id_jeu "
                "WHERE nom='Morpion' DESC "
                "ORDER BY classementjeu "
                "LIMIT 10;")
            resultats = curseur.fetchall()
            stats = []
            for resultat in resultats:
                stats.append([resultat["pseudo"]
                             , resultat["nivjeu"]
                             , resultat["classementjeu"]
                             , resultat["nbpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return stats

    def read_all_1000B():
        """
        Afficher tous les stat du 1000 Bornes
        :param : rien
        :type id: rien
        :return: les stat des joeurs du jeu
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  pseudo, nivjeu, classementjeu, tempstour, nbpartie "
                "FROM Statistiques INNER JOIN Jeu ON Statistiques.id_jeu = Jeu.id_jeu "
                "WHERE nom='1000 Bornes' "
                "ORDER BY classementjeu DESC "
                "LIMIT 10;")
            resultats = curseur.fetchall()
            stats = []
            for resultat in resultats:
                stats.append([resultat["pseudo"]
                             , resultat["nivjeu"]
                             , resultat["classementjeu"]
                             , resultat["nbpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return stats

    
    def read_all():
        """
        Afficher tous les stat de chaque jeu
        :param : rien
        :type id: rien
        :return: les stat des joeurs de chaque jeu
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  id_statistiques, pseudo, id_jeu, nivjeu, classementjeu, tempstour, nbpartie "
                "FROM Statistiques;")
            resultats = curseur.fetchall()
            stats = []
            for i in resultats:
                stats.append([i["id_statistiques"],
                              i["pseudo"],
                              i["id_jeu"],
                              i["nivjeu"],
                              i["classementjeu"],
                              i["tempstour"],
                              i["nbpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return stats


    def update(statistiques):#objet de classe
        """
        Modifier une statistique de la base
        :param Statistique : la statistique a modifier
        :type Statistique: objet de la classe Statistique 
        :return: si la statistique a ete modifiee
        :rtype: bool
        """
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Statistiques"
                "\n\t SET nivJeu = %s, classementJeu = %d, tempsTours = %d, nbPartie= %d"
                "\n\t WHERE id_statistiques=%d ;"
                , (statistiques.nivJeu, statistiques.classementJeu, statistiques.tempsTours, statistiques.nbPartie, statistiques.id_statistiques))
            if curseur.rowcount > 0:
                updated = True
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
   

    def create(id_statistiques, pseudo, id_jeu, nivJeu, classementJeu, tempsTours, nbPartie):
        """
        Ajouter une statistique a la base
        :param Statistique: l'arme à ajouter
        :type Statistique: objet de classe statistique
        :return: rien
        :rtype: rien
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO Statistiques (id_statistiques, pseudo ,id_jeu, nivjeu, classementjeu, tempstour, nbpartie)"
                " VALUES (%(id)s, %(pseudo)s, %(jeu)s, %(niv)s, %(clas)s, %(temps)s, %(nbpart)s) RETURNING pseudo;",
                {"id": id_statistiques,
                "pseudo": pseudo,
                "jeu": id_jeu,
                "niv": nivJeu,
                "clas": classementJeu,
                "temps": tempsTours,
                "nbpart": nbPartie}
                )
            res = curseur.fetchone()
                # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res


    def delete(statistiques):
        """
            Supprime une statistique de la base
            :param Statistique: la statistique a supprimer
            :type Statistique: objet de la classe Statistique 
            :return: si la suppresion a ete faite
            :rtype: bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
            "DELETE FROM Statistiques WHERE id_statistiques=%d;"
            , (statistiques.id_statistiques,))
            # attention quand vous n'avez qu'un champ il faut garder une
            # structure de tuple et donc bien mettre un virgule avec
            # rien derrière

            # on verifie s'il y a eu des supressions
            if curseur.rowcount > 0:
                deleted = True
                # On enregistre la transaction en base
                connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

        return deleted

    def read(pseudo):
        """
        Afficher tous les stat de chaque jeu
        :param : rien
        :type id: rien
        :return: les stat des joeurs de chaque jeu
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  nom, pseudo, nivjeu, classementjeu, tempstour, nbpartie "
                "FROM Statistiques INNER JOIN Jeu ON Statistiques.id_jeu = Jeu.id_jeu "
                "WHERE Statistiques.pseudo=%s;",(pseudo,))
            resultats = curseur.fetchall()
            stats = []
            for i in resultats:
                stats.append([i["nom"]
                    , i["pseudo"]
                    , i["nivjeu"]
                    , i["classementjeu"]
                    , i["tempstour"]
                    , i["nbpartie"]]
                )
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return stats


    def read2(pseudo, id_jeu):
        """
        Afficher tous les stat de chaque jeu
        :param : rien
        :type id: rien
        :return: les stat des joeurs de chaque jeu
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  nivjeu, classementjeu, nbpartie "
                "FROM Statistiques "
                "WHERE pseudo=%s AND id_jeu=%s;",(pseudo, id_jeu))
            resultats = curseur.fetchall()
            stats = []
            for i in resultats:
                stats.append([i["nivjeu"]
                    , i["classementjeu"]
                    , i["nbpartie"]]
                )
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return stats


    def update2(nivjeu, classementjeu, nbpartie, pseudo, id_jeu):#objet de classe
        """
        Modifier une statistique de la base
        :param Statistique : la statistique a modifier
        :type Statistique: objet de la classe Statistique
        :return: si la statistique a ete modifiee
        :rtype: bool
        """
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Statistiques"
                "\n\t SET nivjeu = %s, classementjeu = %s, nbPartie= %s"
                "\n\t WHERE pseudo=%s AND id_jeu=%s RETURNING id_statistiques;"
                , (nivjeu, classementjeu, nbpartie, pseudo, id_jeu))

            res = curseur.fetchone()
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res