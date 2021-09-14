from serveur.dao.pool_connection import PoolConnection
import psycopg2



class ValeurPartieDao:


    def recupp(choix):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT valeurpartie "
                "FROM valeurpartie "
                "WHERE id_partie= %s AND id_parampartie=4;", (choix,))
            resultats = curseur.fetchall()
            table = []
            for i in resultats:
                table.append([i["valeurpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return table

    def recup(id_partie):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT valeurpartie "
                "FROM valeurpartie "
                "WHERE id_partie= %s AND id_parampartie=2;", (id_partie,))
            resultats = curseur.fetchall()
            table = []
            for i in resultats:
                table.append([i["valeurpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return table

    def recupl(choix):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT valeurpartie "
                "FROM valeurpartie "
                "WHERE id_partie= %s AND id_parampartie=1;", (choix,))
            resultats = curseur.fetchall()
            table = []
            for i in resultats:
                table.append([i["valeurpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return table

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
                "SELECT  id_valeurpartie, id_parampartie, id_partie, ordrevaleurpartie, valeurpartie "
                "FROM valeurpartie;")
            resultats = curseur.fetchall()
            table = []
            for i in resultats:
                table.append([i["id_valeurpartie"],
                              i["id_parampartie"],
                              i["id_partie"],
                              i["ordrevaleurpartie"],
                              i["valeurpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return table

    def recupp1(choix):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT valeurpartie "
                "FROM valeurpartie "
                "WHERE id_partie= %s AND id_parampartie=3;", (choix,))
            resultats = curseur.fetchall()
            table = []
            for i in resultats:
                table.append([i["valeurpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return table

    def recuppremier(choix):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT valeurpartie "
                "FROM valeurpartie "
                "WHERE id_partie= %s AND id_parampartie=5;", (choix,))
            resultats = curseur.fetchall()
            table = []
            for i in resultats:
                table.append([i["valeurpartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return table

    def update(Parametre_valeur): #c'est un objet de la classe ValeurPartie qui contient les valeurs à rentrer
        """
        Modifier la valeur d'un parametre dans la base.
        :param Parametre_valeur: le parametre a modifier
        :type id: un objet de la classe ValeurPartie
        :return: si la valeur du parametre a ete modifiee
        :rtype: bool
        """

        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE ValeurPartie"
                "\n\t SET ordreValeurPartie = %s"
                "\n\t WHERE id_valeurPartie=%d ;"
                , ( Parametre_valeur.ValeurPartie
                   , Parametre_valeur.ordreValeurPartie
                   ,Parametre_valeur.id_paramPartie))

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

    def create(id_valeurPartie, id_paramPartie, id_partie,ordrevaleurPartie, valeurPartie):
        """
        Ajouter une valaeur aux valeurs possibles d'un parametre dans la base
        :param Parametre_valeur: la valeur a ajouter
        :type Parametre_valeur: objet de la classe ValeurPartie
        :return: rien
        :rtype: rien
        """
        created= False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO valeurpartie VALUES (%s, %s, %s, %s, %s) ;"
                , (id_valeurPartie
                   , id_paramPartie
                   , id_partie
                   , ordrevaleurPartie
                   , valeurPartie
                   ))
                # On récupère l'id généré
            if curseur.rowcount > 0:
                created = True
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return created


    def delete(Parametre_valeur):
        """
            Supprime une valeur d un parametre de la base
            :param Parametre_valeur: la valeur a supprimer
            :type Parametre_valeur: objet de la classe ValeurPartie
            :return: si la suppresion a ete faite
            :rtype: bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
            "DELETE FROM ValeurPartie WHERE id_valeurPartie=%d;"
            , (Parametre_valeur.id_valeurPartie,))
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
    def readPions(id_partie):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "SELECT valeurPartie FROM ValeurPartie WHERE id_partie=%s;"
                , (id_partie ,))
            # attention quand vous n'avez qu'un champ il faut garder une
            # structure de tuple et donc bien mettre un virgule avec
            # rien derrière
                # On enregistre la transaction en base
            resultat = curseur.fetchall()
            len_res = len(resultat)
            pions = []
            for res in range(len_res):
                pions.append(resultat[res])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return pions



