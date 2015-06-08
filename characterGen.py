# A character generator for D&D 5th Edition
# Still in prototype stages

import random

# Lists
race =[
    "Aasimar",
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Half-Orc",
    "Halfling",
    "Human",
    "Tiefling"
]

role =[
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

stats =["15", "14", "13", "12", "10", "8"]

# Variables
name = raw_input("Character Name?\n>> ")
race = random.choice(race)
role = random.choice(role)

# Basic Info
print "\nYour name is %s." % name
print "You are a %s %s" % (race, role)

# Stats
def statInit():
    print "\n1) Auto-allocate\nor\n2) Choose Stats?"
    choice = raw_input(">> ")
    if str(choice) == "1":
        allocate()
    elif str(choice) == "2":
        choose()
    else:
        print "Invalid choice. Please choose '1' or '2'."

def allocate():
    random.shuffle(stats)
    strength = stats[0]
    dexterity = stats[1]
    constitution = stats[2]
    intelligence = stats[3]
    wisdom = stats[4]
    charisma = stats[5]
    print "\nHere are your stats:\n"
    print "STR = %s" % strength
    print "DEX = %s" % dexterity
    print "CON = %s" % constitution
    print "INT = %s" % intelligence
    print "WIS = %s" % wisdom
    print "CHA = %s" % charisma

def choose():
    print "Null"

statInit()
