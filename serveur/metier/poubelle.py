

class Poubelle:

    def __init__(self, paquet, id_partie):
        self.paquet = paquet
        self.id_partie = id_partie
    
    def retourner_derniere_carte(self):
        """
        Fonction qui retourne la dernièree carte de la poubelle pour pouvoir la jouer
        :param poubelle: liste des cartes dans la poubelle
        :type poubelle: list
        """
        m = self.paquet[-1]
        return m