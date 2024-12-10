from random import randint
import sys
def create_new_game():
    pass

def load_saved_game():
    pass

def about():
    print("Vous êtes le héros. Vous vous réveillez sur une île déserte suite a un crash d'avion avec pour seul objet un couteau. Vous devrez battre des monstres en tout genre pour accumuler de l'expérience et récuperer de nouvelles armes pour devenir plus puissant et battre le boss pour vous échappez de l'ile.")

choice = ""
while choice != "4":
    print("\n=====MENU PRINCIPAL===== :")
    print("1 - Nouvelle Partie")
    print("2 - Charger Partie")
    print("3 - A Propos")                          # Menu interactif
    print("4 - Quitter")
    print("==========================")
    choice = input("=> ")
    match choice:
        case "1" : create_new_game()        
        case "2" : load_saved_game()        
        case "3" : about()        
        case "4" : 
            print("Au revoir")
            sys.exit()
        case _: print("Choix Invalide")

class object :
    def __init__(self,name,power,type):
        self.name = name
        self.power = power
        self.type = type

    def use(self,player):
        if type == "health":
            player.health += self.power
        if type == "defense":
            player.defense += self.power                  # fonction pour utiliser un objet, vérifie le type de l'objet et effectue l'action en fonction du type
        if type == "strenght":
            player.strenght += self.power
class weapon :
    def __init__(self,name,power,attack):
        self.name = name
        self.power = power
        self.attack = attack
    
    def use (self,player):
        player.attack_list.append(self.attack)            # fonction ajoutant une attaque à la liste du personnage

class attack :
    def __init__(self,name,hit_chance,damage,crit_chance,description):
        self.name = name
        self.hit_chance = hit_chance
        self.damage = damage
        self.crit_chance = crit_chance
        self.use_number = 10
        self.description = description

    def calculate_damage(self):
        percent = randint(1,100)
        crit = randint(1,100)
        if percent > self.hit_chance or self.use_number == 0:                   # fonction calculant si une attaque atteint sa cible et si cette attaque est un coup critique puis renvoie les dégâts infligés
            return 0
        else:
            if crit > self.hit_chance:
                return self.damage * 1.5
            else:
                return self.damage
            
    def attack_description(self):
        pass
class player :
    def __init__(self,name,attack_list,experience):
        self.name = name
        self.health = 100
        self.inventory = [object("potion de soin","health",10),object("bandages","health",5),object("taseur à utilisation unique", "strenght",50)]
        self.attack_list = attack_list
        self.strength = 15
        self.defense = 15
        self.experience = 0
        self.level = 1

    def choose_attack(self):
        for attack in self.attack_list:
            print(attack.name)
        choice = input()
        for attack in self.attack_list:                          # fonction permettant de choisir une attaque dans la liste d'attaques du joueur
            if attack.name == choice:
                return attack.calculate_damage()
            else:
                return 0

    def open_inventory(self):
        for object in self.inventory:                         # fonction permettant d'afficher l'inventaire
            print(object.name)

    def use_object(self):
        self.open_inventory()
        choice = input()
        for object in self.inventory:                          # fonction permettant d'utiliser un objet qui se situe dans l'inventaire puis le supprime de l'inventaire
            if object.name == choice:
                object.use(self)
                self.inventory.remove(object)
                print(object.name," a été utilisé")

    def death(self):
        print("Vous êtes mort !")                               # fonction qui mets un terme à la partie si on meurt
        print("Merci d'avoir jouer")

    def roll(self):
        print("Vous effectuez une roulade et esquivez l'attaque de " + mob.name)         # fonction pour esquiver une attaque

    def run_away(self):
        print("Vous essayez de fuir")
        percent = randint(1,100)
        if percent > 75:                                         # fonction pour tenter de prendre la fuite
            print("Vous vous êtes enfui")
        else:
            print("Vous n'avez pas réussi a vous enfuir")

    def combat(self):
        print(mob.name + " vous attaque !")
        while player.health > 0 and mob.health > 0:
            self.combat_interface()
            choice = input("=> ")
            match choice:
                case "1": self.choose_attack()                 # fonction qui gére le combat
                case "2": self.roll()
                case "3": self.use_object()
                case "4": self.run_away()
        if player.health <= 0:
            self.death()
        else:
            print("Vous avez vaincu " + mob.name)
            self.player.experience += randint(1,70)
            if self.player.experience >= 50:
                self.player.experience = self.player.experience - 50
                self.player.level += 1
                self.player.health += 10


    def combat_interface(self):
        print(player.name + " Vie - " + player.health + " Experience - " + player.experience + " VS " + mob.name + " Vie - " + mob.health)
        print("Que voulez vous faire ?")
        print("1 - Attaques")
        print("2 - Roulade")                                # fonction qui affiche le menu interactif pendant le combat
        print("3 - Inventaire")
        print("4 - Fuir")

class mob :
    def __init__(self,name,health,level,attack,defense,strenght,loot):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.strenght = strenght
        self.loot = loot

mob1 = mob("koala",20,1,["coup de patte",60,20,4],2,2)
mob2 = mob("paresseux",30,2,["griffes",80,20,6],2,2)
mob3 = mob("macaque",45,3,["morsure",55,50,12],5,5)
mob4 = mob("BOSS ! - serpent géant",160,5,["crachat de venin",60,70,15],8,8)

class place :
    def __init__(self):
        # name
        # description
        # size
        # coordonate
        # diretion (ou tu peux aller)
        # mob
        # fight
        pass

map = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

x = 0
y = 0

print(map[x+2][y+1])