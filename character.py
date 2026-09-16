class Character:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy
        self.level = 1
        self.gold = 100

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0

        print(f"{self.name} took {amount} damage.")

    def heal(self, amount):
        self.health += amount

        if self.health > 100:
            self.health = 100

        print(f"{self.name} healed for {amount} health.")

    def use_energy(self, amount):
        if amount <= self.energy:
            self.energy -= amount
            print(f"{self.name} used {amount} energy.")
        else:
            print(f"{self.name} does not have enough energy.")

    def level_up(self):
        self.level += 1
        self.health = 100
        self.energy = 100

        print(f"{self.name} reached level {self.level}!")

    def show_status(self):
        print("\n--- Character Status ---")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        print(f"Level: {self.level}")
        print(f"Gold: {self.gold}")
        print("------------------------")

    def rest(self):
        self.energy = 100
        print(f"{self.name} rested and restored their energy.")
        self.show_status()