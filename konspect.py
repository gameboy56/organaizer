# ------------------------- TASK 1 -------------------------


class NPC:
    def __init__(self, name, good):
        self.name = name
        self.good = good

class Merchant(NPC):
    pass


# ------------------------- TASK 2 -------------------------


class Pokemon:
    def __init__(self, name, poke_type, hp, attack):
        self.name = name
        self.poke_type = poke_type
        self.hp = hp
        self.attack = attack

    def show(self):
        print(f"{self.name} ({self.poke_type}) — HP: {self.hp}, Атака: {self.attack}")

class FirePokemon(Pokemon):
    def apply_bonus(self):
        self.attack += 10

class WaterPokemon(Pokemon):
    def apply_bonus(self):
        self.hp += 15

class ElectricPokemon(Pokemon):
    def attack_action(self):
        print(f"⚡ {self.name} выпускает заряд молнии! Сила атаки: {self.attack}")


# ------------------------- TASK 3 -------------------------


class Block:
    def __init__(self):
        self.name = None
        self.hardness = 0
        self.breakable = False

    def show_info(self):
        print(f"Блок: {self.name}")
        print(f"Прочность: {self.hardness}")
        print(f"Можно сломать: {self.breakable}")
        print()

class Stone(Block):
    def set_properties(self):
        self.name = "Stone"
        self.hardness = 10
        self.breakable = True

class Bedrock(Block):
    def set_properties(self):
        self.name = "Bedrock"
        self.hardness = 999
        self.breakable = False

class GrassBlock(Block):
    def set_properties(self):
        self.name = "GrassBlock"
        self.hardness = 1
        self.breakable = True

