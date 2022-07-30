import random


class Person(object):
    '''
    This is a docstring. I have created a new class for Person
    '''
    def __init__(self, index, name, occupation, age, goodquality, badquality,
                 killermoves, ranking, kryptonite):
        self.index = index
        self.name = name
        self.occupation = occupation
        self.age = age
        self.goodquality = goodquality
        self.badquality = badquality
        self.killeroves = killermoves
        self.ranking = ranking
        self.kryptonite = kryptonite


# Characters: Guests
guest1 = Person("1 ", "Luscious Campbell", "Blogger", 29, "Happy", "Selfish",
                "Bludgeoning with Selfie stick", 3, "Safety Helmet")
guest2 = Person("2 ", "Brad Jameson", "Actor/Model", 32, "Charasmatic", "Vain",
                "uses murder methods from movies", 6, "Book on movie murders")
guest3 = Person("3 ", "Tobias Cooper", "Reality Show Judge", 42, "Smooth",
                "Rude and Harsh", "Crack Shot", 4, "Bulletproof Vest")
guest4 = Person("4 ", "Camilla Royce", "Society Lady", 46, "Warm Hearted",
                "Classist", "Poisoner", 2, "Anctidote")
guest5 = Person("5 ", "", "", "", "n/a", "n/a", "innocent", "n/a", "n/a")


def show_guest_details(object):
    """
    function to show guest details
    """
    print(guest1.index + guest1.name)
    print(guest2.index + guest2.name)
    print(guest3.index + guest3.name)
    print(guest4.index + guest4.name)
    print(guest5.index + guest5.name)


show_guest_details(object)

# Returns 1 random element from list
names = ["Luscious", "Brad", "Tobias", "Camilla"]
killer = random.choice(names)
print(killer)


class Protection(object):
    '''
    I have created a new class for protection items
    '''
    def __init__(self, index, name, description, protectionfrom):
        self.index = index
        self.name = name
        self.description = description
        self.protectionfrom = protectionfrom


item1 = Protection("1 ", "Safety Helmet", "Will stop a selfie Stick",
                   "Luscious Campbell")
item2 = Protection("2 ", "Bullet Proof vest", "Can protect from gunshot",
                   "Tobias Cooper")
item3 = Protection("3 ", "antidote", "Can protect against poison",
                   "Camilla Royce")
item4 = Protection("4 ", "Gun", "Can be a good defense against guns",
                   "Brad jameson")
item5 = Protection("5 ", "Book on Movie Murders", "Help defend yourself",
                   "Brad Jameson")


def random_safetyitem():
    '''
    user can be assigned random protection item
    '''
    itemlist = [item1.name, item2.name, item3.name, item4.name, item5.name]
    safetyitem = random.choice(itemlist)
    print(safetyitem)