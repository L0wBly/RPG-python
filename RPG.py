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
ZONENAME = ""
DESCRIPTION = 'description'
SOLVED = False
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

solved_place = {'a1':False, 'a2':False, 'a3':False, 'a4':False, 'a5':False,
                'b1':False, 'b2':False, 'b3':False, 'b4':False, 'b5':False,
                'c1':False, 'c2':False, 'c3':False, 'c4':False, 'c5':False,
                'd1':False, 'd2':False, 'd3':False, 'd4':False, 'd5':False,
                'e1':False, 'e2':False, 'e3':False, 'e4':False, 'e5':False,
                }

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: "",
        DOWN: 'b1',
        LEFT: "",
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: "",
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: "",
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: "",
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'a5',
    },
    'a5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: "",
        DOWN: 'b5',
        LEFT: 'a4',
        RIGHT: "",
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: "",
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "dhgrtdsg",
        DESCRIPTION: 'd',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'b5',
    },
    'b5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'a5',
        DOWN: 'c5',
        LEFT: 'b4',
        RIGHT: "",
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: "",
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: "Home",
        DESCRIPTION: 'You are at your home',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'c5',
    },
    'c5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'b5',
        DOWN: 'd5',
        LEFT: 'c4',
        RIGHT: "",
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'e1',
        LEFT: "",
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'c2',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'e3',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'c4',
        DOWN: 'e4',
        LEFT: 'd3',
        RIGHT: 'd5',
    },
    'd5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'c5',
        DOWN: 'e5',
        LEFT: 'd4',
        RIGHT: "",
    },
    'e1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'd1',
        DOWN: "",
        LEFT: "",
        RIGHT: 'e2',
    },
    'e2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'd2',
        DOWN: "",
        LEFT: 'e1',
        RIGHT: 'e3',
    },
    'e3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'd3',
        DOWN: "",
        LEFT: 'e2',
        RIGHT: 'e4',
    },
    'e4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'd4',
        DOWN: "",
        LEFT: 'e3',
        RIGHT: 'e5',
    },
    'e5': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: 'd5',
        DOWN: "",
        LEFT: 'e4',
        RIGHT: "",
    }
}

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


class player:
    def __init__(self):
        # name
        # hp
        # inventory
        # attack
        # strength
        # defense
        # experience
        # level
        self.position = 'c3'
player1 = player()


class mob :
    def __init__(self):
        # name 
        # hp
        # level
        # attack
        # defense
        # force
        # loot
        pass

class attack :
    def __init__(self):
        # name
        # hit_chance
        # damage
        # critical
        # use_nb
        # description
        pass

################ MAP ##############


def print_location():
	print('\n' + ('#' * (10 +len(player1.position))))
	print('# ' + (zonemap[player1.position][ZONENAME]) + ' #')
	print('#' * (10 +len(player1.position)))
	print('\n' + (zonemap[player1.position][DESCRIPTION]))
	prompt()

def prompt():
	print("\nQue veux tu faire ?\n")
	print("Vous avez le choix entre :\nAvancer, \nOuvrir l'inventaire\n")
	action = input(">>>   ")
	acceptable_actions = ['avancer',"ouvir l'inventaire","quitter"]
	while action.lower() not in acceptable_actions:
		print("Erreur réponse incorrecte\n")
		prompt()
	if action.lower() == 'quitter':
		sys.exit()
	elif action.lower() in ['avancer', 'partir']:
		move(action.lower())
	elif action.lower() in ["ouvrir l'inv", 'inventaire', "ouvrir l'inventaire"]:
		'''fonction inventaire'''

def move(myAction):
	askString = "Où est ce que tu aimerais "+myAction+"?\n> "
	print("Direction possible : up, left, right, down\n")
	destination = input(askString)
	if destination == 'up':
		move_dest = zonemap[player1.position][UP]
		move_player(move_dest)
	elif destination == 'left':
		move_dest = zonemap[player1.position][LEFT]
		move_player(move_dest)
	elif destination == 'right':
		move_dest = zonemap[player1.position][RIGHT]
		move_player(move_dest)
	elif destination == 'down':
		move_dest = zonemap[player1.position][DOWN]
		move_player(move_dest)
	else:
		print("Direction invalide choississez entre up, left, right, down\n")
		move(myAction)

def move_player(move_dest):
	print("\nTu as avancé en :" + move_dest + ".")
	player1.position = move_dest
	print_location()
	
def setup():
	print("\nBienvenu !!\n\nPour un peu de contexte de vais t'expliquer le but de notre jeu")
	print("\nVous êtes le héros. Vous vous réveillez sur une île déserte suite à un crash d'avion avec pour seul objet un couteau. Vous devrez battre des monstres en tout genre pour accumuler de l'expérience et récuperer de nouvelles armes pour devenir plus puissant et battre le boss pour vous échappez de l'ile. \n")
	prompt()
	
start_game()