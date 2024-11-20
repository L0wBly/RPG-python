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