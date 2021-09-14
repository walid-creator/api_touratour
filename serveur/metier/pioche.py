import random

class Pioche:


    """
    Cette classe a pour attributs une pioche prenant la forme d'un paquet de carte (de 0 à 106 cartes) mises sous le format d'un mot.
    Par exemple une pioche de fin de partie dans laquelle il resterait les trois cartes B025, @FEU et !LIM dans cet ordre d'apparition aura pour        attribut paquet "BO25@FEU!LIM".
    Le second attribu correspond simplement à l'identifiant de la partie (un entier) à laquelle la pioche est rattachée. Il y a bijection entre l'ensemble des id_parties et l'ensemble des pioches.

    Cette classe contient deux méthodes : une pour mélanger le paquet et une qui renvoie la dernière carte du paquet.


    """

    def __init__(self, pioche, id_partie):
        self.pioche = pioche
        self.id_partie = id_partie


    def melanger(self):
        """
        Fonction qui mélange les cartes du paquet et les retourne dans une liste de même taille.
        :param pioche: mot à mélanger
        :type pioche: str
        :return: mot mélangé
        :type pioche: str
        """
        L = []

        for i in range(int(len(self.pioche)/4)):  #i va de 0 à 109
            L += [self.pioche[4*i : 4*i+4]]

        random.shuffle(L)
        random.shuffle(L)
        random.shuffle(L)

        paquetmelange = ""
        for i in range(len(L)):
            paquetmelange += L[i]

        return paquetmelange



    def retourner_derniere_carte(self):
        """
        Fonction qui retourne la dernière carte de la pioche pour pouvoir la jouer
        :param pioche: mot des cartes dans la pioche
        :type pioche: str
        :return : retourne la dernière carte du paquet 
        :return type : str
        """
        m = self.pioche[0:4]
        return m

    