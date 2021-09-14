from serveur.dao.pool_connection import PoolConnection



class ParamParticipantDao:
    def create(param):
        """
        Ajouter un participant dans la base
        :param ParamParticipant: la Parametre d un participant 
        :type ParamParticipant: un objet de la classe ParamParticipant
        :return: rien
        :rtype: rien
        """
        created=False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO ParamParticipant (id_paramParticipant,id_jeu ,nomParamParticipant)"
                " VALUES (%d,%d, %s);" 
                , (param.id_assoParticip
                   , param.id_participation
                   , param.id_paramJoueur
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


    def delete(ParamParticipant):
        """
            Supprime un parametre de participant de la base
            :param ParamParticipant: le parametre a supprimer
            :type ParamParticipant: objet de la classe ParamParticipant
            :return: si la suppression a ete faite
            :rtype: bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            
            curseur.execute(
            "DELETE FROM ParamParticipant WHERE id_paramParticipant=%d;"
            , (param.id_assoParticip,
                   ))
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

    def read(id_participant, nomParam):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT valeur"
                "\n\t FROM parametreparticipant "
                "\n\t Where id_participant=%s AND nomparam=%s;",
                (id_participant,nomParam)
            )
            resultats = curseur.fetchall()
            res=resultats["pions"]

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res

