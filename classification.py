import random

global killer 
global safetyitem


class Person(object):
    """
    This is a docstring. I have created a new class for Person
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
guest1 = Person("1 ", "Luscious Campbell", "Blogger", 29, "Happy", "Selfish",
                "Bludgeoning with Selfie stick", 3, "Safety Helmet")
guest2 = Person("2 ", "Brad Jameson", "Actor/Model", 32, "Charasmatic", "Vain",
                "uses murder methods from movies", 6, "Book on movie murders")
guest3 = Person("3 ", "Tobias Cooper", "Reality Show Judge", 42, "Smooth",
                "Rude and Harsh", "Crack Shot", 4, "Bulletproof Vest")
guest4 = Person("4 ", "Camilla Royce", "Society Lady", 46, "Warm Hearted",
                "Classist", "Poisoner", 2, "Anctidote")

x = [guest1, guest2, guest3, guest4]


class Player(object):
    """
    This is a docstring. I have created a new class for Game Player
    """
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age



def show_guest_details():
    """
    function to show guest details
    """
    print(guest1.index + 'Name: ' + guest1.name + ", Age " + str(guest1.age)
          + ", Occupation: " + guest1.occupation + ", Good Quality: " +
          guest1.good_quality + ", Bad Quality: " + guest1.bad_quality)

    print(guest1.index + guest1.name)


print(guest1.name)

show_guest_details()

# Returns 1 random element from list
names = [guest1.name, guest2.name, guest3.name, guest4.name]
killer = random.choice(names)
print(killer)


class Protection(object):
    """
    I have created a new class for protection items
    """
    def __init__(self, index, name, description, protectionfrom):
        self.index = index
        self.name = name
        self.description = description
        self.protectionfrom = protectionfrom


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
    def random_safetyitem_and_survival():
    """
    global safetyitem
    itemlist = [item1.name, item2.name, item3.name, item4.name, item5.name]
    safetyitem = random.choice(itemlist)
    print(safetyitem)
    return safetyitem


random_item()



"""
def survival():
    """
    # user can be assigned random protection item
"""
    # Returns 1 random element from list
    global killer
    global safetyitem      

    if "Luscious Campbell" == killer and "Safety Helmet" == safetyitem:
        print("User lives")
    elif "Brad Jameson" == killer and "Book on Movie Murders" == safetyitem:
        print("User lives")
    elif "Tobias Cooper" == killer and "Bulletproof Vest" == safetyitem:
        print("User lives")
    elif "Camilla Royce" == killer and "Antidote" == safetyitem:
        print("User lives")
    else:
        print("user dies")


survival()

"""