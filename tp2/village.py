from habitant import Habitant

class Village:

    """creation classe village"""

    def __init__(self,nom):
        """constructeur de la classe village"""
        self.nom = nom
        self.habitants = []

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        """créer un nouvel habitant et l'ajoute à la liste, le village est propriétaire de l'habitant"""
        nouvel_habitant = Habitant(nom,age,adresse,animaux)
        self.habitants.append(nouvel_habitant)

    def ajouter_habitant_agregation(self, habitant):
        """ajout un nouvel habitant qui existe déjà, le village utilise l'habitant mais n'en est pas propriétaire"""
        self.habitants.append(habitant)

    def afficher_habitants(self):
        """affiche chaque habitant du village"""
        for habitant in self.habitants:
            # On utilise les accesseurs car les attributs sont privés
            print(f"{habitant.get_nom()}, {habitant.age} ans")
    
    def get_habitants(self):
        """Renvoie la liste des habitants"""
        return self.habitants


pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})

elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)

autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()

#la fonction ajouter_habitant_composition represente une relation de composition car 
# notre objet (la liste habitant) ne peut pas exister sans son conteneur (le village), car on l'a créer alors 
#que pour l'agregation la liste peut exiter toute seule