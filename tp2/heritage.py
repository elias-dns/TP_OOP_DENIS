from abc import ABC, abstractmethod

class Habitant(ABC):
    def __init__(self, nom, age, adresse, animaux):
        self._nom = nom
        self.age = age
        self._adresse = adresse
        self._animaux = animaux if animaux is not None else {}

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """Méthode abstraite pour calculer la retraite"""
        pass


# Adulte : leve une ValueError si age < 18
# calcul_nombre_annee_avant_retraite() renvoie :
# - "Deja a la retraite" si age >= 62
# - 62 - age sinon

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
    

# Enfant : leve une ValueError si age >= 18
# calcul_nombre_annee_avant_retraite() renvoie toujours :
# - "Erreur: un enfant ne peut pas calculer sa retraite"

class Enfant(Habitant):
    def __init__(self, nom, age, adresse, animaux):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
        super().__init__(nom, age, adresse, animaux)

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: un enfant ne peut pas calculer sa retraite"
    


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