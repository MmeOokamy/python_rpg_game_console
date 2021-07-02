import random

# Character object
class Fighter:
    def __init__(self, name, pv, heal, min_strength, max_strength):
        self.name = name
        self.pv = pv
        self.heal = heal
        self.min_strength = min_strength
        self.max_strength = max_strength


    def attack(self, adversary):
        atk = random.randint(self.min_strength, self.max_strength)
        adversary.pv -= atk
        print(f"{self.name} attack, {adversary.name} lose {atk} pv")
        print(f"{self.name} : {self.pv} pv, {adversary.name} : {adversary.pv} pv")

    def healer(self):
        potion = random.randint(15, 50)
        self.heal -= 1
        self.pv += potion
        print(f"you are healed of {potion} pv")

def choice(nb, fighterA, fighterB):
    if nb == 1:
        fighterA.attack(fighterB)
        fighterB.attack(fighterA)

    if nb == 2:
        fighterA.healer(fighterA)
        fighterB.attack(fighterA)


# action
def fight():
    fighterA_name = input("Name of first fighter : ")
    fighterB_name = input("Name of seconde fighter : ")
    pv = 50
    potion = 3

    fighterA = Fighter(fighterA_name, pv,potion, 5, 10)
    fighterB = Fighter(fighterB_name, pv,potion, 0, 15)

    while not fighterA.pv <= 0 or fighterB.pv <= 0:
        if 30 < fighterA.pv <= 50:
            choice(1,fighterA,fighterB)

        if fighterA.pv >= 30:
            nb = input(f"{fighterA.name} Attack(1) or  Heal(2) : " )
            choice(nb,fighterA,fighterB)
        

    if fighterA.pv <= 0:
        print(f"{fighterB.name} Win!")

    if fighterB.pv <= 0:
        print(f"{fighterA.name} Win!")


fight()
