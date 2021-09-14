from serveur.metier.borne_50 import Borne50
import unittest

class test50B(unittest.TestCase):

    def setUp(self):
        self.statut = [3, 75, 1, 1, 1, 1, 1, 0, 0, 0, 0]
        self.joueur = 3
    def test_peut_on_jouer_50B(self):

        statPostJeu = Borne50.peut_on_jouer_50B(self.statut,self.joueur)
        self.assertEqual(statPostJeu ,1)
        
    def test_jouer_50B(self):
        statPostJeu = Borne50.jouer_50B(self.statut)
        self.assertEqual(statPostJeu ,[3, 125, 1, 1, 1, 1, 1, 0, 0, 0, 0])
        
unittest.main()