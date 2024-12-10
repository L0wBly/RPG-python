def about():
    print("Vous êtes le héros. Vous vous réveillez sur une île déserte suite a un crash d'avion avec pour seul objet un couteau. Vous devrez gagner battre des monstres en tout genre pour accumuler de l'expérience et récuperer de nouvelles armes pour devenir plus puissant et battre le boss pour vous échappez de l'ile.")

choice = ""
while choice != "4":
    print("\n=====MAIN MENU===== :")
    print("1 - Create New Game")
    print("2 - Load Saved Game")
    print("3 - About")
    print("4 - Exit")
    print("===================")
    choice = input("> ")
    match choice:
        case "1" : create_new_game()        
        case "2" : load_saved_game()        
        case "3" : about()        
        case "4" : print("Goodbye")
        case _: print("Choix Invalide")

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
        self.location = 'start'
        pass

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

""" 
Dévut en c3
a1  a2 a3 a4 a5
----------------
|  |  |  |  |  | a
----------------
|  |  |  |  |  | b
----------------
|  |  |  |  |  | c
----------------
|  |  |  |  |  | d
----------------
|  |  |  |  |  |  e
----------------

"""

ZONENAME = ''
DESCRIPTION = 'description'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_place = {'a1':False, 'a2':False, 'a3':False, 'a4':False, 'a5':False,
                'b1':False, 'b2':False, 'b3':False, 'b4':False, 'b5':False,
                'c1':False, 'c2':False, 'c3':False, 'c4':False, 'c5':False,
                'd1':False, 'd2':False, 'd3':False, 'd4':False, 'd5':False,
                'e1':False, 'e2':False, 'e3':False, 'e4':False, 'e5':False,
                }

zonemap = {
    'a1': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b1',
        'LEFT': "",
        'RIGHT': 'a2',
    },
    'a2': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3',
    },
    'a3': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4',
    },
    'a4': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': 'a5',
    },
    'a5': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b5',
        'LEFT': 'a4',
        'RIGHT': "",
    },
    'b1': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'a1',
        'DOWN': 'c1',
        'LEFT': "",
        'RIGHT': 'b2',
    },
    'b2': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'a2',
        'DOWN': 'c2',
        'LEFT': 'b1',
        'RIGHT': 'b3',
    },
    'b3': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'a3',
        'DOWN': 'c3',
        'LEFT': 'b2',
        'RIGHT': 'b4',
    },
    'b4': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'a4',
        'DOWN': 'c4',
        'LEFT': 'b3',
        'RIGHT': 'b5',
    },
    'b5': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'a5',
        'DOWN': 'c5',
        'LEFT': 'b4',
        'RIGHT': "",
    },
    'c1': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'b1',
        'DOWN': 'd1',
        'LEFT': "",
        'RIGHT': 'c2',
    },
    'c2': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'b2',
        'DOWN': 'd2',
        'LEFT': 'c1',
        'RIGHT': 'c3',
    },
    'c3': {
        'ZONENAME': "Home",
        'DESCRIPTION': 'You are at your home',
        'SOLVED': False,
        'UP': 'b3',
        'DOWN': 'd3',
        'LEFT': 'c2',
        'RIGHT': 'c4',
    },
    'c4': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'b4',
        'DOWN': 'd4',
        'LEFT': 'c3',
        'RIGHT': 'c5',
    },
    'c5': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'b5',
        'DOWN': 'd5',
        'LEFT': 'c4',
        'RIGHT': "",
    },
    'd1': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'c1',
        'DOWN': 'e1',
        'LEFT': "",
        'RIGHT': 'd2',
    },
    'd2': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'c2',
        'DOWN': 'e2',
        'LEFT': 'd1',
        'RIGHT': 'd3',
    },
    'd3': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'c3',
        'DOWN': 'e3',
        'LEFT': 'd2',
        'RIGHT': 'd4',
    },
    'd4': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'c4',
        'DOWN': 'e4',
        'LEFT': 'd3',
        'RIGHT': 'd5',
    },
    'd5': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'c5',
        'DOWN': 'e5',
        'LEFT': 'd4',
        'RIGHT': "",
    },
    'e1': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'd1',
        'DOWN': "",
        'LEFT': "",
        'RIGHT': 'e2',
    },
    'e2': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'd2',
        'DOWN': "",
        'LEFT': 'e1',
        'RIGHT': 'e3',
    },
    'e3': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'd3',
        'DOWN': "",
        'LEFT': 'e2',
        'RIGHT': 'e4',
    },
    'e4': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'd4',
        'DOWN': "",
        'LEFT': 'e3',
        'RIGHT': 'e5',
    },
    'e5': {
        'ZONENAME': "",
        'DESCRIPTION': 'description',
        'SOLVED': False,
        'UP': 'd5',
        'DOWN': "",
        'LEFT': 'e4',
        'RIGHT': "",
    }
}