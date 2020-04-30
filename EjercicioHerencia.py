class Transporte:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("Voy a {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

class Auto (Transporte):
    def ruedas(self):
        print("Es un transporte con cuatro ruedas")

    def capacidad(self):
        self.capacidad = 5
        return self.capacidad

    def __motor(self):
        pass


class Moto (Transporte):
    def ruedas(self):
        print("Es un transporte de dos ruedas")

    def capacidad(self):
        self.capacidad = 2
        return self.capacidad

vehiculo = Moto()
vehiculo.ruedas()
personas=vehiculo.capacidad()
print("la capacidad de este transporte es de {} personas".format(personas))

while True:
    action = input("Que desea hacer? [A]celerare, [B]requear, "
                   "mostrar [V]elocimetro, [S]alir ? ").upper()
    if action not in "ABVS" or len(action) != 1:
        print("No entendi!...")
        continue
    if action == 'A':
        vehiculo.accelerate()
    elif action == 'B':
        vehiculo.brake()
    elif action == 'V':
        print("voy a  {} kilometers".format(vehiculo.odometer))
    elif action == 'S':
        break
    vehiculo.step()
    vehiculo.say_state()
