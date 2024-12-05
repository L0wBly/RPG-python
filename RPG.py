def create_new_game():
    pass

def load_saved_game():
    pass

def about():
    print("Vous êtes le héros. Vous vous réveillez sur une île déserte suite a un crash d'avion avec pour seul objet un couteau. Vous devrez gagner battre des monstres en tout genre pour accumuler de l'expérience et récuperer de nouvelles armes pour devenir plus puissant et battre le boss pour vous échappez de l'ile.")

choice = ""
while choice != "4":
    print("\n=====MAIN MENU===== :")
    print("1 - Create New Game")
    print("2 - Load Saved Game")
    print("3 - About")                          # Menu interactif
    print("4 - Exit")
    print("===================")
    choice = input("> ")
    match choice:
        case "1" : create_new_game()        
        case "2" : load_saved_game()        
        case "3" : about()        
        case "4" : print("Goodbye")
        case _: print("Choix Invalide")

class object :
    def __init__(self,name,power,type):
        self.name = name
        self.power = power
        self.type = type

    def use(self,hero):
        if type == "health":
            hero.health += self.power
        if type == "defense":
            hero.defense += self.power                  # fonction pour utiliser un objet, vérifie le type de l'objet et effectue l'action en fonction du type
        if type == "strenght":
            hero.strenght += self.power
class weapon :
    def __init__(self,name,power,attack):
        self.name = name
        self.power = power
        self.attack = attack
    
    def use (self,hero):
        hero.attack_list.append(self.attack)            # fonction ajoutant une attaque à la liste du personnage

class attack :
    def __init__(self,name,hit_chance,damage,crit_chance,description):
        self.name = name
        self.hit_chance = hit_chance
        self.damage = damage
        self.crit_chance = crit_chance
        self.use_number = 10
        self.description = description

    def calculate_damage(self):
        from random import randint
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
        self.experience = experience
        self.level = 1

    def choose_attack(self):
        for attack in self.attack_list:
            print(attack.name)
        choice = input()
        for attack in self.attack_list:                          # fonction permettant de choisir une attaque dans la liste du joueur
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

    def level(self):
        pass

    def death(self):
        if self.hp == 0:                                      # fonction qui mets un terme à la partie si on meurt
            print("Vous êtes mort !")
            print("Merci d'avoir jouer")

class mob :
    def __init__(self,name,health,level,attack,defense,strenght,loot):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.strenght = strenght
        self.loot = loot

mob1 = mob("renard",20,1,["morsure",60,20,4],2,2)
mob2 = mob("macaque",45,3,["morsure",55,50,12],5,5)

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