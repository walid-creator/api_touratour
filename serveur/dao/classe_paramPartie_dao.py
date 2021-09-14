from serveur.dao.pool_connection import PoolConnection
import psycopg2



class ParamPartieDao:

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
                "SELECT  id_parampartie, id_jeu, nomparampartie "
                "FROM parampartie;")
            resultats = curseur.fetchall()
            tab = []
            for i in resultats:
                tab.append([i["id_parampartie"],
                              i["id_jeu"],
                              i["nomparampartie"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return tab

    def find_by_id(id):
        """
        Obtenir un  parametre a partir de son id
        :param id: identifiant du parametre
        :type id: integer
        :return: le parametre dont l identifiant est id
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  id_paramPartie ,id_jeu, nomParamPartie,"
                "\n\t FROM ParamPartie",
                "\n\t Where id_paramPartie = %d", 
                (id,))
            resultats = curseur.fetchone()
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return resultats

    def update(ParamPartie): #c'est un objet de la classe paramètre qui contirnt les valeurs à rentrer
        """
        Modifier la valeur d'un paramètre
        :param Parametre: les nouvelles valeurs du paramètre à rentrer
        :type Parametre: objet de la classe ParamPartie
        :return: si le parametre a ete modifie
        :rtype: bool
        """
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE ParamPartie"
                "\n\t SET nomParamPartie = %s" #id_Parametres=1,2,3,4...
                "\n\t WHERE id_paramPartie=%d ;"
                , (ParamPartie.nomParamPartie, ParamPartie.id_paramPartie))

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

    def create(ParamPartie):
        """
        Ajouter une arme dans notre base de données.
        :param Parametre: le paramètre à ajouter
        :type Parametre: objet de la classe ParamPartie 
        :return: rien
        :rtype: rien
        """
        created = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO ParamPartie (id_paramPartie = %d, id_jeu  = %d ,nomParamPartie = %s"
                " VALUES (%d, %d, %d); "
                , (ParamPartie.id_paramPartie
                   , ParamPartie.id_jeu
                   , ParamPartie.nomParamPartie
                   )) 
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


    def delete_param(ParamPartie):
        """
            Supprime un parametre de la base 
            :param Parametre: le parametre à supprimer
            :type Parametre: objet de la classe ParamPartie 
            :return: si la suppresion a ete faite
            :rtype: bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
            "DELETE FROM ParamPartie WHERE id_paramPartie=%d;"
            , (ParamPartie.id_paramPartie,))
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