""" 
Créez une classe "Animal" avec des attributs tels que le nom et la nourriture préférée.
 Créez une classe "Zoo" qui contient une liste d'animaux et des méthodes pour les nourrir et
 afficher leurs informations
"""

class Animal:
    def __init__(self, nom, nourriture_preferee):
        self.nom = nom
        self.nourriture_preferee = nourriture_preferee

    def nourrir(self, nourriture):
        if nourriture == self.nourriture_preferee:
            print(f"{self.nom} est ravi de manger sa nourriture préférée : {nourriture} !")
        else:
            print(f"{self.nom} mange de la {nourriture}, mais aurait préféré de la {self.nourriture_preferee}...")

    def afficher_infos(self):
        print(f"{self.nom} aime manger de la {self.nourriture_preferee}.")

class Zoo:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def nourrir_animaux(self, nourriture):
        for animal in self.animaux:
            animal.nourrir(nourriture)

    def afficher_infos_animaux(self):
        for animal in self.animaux:
            animal.afficher_infos()

# Création des animaux
lion = Animal("Simba", "viande")
girafe = Animal("Girafon", "feuilles")
pingouin = Animal("Pingou", "poisson")

# Création du zoo et ajout des animaux
zoo = Zoo()
zoo.ajouter_animal(lion)
zoo.ajouter_animal(girafe)
zoo.ajouter_animal(pingouin)

# Nourrissage des animaux
zoo.nourrir_animaux("viande")
zoo.nourrir_animaux("feuilles")
zoo.nourrir_animaux("poisson")

# Affichage des informations des animaux
zoo.afficher_infos_animaux()
