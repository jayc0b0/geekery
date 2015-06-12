# A character generator for D&D 5th Edition
# Still in prototype stages

import random

# Lists
race = [
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

role = [
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

statNamesLong = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma"
]

statNamesAbr = [
    "STR",
    "DEX",
    "CON",
    "INT",
    "WIS",
    "CHA"
]

statValues = ["15", "14", "13", "12", "10", "8"]

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
    random.shuffle(statValues)
    strength = statValues[0]
    dexterity = statValues[1]
    constitution = statValues[2]
    intelligence = statValues[3]
    wisdom = statValues[4]
    charisma = statValues[5]
    print "\nHere are your stats:\n"
    print "STR = %s" % strength
    print "DEX = %s" % dexterity
    print "CON = %s" % constitution
    print "INT = %s" % intelligence
    print "WIS = %s" % wisdom
    print "CHA = %s" % charisma


def choose():
    statCopy = list(statValues)
    for stat, statAbr in zip(statNamesLong, statNamesAbr):
        print "\n"
        print statCopy
        print "%s Stat?" % stat
        stat = raw_input(">> ")
        if stat in statCopy:
            statCopy.remove(stat)
            print "%s = %s" % (statAbr, stat)
        elif stat not in statCopy:
            print "Invalid number."
            choose()
        else:
            print "ERROR IN choose()"

statInit()
