import classification
from classification import *
import narration
from narration import *
import art
from art import *
from classification import guest1, guest2, guest3, guest4
from classification import item1, item2, item3, item4, item5
import sys
import time
import random
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init()

# variables
start = "no"
rsvp = "no"
rsvp = "no"
staircase = "up"
doorchoice = "1"


A = 2.5
B = 2
C = 1
C = 0.2
D = 0.08


def add_narration(text_to_print):
    '''
    This prints all of the text slowly.
    # '''
    for character in text_to_print:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.020)

print(Fore.RED)
print(Back.BLACK)
print(Style.BRIGHT)
word = pyfiglet.figlet_format('WHERE  EVIL   DWELLS')
print(word)
response = input("Would you like to have an encounter with Evil?\n ")
if response.lower().strip() == "yes":
    print("welcome to the Game, let's hope you make it out alive!")
    time.sleep(C)
    start = True
elif response.lower().strip() == "no":
    print("understandable, sorry to see you go")
    start = False
    bye = pyfiglet.figlet_format(' Bye for Now!')
    print(bye)
    sys.exit()
else:
    print("That is not a valid response")
    start = False
    farewell = pyfiglet.figlet_format(' Come back soon!')
    print(farewell)
    sys.exit()
if start is True:
    time.sleep(B)

    '''
    _function to show intro to user_
    '''


def show_intro():
    time.sleep(A)
    print(Fore.LIGHTBLUE_EX + art.HOUSE)
    print(Fore.RESET)
    add_narration(narration.intro)
    time.sleep(A)

show_intro()
rsvp = input("the question is do you accept the invite? yes/no?\n ")
if rsvp.lower().strip() == "yes":
    print("Great, I see a hot-tub and Big Screen TV in your future")
    # Arrival Txt is opened and content is displayed to user
    rsvp = "yes"
    time.sleep(A)
    print(Fore.LIGHTGREEN_EX + art.DOOR)
    print(Fore.RESET)
    add_narration(narration.arrival)
    time.sleep(A)
elif rsvp.lower().strip() == "no":
    print("Well I guess it is instant noodles for you")
    rsvp = "no"
    bye = pyfiglet.figlet_format(' Bye for Now!')
    print(bye)
    sys.exit()
else:
    print("let's try that again, shall we")
    rsvp2 = input("The question is do you accept the invite? yes/no?\n ")
    if rsvp2 == "yes":
        print("Great choice, welcome")
    elif rsvp2 == "no":
        print("Sorry to see you go")
        sys.exit()
    else:
        print("That is not a valid response")
        sys.exit()
'''
setting lounge function
'''


def setting_lounge():
    print("You are in the lounge now and the other guests have arrived")
    print("There are four guests, they introuduce themselves, as: ")
    print(guest1.index + guest1.name)
    print(guest2.index + guest2.name)
    print(guest3.index + guest3.name)
    print(guest4.index + guest4.name)
    print("Please provide your details to the other guests: ")


time.sleep(A)
print(Fore.LIGHTWHITE_EX + art.DRINK)
print(Fore.RESET)
print("You are now in the lounge, you can... ")
print("A. Make a start on the booze and work your way through the spirits")
print("B. Fill your pockets with canopies and the smoked salmon entrees")
print("C. Decide to explore a little, when you will get this change again")
print("D. Wait for the other guests to arrive")
lounge = input("What is your pick A, B, C or D?\n ")
if lounge.lower().strip() == "a":
    print("Remember moderation is key, let's wait for the other guests")
    setting_lounge()
    time.sleep(A)
elif lounge.lower().strip() == "b":
    print("Leave some food for the other guests, let's wait for them")
    setting_lounge()
    time.sleep(A)
elif lounge.lower().strip() == "c":
    print("Great choice, take a canopy for the road, and start exploring")    
    time.sleep(A)
elif lounge.lower().strip() == "d":
    print("What no food or drink, let's wait for the other guests")
    setting_lounge()
    time.sleep(A)
else:
    print("I guess you're here now anyway, best wait for the other guests")
    setting_lounge()
    time.sleep(A)

if lounge.lower().strip() == "c":
    staircase = input("You sneak out to the staircase, up or down?: ")
    print(Fore.LIGHTBLUE_EX + art.ARROWS)
    print(Fore.RESET)
else:
    print("down it is")

if staircase.lower().strip() == "down":
    print("You are going down a creepy dark staircase to the cellar")
    print("When you reach the bottom, you can see 3 doors...")
    print("1. A battered door, it that maniacal laughter you hear?")
    print("2. A pristine door in mint shape, with soothing music inside")
    print("3. A solid oak door, with a stange tapping sound from within")
    doorchoice = input("Which door do you pick to explore, 1, 2 or 3?\n ")
    time.sleep(B)
    if doorchoice.strip() == "1":
        print(" you enter, you see a caged bird laughing, that's weird")
        print("Feels cold here and am hungry again, back to the lounge")
        setting_lounge()
    elif doorchoice.strip() == "2":
        print(" oh, no, you'been caught by Jeeves, doing his meditation")
        print("He is furious and sends you to the lounge, see you there")
        setting_lounge()
    elif doorchoice.strip() == "3":
        print("You enter the room, and are caught by an evil wrongdoer")
        print("alas the adventure has ended, better luck next time")
        word = pyfiglet.figlet_format(' Game Over! ')
        print(word)
        sys.exit()
    else:
        print("It's not worth the risk, get back to the lounge")
        

if staircase.lower().strip() == "up":
    print("You are going up the stairs to the bedroom area")
else:
    print("maybe you should go back to the lounge instead")

print("On the landing you see a figure skulking on the landing")
print("1. You follow him, he looks suspicious, and you are curious")
print("2. You get scared and decide to return to the lounge")
print("3. You ignore the skulker and continue your own skulking")
stranger = input("What do you do next, 1, 2 or 3? ")
if stranger.lower().strip() == "1":
    print("You stalk the stalker, like a ninja")
    print("right until, he turns around and puts you in a headlock")
    print("Sorry the Stalker caught you, better luck next time")
    word = pyfiglet.figlet_format(' Game Over! ')
    print(word)
    sys.exit()
elif stranger.lower().strip() == "2":
    print(" Good chooice, they maybe running out of the food")
    print("You have a hankering for a pig in a blanket")
    print("Back to the lounge you go")
    setting_lounge()
elif stranger.lower().strip() == "3":
    print("There's too many skulkers in this house for your liking!")
    print("Time to end the skulking, and get back to the food")
    setting_lounge()
else:
    print("Is that rancheros I smell, I'm in the mood for a ranchero!")
    print("The lounge is the best place to be right now anyway")
    setting_lounge()

'''
function to add user as guest
'''


def add_guest_details():
    name = input("Enter your name:/n ")
    occupation = input("Enter your occupation:/n ")
    age = input("Enter your age:/n ")
    guest5 = (name, occupation, age)
    print(guest5)


add_guest_details()

print("The guests are mingling, when Jeeves enters with a letter on a tray")
letter = input("Do you want to see what is in the letter? yes/no:\n ")
if letter == "yes":
    time.sleep(A)
    add_narration(narration.letter)
if letter == "no":
    print("I guess that might have been important")
    print("A rock comes through window, with note attached, it reads")
    time.sleep(A)
    add_narration(narration.letter)

time.sleep(A)
print("you are in a dangerous dilemma, you need to team up with a buddy")
review = input("Would you like to see details on all or 1/2/3/4?\n ")
if review == "all":
    print(vars(guest1))
    print(vars(guest2))
    print(vars(guest3))
    print(vars(guest4))
elif review == 1:
    print(vars(guest1))
elif review == 2:
    print(vars(guest2))
elif review == 3:
    print(vars(guest3))
elif review == 4:
    print(vars(guest4))
else:
    print("not valid answer")

buddy = input("Now you can choose who is your buddy? 1, 2, 3 or 4?\n ")
if buddy == "1":
    print("You are teamed up with Luscious, I hope you like social media")
    print("and watch your back, there's a killer about")
elif buddy == "2":
    print("You are teamed up with Brad, keep him away from mirrors")
    print("Keep your wits about you, there is a killer around")
elif buddy == "3":
    print("You are with Tobias, don't take it personal, he's always rude")
elif buddy == "4":
    print("You are with Camilla, try to act richer")
else:
    print("need to pick someone, it's not safe alone")
    buddy = input("Now you can choose who is your buddy? 1, 2, 3 or 4?\n ")
    if buddy == "1":
        print("You are teamed up with Luscious, I hope you like social media")
        print("and watch your back, there's a killer about")
    elif buddy == "2":
        print("You are teamed up with Brad, keep him away from mirrors")
        print("Keep your wits about you, there is a killer around")
    elif buddy == "3":
        print("You are with Tobias, don't take it personal, he's always rude")
    elif buddy == "4":
        print("You are with Camilla, try to act richer")
    else:
        print("Sorry, it's too dangerous alone, i think it's safer to leave")
        word = pyfiglet.figlet_format(' Game Over! ')
        print(word)
        sys.exit()
print("Before you leave with your Buddy there is one more thing...")
print("For your own safety, you get to choose an item of protection...")
print(item1.index + item1.name)
print(item2.index + item2.name)
print(item3.index + item3.name)
print(item4.index + item4.name)
print(item5.index + item5.name)
safetyitemchoice = input("What is your chosen protection, 1, 2, 3, 4, 5?\n ")
if safetyitemchoice == "1":
    print("You never know when it will come in handy")
elif safetyitemchoice == "2":
    print("The best offence is a good defense")
elif safetyitemchoice == "3":
    print("It will make sense at some point")
elif safetyitemchoice == "4":
    print("Have gun will travel, you can never be too sure")
elif safetyitemchoice == "5":
    print("Read up well, it may just save your life")
else:
    print("You will be allocated a random choice of protection")
    random_safetyitem()
    print("you have been allocated a (safetyitem)")