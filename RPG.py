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