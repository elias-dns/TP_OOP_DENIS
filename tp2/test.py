import unittest

from habitant import Habitant
from heritage import Habitant, Adulte, Enfant

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation"""

    def test_age_setter_valide(self):
        """cas age valide"""
        h = Habitant("Marie Dupont", 35, "Rue A", {})
        h.age = 36
        self.assertEqual(h.age, 36)

    def test_age_setter_invalide(self):
        """Cas limite age negatif"""
        h = Habitant("Marie Dupont", 35, "Rue A", {})
        with self.assertRaises(ValueError):
            h.age = -5

    def test_compte_animal_limite(self):
        """Cas limite l'animal n'est pas possédé"""
        h = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(h.compte_animal("moutons"), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)

class TestHeritage(unittest.TestCase):
    """Tests pour héritage"""

    def test_retraite_adulte(self):
        """Vérifie la retraite pour un adulte"""
        adulte = Adulte("Marie", 35, "Rue A", {})
        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(), 27)

