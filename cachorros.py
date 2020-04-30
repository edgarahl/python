class Cachorro():

    def __init__(self, color, raza, nombre):
        self.color = color
        self.raza = raza
        self.name = nombre


perrito = Cachorro("Negro", "come_cuando_hay", "pepito")
print("{} es un cachorro de raza: {} y de color {}".format(perrito.name, perrito.raza, perrito.color))


