import random
from colorama import Fore, Style


# Character object
class Fighter:
    def __init__(self, name, pv, heal, min_strength, max_strength, alive=True):
        self.name = name
        self.pv = pv
        self.heal = heal
        self.min_strength = min_strength
        self.max_strength = max_strength
        self.alive = alive

    def attack(self, adversary):
        atk = random.randint(self.min_strength, self.max_strength)
        adversary.pv -= atk
        print(Fore.GREEN + f"{self.name} attack, {adversary.name} lose {atk} pv")

    def ripost(self, adversary):
        reply = random.randint(adversary.min_strength, adversary.max_strength)
        adversary.pv -= reply
        print(Fore.RED + f"{self.name} ripost, {adversary.name} lose {reply} pv")

    def status(self, adversary):
        print(Fore.BLUE + f"{self.name} : {self.pv} pv, {adversary.name} : {adversary.pv} pv")

    def healer(self):
        potion = random.randint(15, 50)
        self.heal -= 1
        self.pv += potion
        print(Fore.CYAN + f"you are healed of {potion} pv")


# action
def fight():
    
    fighter_a_name = input("Name of first fighter : ")
    fighter_b_name = input("Name of seconde fighter : ")
    
    pv = 50
    potion = 3

    fighter_a = Fighter(fighter_a_name, pv, potion, 5, 10)
    fighter_b = Fighter(fighter_b_name, pv, 0, 5, 15)
   
    while fighter_a.alive or fighter_b.alive:
        decision = input(Style.BRIGHT + Fore.CYAN + "Choose fight for 1 or heal for 2 : ")
        try:
            decision_nb = int(decision)
        except:
            print(Style.BRIGHT + Fore.RED + "You need to choose!!")
        else:
            print(Style.RESET_ALL)
            if decision_nb == 1:
                fighter_a.attack(fighter_b)
                fighter_b.ripost(fighter_a)
                fighter_a.status(fighter_b)
            elif decision_nb == 2:
                fighter_a.healer()
                fighter_b.attack(fighter_a)
                fighter_a.status(fighter_b)
            print(Style.RESET_ALL)

        if fighter_b.pv <= 0 and fighter_a.pv <= 0:
            fighter_a.alive = False
            fighter_b.alive = False
            print("Both fighters are K.O. !!")
            break
        elif fighter_a.pv <= 0:
            fighter_a.alive = False
            print(f"{fighter_b.name} Win!")
            break
        elif fighter_b.pv <= 0:
            fighter_b.alive = False
            print(f"{fighter_a.name} Win!")
            break
        

fight()
