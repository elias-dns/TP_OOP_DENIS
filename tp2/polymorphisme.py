from abc import ABC, abstractmethod

class Habitant(ABC):
    def __init__(self, nom, age, adresse, animaux):
        self._nom = nom
        self.age = age
        self._adresse = adresse
        self._animaux = animaux if animaux is not None else {}

    def get_nom(self):
        return self._nom

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        pass

    def __str__(self):
        return f"{self._nom}, {self.age} ans, habite a {self._adresse}"



class Adulte(Habitant):
    def __init__(self, nom, age, adresse, animaux):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")
        super().__init__(nom, age, adresse, animaux)

    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Deja a la retraite"
        return age_retraite - self.age


class Enfant(Habitant):
    def __init__(self, nom, age, adresse, animaux):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
        super().__init__(nom, age, adresse, animaux)

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: un enfant ne peut pas calculer sa retraite"

def affichage(h: Habitant):
    """Fonction qui affiche un habitant sans se soucier de son type"""
    print(str(h))


adulte = Adulte("Marie Dupont", 35, "Rue A",{})
enfant = Enfant("Lucas Martin", 12, "Rue B",{})
assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

try:
    Enfant("Oups", 25, "Rue C",{})
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

affichage(adulte)
affichage(enfant)