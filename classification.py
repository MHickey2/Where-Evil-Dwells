"""
Create Class objects for Person and Protection and
functions for random safety item and choosing a
random killer each time the game starts. The
Person class and Protection class has more properties
than are shown to the player, but they are intended
to be the base for future development. This would
add more of RPG style to the existing game format.
"""

import random


class Person(object):
    """
    I have created a new class for Person
    """
    def __init__(self, index, name, occupation, age, good_quality, bad_quality,
                 killermoves, ranking, kryptonite):
        self.index = index
        self.name = name
        self.occupation = occupation
        self.age = age
        self.good_quality = good_quality
        self.bad_quality = bad_quality
        self.killermoves = killermoves
        self.ranking = ranking
        self.kryptonite = kryptonite


# Characters: Guests
guest1 = Person("1", "Luscious Campbell", "Blogger", 29, "Happy", "Selfish",
                "Bludgeoning with Selfie stick", 3, "Safety Helmet")
guest2 = Person("2", "Brad Jameson", "Actor/Model", 32, "Charasmatic", "Vain",
                "uses murder methods from movies", 6, "Book on movie murders")
guest3 = Person("3", "Tobias Cooper", "Reality Show Judge", 42, "Smooth",
                "Rude and Harsh", "Crack Shot", 4, "Bulletproof Vest")
guest4 = Person("4", "Camilla Royce", "Society Lady", 46, "Warm Hearted",
                "Classist", "Poisoner", 2, "Anctidote")
# Killer is chosen at random each time the game starts
guests = [guest1, guest2, guest3, guest4]
names = [guest1.name, guest2.name, guest3.name, guest4.name]
killer = random.choice(names)


class Protection(object):
    """
    I have created a new class for protection items
    """
    def __init__(self, index, name, description, protectionfrom):
        self.index = index
        self.name = name
        self.description = description
        self.protectionfrom = protectionfrom


# Items of protection
item1 = Protection("1 ", "Safety Helmet", "Will stop a selfie Stick",
                   "Luscious Campbell")
item2 = Protection("2 ", "Bulletproof Vest", "Can protect from gunshot",
                   "Tobias Cooper")
item3 = Protection("3 ", "Antidote", "Can protect against poison",
                   "Camilla Royce")
item4 = Protection("4 ", "Gun", "Can be a good defense against guns",
                   "Brad jameson")
item5 = Protection("5 ", "Book on Movie Murders", "Help defend yourself",
                   "Brad Jameson")


def random_item():
    """
    random safety item selection, in case player does not select themselves.
    The player will be allocated an item of protection
    """
    itemlist = [item1.name, item2.name, item3.name, item4.name, item5.name]
    safetyitem = random.choice(itemlist)
    print("Your safetyitem is a" + " " + safetyitem)
    return safetyitem
