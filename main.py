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
        print()

    def ripost(self, adversary):
        print(f"{adversary.name} attack in turn")
        reply = random.randint(adversary.min_strength, adversary.max_strength)
        self.pv -= reply
        print(f"{self.name} ripost, {adversary.name} lose {reply} pv")
        print()
        
    def status(self, adversary):
        print(f"{self.name} : {self.pv} pv, {adversary.name} : {adversary.pv} pv")

    def healer(self):
        potion = random.randint(15, 50)
        self.heal -= 1
        self.pv += potion
        print(f"you are healed of {potion} pv")


# action
def fight():
    fighter_a_name = input("Name of first fighter : ")
    fighter_b_name = input("Name of seconde fighter : ")
    pv = 50
    potion = 3

    fighter_a = Fighter(fighter_a_name, pv, potion, 5, 10)
    fighter_b = Fighter(fighter_b_name, pv, potion, 0, 15)
    try:
        while not fighter_a.pv <= 0 or fighter_b.pv <= 0:
            if 30 < fighter_a.pv:
                fighter_a.attack(fighter_b)
                fighter_b.ripost(fighter_a)
                fighter_a.status(fighter_b)
            if 0 < fighter_a.pv <= 30:
                decision = int(input("choose fight for 1 or heal for 2 :"))
                if decision == 1:
                    fighter_a.attack(fighter_b)
                    fighter_b.ripost(fighter_a)
                    fighter_a.status(fighter_b)
                elif decision == 2:
                    fighter_a.healer()
                    fighter_b.attack(fighter_a)
                    fighter_a.status(fighter_b)
        
        if fighter_a.pv <= 0:
            print(f"{fighter_b.name} Win!")

        if fighter_b.pv <= 0:
            print(f"{fighter_a.name} Win!")
        
    except IOError as e:
        print(e)


fight()
