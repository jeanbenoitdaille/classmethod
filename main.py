    class Voiture(object):
        def __init__(self, marque, prix, couleur):
    	self.marque = marque
    	self.prix = prix
    	self.couleur = couleur
     
        @classmethod
        def lamborghini(cls):
    	return cls("Lamborghini", 150000, "rouge")
     
        @classmethod
        def porsche(cls):
    	return cls("Porsche", 200000, "noire")
     
    lamborghini = Voiture.lamborghini()
    print(lamborghini.prix)
    porsche = Voiture.porsche()
    print(porsche.prix)
