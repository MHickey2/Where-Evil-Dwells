import random

global killer


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
guest5 = Person("5 ", "", "", "", "n/a", "n/a", "innocent", "n/a", "n/a")

'''
def show_information(guest1):
    print( '\nName of Guest: ' + {name} + '\nOccupation of Guest: '
    + {occupation} +'\nAge of Guest: ' + self.age
    + '\nGood Quality: ' + {goodquality} +'\nBad Quality: '
    + {badquality})
    
show_information(guest1)
show_information(guest2)
show_information(guest3)
show_information(guest4)
show_information(guest5)
''' 


def show_guest_details():
    """
    function to show guest details
    """
    print(guest1.index + 'Name: ' + guest1.name + ", Age " + str(guest1.age)
        + ", Occupation: " + guest1.occupation + ", Good Quality: " + guest1.goodquality + ", Bad Quality: " +
        guest1.badquality)
    
    print(guest5.index + guest5.name)


print(guest1.name)

show_guest_details()

# Returns 1 random element from list
names = [guest1.name, guest2.name, guest3.name, guest4.name]
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
    
random_safetyitem()


def survival():
    '''
    does player survive
    '''
    print(guest1.name)
    print(killer)
    
    safetyitem = "Safety Helmet"
    if "Luscious Campbell" == killer and safetyitem == "Safety Helmet":
        print("user survives")
    else:
        print("user dies")


survival()