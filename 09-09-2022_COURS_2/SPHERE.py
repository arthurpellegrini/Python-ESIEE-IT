import math


class Sphere:
    """
    Cette classe permet la création d'un objet qui est une sphère.
    """
    def __init__(self, rayon: float):
        """
        Constructeur de la classe Sphere.
        :param rayon: La longueur du rayon.
        """
        self.rayon = rayon
        self.surface = 4 * math.pi * self.rayon ** 2
        self.volume = (4 / 3) * math.pi * self.rayon ** 3
        self.perimetre = math.pi * self.rayon**2
        self.arrete_inscrit = (2 * self.rayon)/math.sqrt(3)
        self.volume_inscrit = (self.arrete_inscrit**3)

    def __str__(self):
        return "Le rayon est de %0.2f \nLa surface est de %0.2f \nLe volume est de %0.2f \n" \
               "Le périmètre est de %0.2f \n Le rayon du cube inscrit est de %0.2f \n" \
               "Le volume du cube inscrit est de %0.2f" \
               % (self.rayon, self.surface, self.volume, self.perimetre, self.arrete_inscrit, self.volume_inscrit)


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    sphere = Sphere(2.5)
    print(sphere)
