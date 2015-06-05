"""
A simple town generator
for any fantasy RPG system.
Originally conceived for D&D,
but may be used for whatever else.
"""

import random

size =[
    "small",
    "medium",
    "large",
    "other"
]

typeSmall =[
    "Shanty Town",
    "Couple of Villas",
    "Small Village",
    "Tent City",
    "Outpost",
]

typeMedium =[
    "Medium Village",
    "Small City",
    "Fort",
    "Factory Town",
    "Mill Town",
]

typeLarge =[
    "Medium City",
    "Large City",
    "Castle and its lands",
    "Large Village",
]

typeOther =[
    "Ruined Village",
    "Underground Village",
]

feature = [
    "TEMPLE",
    "SHADY BAR",
    "RIVER",
    "GRAVEYARD",
    "ARENA",
    "PRISON",
    "BAZAAR",
    "LIBRARY",
    "GUILD",
    "UNIVERSITY",
    "BARRACKS",
    "TOWER",
    "SLUM",
    "WAREHOUSE"
]

hook = [
    "a string of robberies",
    "an army of monsters nearby",
    "a growing cult",
    "a mysterious artifact",
    "something in the sewers",
    "a coup by the local crime syndicate",
    "a kidnapping",
    "a curse on the town",
    "werewolves on the prowl",
    "a legion of vampires",
    "the machinations of a mad scientist",
    "farmers losing their livestock",
    "mysterious lights in the distance"
]

def townPick(size):
    if size == "small":
        return random.choice(typeSmall)
    elif size == "medium":
        return random.choice(typeMedium)
    elif size == "large":
        return random.choice(typeLarge)
    elif size == "other":
        return random.choice(typeOther)
    else:
        return "Error in townPick()"

def featurePrint(size):
    if size == "small":
        print "It has a %s." % feature1.upper()
    elif size == "medium":
        print "It has a %s and a %s." % (feature1.upper(), feature2.upper())
    elif size == "large":
        print "It has a %s, a %s, and a %s." % (feature1.upper(), feature2.upper(), feature3.upper())
    elif size == "other":
        print "It has a %s and a %s." % (feature1.upper(), feature2.upper())
    else:
        return "Error in featurePrint()"

size = random.choice(size)
town = townPick(size)
feature1 = random.choice(feature)
feature2 = random.choice(feature)
feature3 = random.choice(feature)
plotHook = random.choice(hook)

print "You come across a %s." % town.upper()
featurePrint(size)
print "There are whispers of %s." % plotHook.upper()
