# classmethod
Créer des classes de base avec les classmethod
Dans cet exercice, on continue dans les fonctions avancées de l'orienté objet avec les classmethod.

Pour spécifier qu'une méthode est une "classemethod", on utilise le décorateur @classmethod.

Cela nous permet de déclarer deux méthodes, "lamborghini" et "porsche", qui vont nous permettre de créer des instances à partir de notre classe Voiture plus facilement.

Une "classmethod" a comme premier paramètre, la classe elle-même, qui par convention est appelé "cls" :

    @classmethod
    def lamborghini(cls):
        pass

À l'intérieur de cette méthode "lamborghini", nous pouvons donc utiliser "cls" pour référer à la class Voiture :

    return cls("Lamborghini", 150000, "rouge")

Dans le cas de la méthode "lamborghini", nous retournons donc une instance créé à partir de la classe "Voiture", dont la marque est "Lamborghini", le prix 150,000 et la couleur "rouge".

On fait de même pour la porsche avec des valeurs différentes pour chaque attribut :

    @classmethod
    def porsche(cls):
        return cls("Porsche", 200000, "noire")

Cela nous permet donc de créer facilement des modèles pour chaque type de voiture, afin de pouvoir facilement créer des voitures de marques célèbres :

    lamborghini = Voiture.lamborghini()
    porsche = Voiture.porsche()
