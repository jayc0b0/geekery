"""
A simple town generator
for any fantasy RPG system.
Originally conceived for D&D,
but may be used for whatever else.
"""

import random

size =[
    "Shanty Town",
    "Couple of Villas",
    "Small Village",
    "Medium Village",
    "Large Village",
    "Small City",
    "Medium City",
    "Large City",
    "Tent City",
    "Underground Village",
    "Ruined Village",
    "Fort",
    "Factory/Mill Town"
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

size = random.choice(size)
feature1 = random.choice(feature)
feature2 = random.choice(feature)
plotHook = random.choice(hook)

def dupeCheck():
    if str(feature1) == str(feature2):
        random.choice(feature)
        dupeCheck()
    else:
        pass

dupeCheck()

print "You come across a %s." % size.upper()
print "It has a %s and a %s." % (feature1, feature2)
print "There are whispers of %s" % plotHook.upper()
