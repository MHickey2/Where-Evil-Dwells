'''
This is a docstring. I have created a new class for Person
'''
class Person(object):
    def __init__(self, index, name, occupation, age, goodQuality, badQuality,
                 killerMoves, ranking, kryptonite):
        self.index = index
        self.name = name
        self.occupation = occupation
        self.age = age
        self.goodQuality = goodQuality
        self.badQuality = badQuality
        self.killerMoves = killerMoves
        self.ranking = ranking
        self.kryptonite = kryptonite
'''
Characters: Guests
'''        
guest1 = Person("1 ", "Luscious Campbell", "Blogger", 29, "Happy", "Selfish",
                "Bludgeoning with Selfie stick", 3, "Safety Helmet")
guest2 = Person("2 ", "Brad Jameson", "Actor/Model", 32, "Charasmatic", "Vain",
                "uses murder methods from movies", 6, "Book on movie murders")
guest3 = Person("3 ", "Tobias Cooper", "Reality Show Judge", 42, "Smooth",
                "Rude and Harsh", "Crack Shot", 4, "Bulletproof Vest")
guest4 = Person("4 ", "Camilla Royce", "Society Lady", 46, "Warm Hearted",
                "Classist", "Poisoner", 2, "Anctidote")
guest5 = Person("5 ", "", "", "", "n/a", "n/a", "innocent", "n/a", "n/a")
"""
function to show guest details
"""
def show_guest_details(object):
    print(guest1.index + guest1.name)
    print(guest2.index + guest2.name)
    print(guest3.index + guest3.name)
    print(guest4.index + guest4.name)
    print(guest5.index + guest5.name)

show_guest_details(object)
   
'''
I have created a new class for location
'''  


