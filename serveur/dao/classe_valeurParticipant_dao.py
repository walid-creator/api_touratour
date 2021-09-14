from dao.pool_connection.py import PoolConnection



class ValeurParticipantDao:
    
    def create(ValeurParticipant):
        """
        Ajoute une valeur d'un parametre de participant a la base
        :param Parametre_participation: la valeur a ajouter
        :type Parametre_participation: objet de la classe ValeurParticipant
        :return: rien
        :rtype: rien
        """
        created= False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO ValeurParticipant (id_valeurParticipant,id_paramParticipant,id_participant ,ordreParticipant,valeurParticipant)"
                " VALUES (%s,%s,%s,%s, %s) " 
                , (ValeurParticipant.id_valeurParticipant
                   , ValeurParticipant.id_paramParticipant
                   , ValeurParticipant.id_participant
                   , ValeurParticipant.ordreParticipant
                   , ValeurParticipant.id_paramParticipant
                   ,ValeurParticipant.valeurParticipant
                   ))
            if curseur.rowcount > 0:
                created= False
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return created


    def delete(ValeurParticipant):
        """
            Supprime la valeur d un parametre d un participant de la base
            :param Parametre_participation: le valeur du parametre a supprimer
            :type Parametre_participation: objet de la classe ValeurParticipant
            :return: si la suppresion a ete faite 
            :rtype: bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            
            curseur.execute(
            "DELETE FROM ValeurParticipant WHERE id_valeurParticipant=%d;"
            , (ValeurParticipant.id_valeurParticipant,)
            )
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
            
    def update(ValeurParticipant): #c'est un objet de la classe paramètre qui contirnt les valeurs à rentrer
        """
            Modifie uen valeur d un parametre d un participant de la base
            :param Parametre_participation: la valeur du parametre a supprimer
            :type Parametre_participation: objet de la classe ValeurParticipant
            :return: si la suppresion a ete faite 
            :rtype: bool
        """
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE ValeurParticipant"
                "\n\t SET valeurParticipant %s, ordreParticipant" #id_Parametres=1,2,3,4...
                "\n\t WHERE id_valeurParticipant=%d ;"
                , (ValeurParticipant.valeurParticipant, ValeurParticipant.ordreParticipant,ValeurParticipant.id_valeurParticipant)
                ) 

            if curseur.rowcount > 0:
                updated = True

            # On enregistre la transaction en base
            connexion.commit()
        except psycopg.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return updated
