import random
import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.happiness = 100
        self.health = 100
        self.is_alive = True

    def feed(self):
        if self.is_alive:
            self.hunger -= 10
            self.happiness += 5
            # Limitar las estadísticas a un máximo de 100
            self.hunger = min(self.hunger, 100)
            self.happiness = min(self.happiness, 100)
        self.check_status()

    def play(self):
        if self.is_alive:
            self.happiness += 10
            self.hunger += 5
            # Limitar las estadísticas a un máximo de 100
            self.hunger = min(self.hunger, 100)
            self.happiness = min(self.happiness, 100)
        self.check_status()

    def heal(self):
        if self.is_alive:
            self.health = 100
        self.check_status()

    def check_status(self):
        if self.hunger <= 0 or self.health <= 0:
            print(f"{self.name} ha muerto...")
            self.is_alive = False
        else:
            print(f"{self.name} - Hambre: {self.hunger}, Felicidad: {self.happiness}, Salud: {self.health}")

def main():
    name = input("Dale un nombre a tu Tamagotchi: ")
    tamagotchi = Tamagotchi(name)
    
    while tamagotchi.is_alive:
        action = random.choice(["comer", "jugar", "sanar"])  # Realizar acciones aleatorias
        if action == "comer":
            tamagotchi.feed()
        elif action == "jugar":
            tamagotchi.play()
        elif action == "sanar":
            tamagotchi.heal()
        
        print("Opciones: Comer, Jugar, Sanar, Salir")
        time.sleep(2)  # Pausa de 2 segundos entre cada actualización de estado.

if __name__ == "__main__":
    main()

