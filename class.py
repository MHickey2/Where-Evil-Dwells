'''
This is a docstring. I have created a new class for Person
'''

class Person:
	def __init__(self, name, occupation, age, goodQuality, badQuality, 
                 killerMoves, ranking, kryptonite):
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
guest1 = Person("Luscious Campbell", "Blogger", 29, "Enthusiastic", "Self-Obsessed", 
                "Bludgeoning with Selfie stick", 3, "Safety Helmet")        
guest2 = Person("Brad Jameson", "Actor/Model", 32, "Charasmatic", "Narscicist", 
                "uses murder methods from movies", 6, "Book on movie murders") 
guest3 = Person("Tobias Cooper", "Reality Show Judge", 42, "Super Smooth", 
                "Rude and Harsh", "Crack Shot", 4, "Bulletproof Vest")
guest4 = Person("Camilla Royce", "Society Lady", 46, "Warm Hearted", 
                "Classist", "Poisoner", 2, "Anctidote") 

print(guest1)  

def show_guest_details():
    print("The guest/'s name is {name}")
    print("The guest/'s occupation is {occupation}")
    print("The guest/'s age is {age}")
    print("The guest/'s best quality: {goodQuality}")
    print("The guest/'s worsst quality: {badQuality}")
   
'''
I have created a new class for location
'''  
