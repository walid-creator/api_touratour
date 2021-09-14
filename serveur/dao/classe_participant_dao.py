from serveur.dao.pool_connection import PoolConnection
import psycopg2

class ParticipantDao:
    def modif_tour(id_participant,tour):
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Participant"
                "\n\t SET sontour=%s"
                "\n\t WHERE id_participant=%s;"
                , (tour,id_participant)
            )

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

    def read_all():
        """
                Obtenir toutes les parties en attente de joueurs dans la base de données.
                :return: toutes les parties de 1000B en attente de joueur de la base
                :rtype: liste de parties
                """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # Envoi de la requête SQL au serveur #
            curseur.execute(
                "SELECT id_participant "
                "FROM Participant;"
            )
            resultats = curseur.fetchall()
            participants = []
            for res in resultats:
                participants.append([res["id_participant"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return participants




    # def find_by_id(participant):
    #     """
    #         Cherche le participant dans la base a partir de son identifiant
    #         :param id: l identifiant d un participant
    #         :type id: Integer
    #         :return: le participant
    #         :rtype: list
    #     """
    #     connexion = PoolConnection.getConnexion()
    #     curseur = connexion.cursor()
    #     try:
    #         curseur.execute(
    #             "SELECT  id_participant ,id_joueur, id_partie, score, classementPartie"
    #             "\n\t FROM Participant",
    #             "\n\t Where id_participant = %d;",
    #             (participant.id_participant,))
    #         resultats = curseur.fetchall()
    #     finally:
    #         curseur.close()
    #         PoolConnection.putBackConnexion(connexion)
    #     return resultats
    

    def find_participant(id_partie):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  pseudo"
                "\n\t FROM Participant"
                "\n\t WHERE id_partie = %s;",
                (id_partie,))
            resultats = curseur.fetchall()
            participants = []
            for res in resultats:
                participants.append([res["pseudo"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return participants


    def find_participant_pseudo(id_participant):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  pseudo"
                "\n\t FROM Participant"
                "\n\t WHERE id_participant = %s;",
                (id_participant,))
            res = curseur.fetchone()
            participant = res["pseudo"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return participant



    def find_id_participant(id_partie, pseudo):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  id_participant"
                "\n\t FROM Participant"
                "\n\t WHERE id_partie = %s AND pseudo = %s;",
                (id_partie, pseudo))
            resultats = curseur.fetchall()
            participants = []
            for res in resultats:
                participants.append([res["id_participant"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return participants

    def find_id_participant_ordre(id_partie, ordre):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  id_participant"
                "\n\t FROM Participant"
                "\n\t WHERE id_partie = %s AND ordreparticipant = %s;",
                (id_partie, ordre))
            res = curseur.fetchone()
            participant = res["id_participant"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return participant


    def find_id_partie(id_participant):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  id_partie"
                "\n\t FROM Participant"
                "\n\t WHERE id_participant = %s;",
                (id_participant,)
            )
            res = curseur.fetchone()
            partie = res["id_partie"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return partie


    def find_ordre(id_participant):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  ordreparticipant"
                "\n\t FROM Participant"
                "\n\t WHERE id_participant = %s;",
                (id_participant,)
            )
            res = curseur.fetchone()
            partie = res["ordreparticipant"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return partie


    def find_id_participant_all(id_partie):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  id_participant"
                "\n\t FROM Participant"
                "\n\t WHERE id_partie = %s;",
                (id_partie,))
            resultats = curseur.fetchall()
            participants = []
            for res in resultats:
                participants.append([res["id_participant"]])
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return participants


    def update(participant, nvordre): #c'est un objet de la classe paramètre qui contient les valeurs à rentrer
        """
            Modifie un participant de la base
            :param Participant: la Participation a modifier
            :type Participant: objet de la classe
            :return: si la modification a été faite
            :rtype: bool
        """
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Participant"
                "\n\t SET score=%s, classementpartie=%s, ordreparticipant=%s, enjeu=%s"
                "\n\t WHERE id_participant=%;"
                , (participant.score, participant.classementPartie, participant.ordreParticipant, participant.enJeu, participant.id_participation)
            )

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



    def update2(id_partie, nvordre, pseudo): #c'est un objet de la classe paramètre qui contient les valeurs à rentrer
        """
            Modifie un participant de la base
            :param Participant: la Participation a modifier
            :type Participant: objet de la classe
            :return: si la modification a été faite
            :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Participant"
                "\n\t SET ordreparticipant=%s"
                "\n\t WHERE id_partie=%s AND pseudo=%s RETURNING id_participant;"
                , (nvordre, id_partie, pseudo)
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

    def update3(id_partie, sontour, pseudo): #c'est un objet de la classe paramètre qui contient les valeurs à rentrer
        """
            Modifie un participant de la base
            :param Participant: la Participation a modifier
            :type Participant: objet de la classe
            :return: si la modification a été faite
            :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Participant"
                "\n\t SET sontour=%s"
                "\n\t WHERE id_partie=%s AND pseudo=%s RETURNING id_participant;"
                , (sontour, id_partie, pseudo)
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


    def update4(id_participant, score, classement, enjeu): #c'est un objet de la classe paramètre qui contient les valeurs à rentrer
        """
            Modifie un participant de la base
            :param Participant: la Participation a modifier
            :type Participant: objet de la classe
            :return: si la modification a été faite
            :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Participant"
                "\n\t SET score=%s, classementpartie=%s, enjeu=%s"
                "\n\t WHERE id_participant=%s RETURNING id_participant;"
                , (score, classement, enjeu, id_participant)
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







    def create(participant):
        """
        Ajouter un participant dans notre base de données.
        :param Participation: la Participation à ajouter
        :type Participation: Objet de classe
        :return: rien
        :rtype: rien
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO Participant (id_participant, pseudo, id_partie, score, classementpartie, ordreparticipant, enjeu, sontour) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) " 
                "RETURNING id_participant;",
                (participant.id_participant
                   , participant.pseudo
                   , participant.id_partie
                   , participant.score
                   , participant.classement
                   , participant.ordre
                   , participant.enjeu
                   , participant.sontour)
            )
                # On récupère l'id généré
            res = curseur.fetchone()
            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return res







    def obtenir_sontour(id_participant):
        """
            Cherche les participants de la base d une partie
            :param Participation: l identifiant d une partie
            :type Participation: integer
            :return: la liste des paricipants
            :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT  sontour"
                "\n\t FROM Participant"
                "\n\t WHERE id_participant = %s;",
                (id_participant,)
            )
            res = curseur.fetchone()
            partie = res["sontour"]
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return partie



    def update5(id_participant, sontour): #c'est un objet de la classe paramètre qui contient les valeurs à rentrer
        """
            Modifie un participant de la base
            :param Participant: la Participation a modifier
            :type Participant: objet de la classe
            :return: si la modification a été faite
            :rtype: bool
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Participant"
                "\n\t SET sontour=%s"
                "\n\t WHERE id_participant=%s RETURNING id_participant;"
                , (sontour, id_participant)
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
