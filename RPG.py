from random import randint
import random
import sys

""" 
Dévut en c3
a1  a2 a3 a4 a5
----------------
|  |  |  |  |  | a
----------------
|  |  |  |  |  | b
----------------
|  |  | c3 |  |  | c
----------------
|  |  |  |  |  | d
----------------
|  |  |  |  |  |  e
----------------

"""
class mob :
    def __init__(self,name,health,level,attack,defense,strenght,loot):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.strenght = strenght
        self.loot = loot

mob1 = mob("Koala",20,1,["coup de patte",60,20,4],2,2,"")
mob2 = mob("Paresseux",30,2,["griffes",80,20,6],2,2,"")
mob3 = mob("Macaque",45,3,["morsure",55,50,12],5,5,"")
mob4 = mob("BOSS ! - Serpent géant",160,5,["crachat de venin",60,70,15],8,8,"")

my_list = [mob1, mob2, mob3]

aléatoire = random.choice(my_list)
instance = aléatoire.name

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
    def __init__(self,name,hit_chance,damage,crit_chance,use_number):
        self.name = name
        self.hit_chance = hit_chance
        self.damage = damage
        self.crit_chance = crit_chance
        self.use_number = use_number

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
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.inventory = [object("potion de soin","health",10),object("bandages","health",5),object("taseur à utilisation unique", "strenght",50)]
        self.attack_list = [attack("coup de couteau",80,15,10,15),attack("saignement",70,25,45,10)]
        self.strength = 15
        self.defense = 15
        self.experience = 0
        self.level = 1
        self.position = 'c3'

    def choose_attack(self):
        for attack in self.attack_list:
            print(attack.name)
        choice = input()
        for attack in self.attack_list:                          # fonction permettant de choisir une attaque dans la liste d'attaques du joueur
            if attack.name == choice:
                print(int(attack.calculate_damage()))
                print((int(aléatoire.health) - int(attack.calculate_damage())))
    
    def open_inventory(self):
        for object in self.inventory:                         # fonction permettant d'afficher l'inventaire
            print(object.name)
            prompt()

    def use_object(self):
        self.open_inventory()
        choice = input()
        for object in self.inventory:                          # fonction permettant d'utiliser un objet qui se situe dans l'inventaire puis le supprime de l'inventaire
            if object.name == choice:
                object.use(self)
                self.inventory.remove(object)
                print(object.name," a été utilisé")
        prompt()

    def death(self):
        print("Vous êtes mort !")                               # fonction qui mets un terme à la partie si on meurt
        print("Merci d'avoir jouer")

    def roll(self):
        print("Vous effectuez une roulade et esquivez l'attaque de " + aléatoire.name)         # fonction pour esquiver une attaque

    def run_away(self):
        print("Vous essayez de fuir")
        percent = randint(1,100)
        if percent > 75:                                         # fonction pour tenter de prendre la fuite
            print("Vous vous êtes enfui")
        else:
            print("Vous n'avez pas réussi a vous enfuir")

    def combat(self):
        print(aléatoire.name + " vous attaque !")
        while player1.health > 0 and aléatoire.health > 0:
            self.combat_interface()
            choice = input("=> ")
            match choice:
                case "1": self.choose_attack()                 # fonction qui gére le combat
                case "2": self.roll()
                case "3": self.use_object()
                case "4": self.run_away()
            print(aléatoire.attack)
            print(int(player1.health) - int(aléatoire.strenght))
        if player1.health <= 0:
            self.death()
        else:
            print("Vous avez vaincu " + aléatoire.name)
            self.player.experience += randint(1,70)
            if self.player.experience >= 50:
                self.player.experience = self.player.experience - 50
                self.player.level += 1
                self.player.health += 10


    def combat_interface(self):
        print(player1.name + " Vie - " + str(player1.health) + " Experience - " + str(player1.experience) + " VS " + aléatoire.name + " Vie - " + str(aléatoire.health))
        print("Que voulez vous faire ?")
        print("1 - Attaques")
        print("2 - Roulade")                                # fonction qui affiche le menu interactif pendant le combat
        print("3 - Inventaire")
        print("4 - Fuir")


################### MAP #####################

ZONENAME = ""
DESCRIPTION = 'description'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: "",
        DOWN: 'b1',
        LEFT: "",
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: "",
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: "",
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: "",
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'a5',
    },
    'a5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: "",
        DOWN: 'b5',
        LEFT: 'a4',
        RIGHT: "",
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'a1',
        DOWN: 'c1',
        LEFT: "",
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: 'dhgrtdsg',
        DESCRIPTION: 'd',
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'b5',
    },
    'b5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'a5',
        DOWN: 'c5',
        LEFT: 'b4',
        RIGHT: "",
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'b1',
        DOWN: 'd1',
        LEFT: "",
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "zaco",
        DESCRIPTION: 'description',
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: 'Home',
        DESCRIPTION: 'You are at your home',
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'c5',
    },
    'c5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'b5',
        DOWN: 'd5',
        LEFT: 'c4',
        RIGHT: "",
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'c1',
        DOWN: 'e1',
        LEFT: "",
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'c2',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'c3',
        DOWN: 'e3',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'c4',
        DOWN: 'e4',
        LEFT: 'd3',
        RIGHT: 'd5',
    },
    'd5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'c5',
        DOWN: 'e5',
        LEFT: 'd4',
        RIGHT: "",
    },
    'e1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'd1',
        DOWN: "",
        LEFT: "",
        RIGHT: 'e2',
    },
    'e2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        UP: 'd2',
        DOWN: '',
        LEFT: 'e1',
        RIGHT: 'e3',
    },
    'e3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'd3',
        DOWN: "",
        LEFT: 'e2',
        RIGHT: 'e4',
    },
    'e4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'd4',
        DOWN: "",
        LEFT: 'e3',
        RIGHT: 'e5',
    },
    'e5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        UP: 'd5',
        DOWN: "",
        LEFT: 'e4',
        RIGHT: "",
    }
}

###############################################

def start_game():
    print(('-' * 50) + '\n')
    print(' ' *7 +"Bienvenu dans notre RPG textuel \n")
    print('-' * 50 + '\n')
    print(' '* 12 + ("    - Play -    ") + ' ' * 5)
    print(' '* 12 + ("    - About -    ") + ' ' * 5)
    print(' '* 12 + ("    - Quit -    ") + ' ' * 5 + '\n')
    print(('-' * 50) + '\n')
    game_select()
	
def game_select():
	answer = input('>>>   ')
	if answer == "play" or answer == "Play" :
		setup()
	elif answer == "About" or answer == "about":
		about()
	elif answer == "Quit" or answer == "quit" :
		sys.exit()

def about():
    print('\n' + '='*19 + "  A propos  " + '='*19 + '\n'+ '\n')
    print('   Pojet réalisé par Cyril Mathé et Arthur Boutry ' + '\n')
    print("Projet RPG python réalisé dans le cadre d'un projet\nd'école HETIC" + '\n')
    print('\n'+ '\n')
    start_game() 

def print_location():
    print('\n' + ('#' * (10 + len(player1.position))))
    print('# ' + (zonemap[player1.position][ZONENAME]) + ' #')
    print('#' * (10 + len(player1.position)))
    print('\n' + (zonemap[player1.position][DESCRIPTION]))
    
def prompt():
    print("\nQue veux-tu faire ?\n")
    print("Vous avez le choix entre :\nAvancer, \nOuvrir l'inventaire, \nCombattre\n")
    action = input(">>>   ")
    acceptable_actions = ['avancer', 'partir', 'quitter', "ouvrir l'inv", 'inventaire', "ouvrir l'inventaire", "combattre"]

    while action.lower() not in acceptable_actions:
        print("Erreur réponse incorrecte\n")
        action = input(">>>   ")

    if action.lower() == 'quitter':
        sys.exit()
    elif action.lower() in ['avancer', 'partir']:
        move(action.lower())
    elif action.lower() in ["ouvrir l'inv", 'inventaire', "ouvrir l'inventaire"]:
        player1.open_inventory()
    elif action.lower() == "combattre":
        player1.combat()

def move(myAction):
	askString = "Où est ce que tu aimerais "+myAction+"?\n> "
	print("Direction possible : " + zonemap[player1.position][UP],zonemap[player1.position][DOWN],zonemap[player1.position][LEFT],zonemap[player1.position][RIGHT] )
	destination = input(askString)
	if destination == zonemap[player1.position][UP]:
		move_dest = zonemap[player1.position][UP]
		move_player(move_dest)
	elif destination == zonemap[player1.position][LEFT]:
		move_dest = zonemap[player1.position][LEFT]
		move_player(move_dest)
	elif destination == zonemap[player1.position][RIGHT]:
		move_dest = zonemap[player1.position][RIGHT]
		move_player(move_dest)
	elif destination == zonemap[player1.position][DOWN]:
		move_dest = zonemap[player1.position][DOWN]
		move_player(move_dest)
	else:
		print("Direction invalide choississez entre up, left, right, down\n")
		move(myAction)

def move_player(move_dest):
	player1.position = move_dest
	print_location()
	
def setup():
	print("\nBienvenu " + player_name + " !!\n\nPour un peu de contexte de vais t'expliquer le but de notre jeu")
	print("\nVous êtes le héros. Vous vous réveillez sur une île déserte suite à un crash d'avion avec pour seul objet un couteau. Vous devrez battre des monstres en tout genre pour accumuler de l'expérience et récuperer de nouvelles armes pour devenir plus puissant et battre le boss pour vous échappez de l'ile. \n")
	prompt()

player_name = input("Quel est votre nom ? ")
player1 = player(player_name)

start_game()
