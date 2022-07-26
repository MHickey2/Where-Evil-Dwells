import classification
from classification import Person
from classification import guest1, guest2, guest3, guest4
# import sys,time
import time
import random
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init()

# variables
global guest1
global guest2
global guest3
global guest4


A = 2.5
B = 2
C = 0.2
D = 0.08

print(Fore.RED)
print(Back.BLACK)
print(Style.BRIGHT)
word = pyfiglet.figlet_format(' WHERE  EVIL   DWELLS')
print(word)
response = input("Would you like to have an encounter with Evil? ")
if response.lower().strip() == "yes":
    print("welcome to the Game, let's hope you make it out alive!")
    time.sleep(B)
    start = True
elif response.lower().strip() == "no":
    print("understandable, sorry to see you go")
    start = False
    word = pyfiglet.figlet_format(' Bye for Now!')
    print(word)
else:
    print("That is not a valid response")
    start = False
if start is True:
    time.sleep(B)
    '''
    _function to show intro to user_
    '''


def show_intro():
    time.sleep(A)
    print("You are invited to a reading of a Will at Harland Manor")
    time.sleep(A)
    print("an old house steeped in mystery..")
    time.sleep(A)
    print("With a long history of murder and debauchery")
    time.sleep(A)
    print("It is in relation to your great uncle Raymon DeCharles")
    time.sleep(A)
    print("It is a frightening prospect, but you really need the money")
    time.sleep(A)


show_intro()
rsvp = input("the question is do you accept the invite? yes/no ")
if rsvp.lower().strip() == "yes":
    print("Great, I see a hot-tub and Big Screen TV in your future")
    # Arrival Txt is opened and content is displayed to user
    rsvp = "yes"
    time.sleep(A)
    with open('arrival.txt') as f:
        contents = f.read()
    print(contents)
    f.close()
elif rsvp.lower().strip() == "no":
    print("Well I guess it is instant noodles for you")
    rsvp = "no"
else:
    print("let's try that again, shall we")
    print("the question is do you accept the invite? yes/no? ")
    if rsvp is True:
        print("Great choice, welcome")
    if rsvp is False:
        print("Sorry to see you go")
    else:
        print("That is not a valid response")
if rsvp is True:
    print("I knew you'd see sense")
if rsvp is False:
    print("Sorry to see you go")
time.sleep(A)
print("You are now in the lounge, you can.. ")
print("A. Make a start on the booze and work your way through the spirits")
print("B. Fill your pockets with canopies and the smoked salmon entrees")
print("C. Decide to explore a little, when you will get this change again")
print("D. Wait for the other guests to arrive")
lounge = input("What is your pick,  A, B, C or D? ")
if lounge.lower().strip() == "A":
    print("A. Remember moderation is key, let's wait for the other guests")
    time.sleep(A)
elif lounge == "B":
    print("B. Leave some food for the other guests, let's wait for them")
    time.sleep(A)
elif lounge.lower().strip() == "C":
    print("C. Great choice, take a canopy for the road, the adventure begins")
    time.sleep(A)
elif lounge.lower().strip() == "D":
    print("D. What no food or drink, let's wait for the other guests")
    time.sleep(A)
else:
    print("I guess you're here now anyway, best wait for the other guests")
time.sleep(A)
staircase = input("You sneak out and get to the staircase, up or down?/n ")
if staircase.lower().strip() == "down":
    print("you are going down a creepy dark staircase to the cellar")
    print("1. A battered door, it that maniacal laughter you hear?")
    print("2. A pristine door in mint codition, with soothing music within")
    print("3. A solid oak door, with a stange tapping sound from within")
doorchoice = input("Which door do you pick to explore, 1, 2 or 3? ")
time.sleep(B)
if doorchoice.lower().strip() == "1":
    print(" you enter, you see a caged bird laughing, well that's weird")
    print("Feels cold down here and am hungry again, back to the lounge")
elif doorchoice.lower().strip() == "2":
    print(" oh, no, you'been caught by Jeeves, doing his meditation")
    print("He is furious and sends you back to the lounge, see you there")
elif doorchoice.lower().strip() == "3":
    print("You enter the room, and are caught by an evil wrongdoer")
    print("alas the adventure has ended for you, better luck next time")
    # adventure ends
    word = pyfiglet.figlet_format(' Game Over! ')
    print(word)
else:
    print("You're right it's not worth the risk, get back to the lounge")
    print("I'll help you decide, let's go down, no worries")
if staircase.lower().strip() == "up":
    print("You are going up to the bedroom area, it's well lit")
print("At the top of the stairs you see a figure skulking on the landing")
print("1. You follow him, he looks suspicious, and you are curious")
print("2. You get scared and decide to return to the lounge")
print("3. You ignore the skulking person and continue skulking")
stranger = input("What do you do next, 1,2 or 3? ")
if stranger.lower().strip() == "1":
    print("You stalk the stalker, like a ninja")
    print("right until, he turns around and puts you in a headlock")
    print("Sorry the Stalker caught you, better luck next time")
    word = pyfiglet.figlet_format(' Game Over! ')
    print(word)
    # adventure ends
elif stranger.lower().strip() == "2":
    print(" Good chooice, they may be finishing off the food right now")
    print("You have a hankering for a pig in a blanket")
elif stranger.lower().strip() == "3":
    print("There's one too maney skulkers in this house for your liking!")
else:
    print("Is that rancheros I smell, I'm in the mood for a ranchero!")

print("You are back in the loung and the guests have arrived")
print("There are four guests, they introuduce themselves, they are:")
print(guest1.index + guest1.name)
print(guest2.index + guest2.name)
print(guest3.index + guest3.name)
print(guest4.index + guest4.name)
print("Please add youn input to joing the other guests")

'''
function to add user as guest
'''


def add_guest():
    name = input("Enter your name: ")
    occupation = input("Enter your occupation: ")
    age = input("Enter your age: ")
    guest5 = (name, occupation, age)
    print(guest5)


add_guest()

print("The guests are mingling, when Jeeves enters with a letter on a tray")
letter = input("Do you want to see what is in the letter? yes/no")
if letter == "yes":
    time.sleep(A)
    with open('letter.txt') as f:
        contents = f.read()
        print(contents)
        f.close()
if letter == "no":
    print("I guess that might have been important")
    print("A rock comes through window, with note attached, it reads")
    time.sleep(A)
    with open('letter.txt') as f:
        contents = f.read()
        print(contents)
        f.close()
        
