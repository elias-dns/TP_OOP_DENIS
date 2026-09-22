class Habitant:
    """classe d'un habitant du village avec des attributs privés"""

    def __init__(self, nom: str, age: int, adresse: str, animaux: dict = None):
        """Constructeur de la classe Habitant"""
        self.__nom = nom
        self.age = age  #on utilise property pour valider l'age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        """Modifie l'âge avec vérification"""
        if valeur < 0 or valeur > 130:
            raise ValueError("L'âge doit être compris entre 0 et 130")
        self.__age = valeur

    def get_nom(self):
        return self.__nom

    def get_adresse(self):
        return self.__adresse

    def get_animaux(self):
        return self.__animaux
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_adresse(self, adresse):
        self.__adresse = adresse
    
    def set_animaux(self, animaux):
        self.__animaux = animaux

    def affichage_adresse(self):
        print(f"{self.__nom} habite à {self._adresse}")

    def compte_animal(self, animal):
        return self.__animaux.get(animal, 0)


h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass