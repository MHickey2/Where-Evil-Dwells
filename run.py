"""
Text Based Adventure Game
"""
import sys
import time
import random
import classification
from classification import *
import narration
from narration import *
import art
from art import *
from classification import guest1, guest2, guest3, guest4
from classification import item1, item2, item3, item4, item5
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init()

# variables
START = False
RSVP = "no"
staircase = ""
doorchoice = ""
global buddy
global safetyitem


A = 3
B = 2
C = 1
D = 0.2
E = 0.08


def add_narration(printed_text):
    """
    This prints all of the text from
    narration.py slowly.
    """
    for character in printed_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.060)


def main():
    """_main function_
    """
    print(Fore.RED)
    print(Back.BLACK)
    print(Style.BRIGHT)
    word = pyfiglet.figlet_format(' WHERE  EVIL   DWELLS ')
    print(word)
    response = input("Would you like to have an encounter with Evil?\n ")
    if response.lower().strip() == "yes":
        print("welcome to the Game, let's hope you make it out alive!")
        time.sleep(C)
        START = True
    elif response.lower().strip() == "no":
        print("understandable, sorry to see you go")
        START = False
        BYE = pyfiglet.figlet_format(' Bye for Now!')
        print(BYE)
        sys.exit()
    else:
        print("That is not a valid response")
        START = False
        farewell = pyfiglet.figlet_format(' Come back soon! ')
        print(farewell)
        sys.exit()
    if START is True:
        time.sleep(C)


main()


def show_intro():
    """
    _function to show intro to the user_
    """
    time.sleep(C)
    print(Fore.LIGHTBLUE_EX + art.HOUSE)
    print(Fore.RESET)
    add_narration(narration.INTRO)
    time.sleep(C)


show_intro()


def accept_invite():
    """_user accepts or declines invite_
    """
    RSVP = input("the question is do you accept the invite? yes/no?\n ")
    if RSVP.lower().strip() == "yes":
        print("Great, I see a hot-tub and Big Screen TV in your future")
        # Arrival Txt from Narration content is displayed to user
        RSVP = "yes"
        time.sleep(A)
        print(Fore.LIGHTGREEN_EX + art.DOOR)
        print(Fore.RESET)
        add_narration(narration.ARRIVAL)
        time.sleep(A)
    elif RSVP.lower().strip() == "no":
        print("Well I guess it is instant noodles for you")
        RSVP = "no"
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


accept_invite()


def setting_lounge():
    """
    setting lounge function
    """
    print("You are in the lounge now and the other guests have arrived")
    print("There are four guests, they introuduce themselves, as:\n ")
    print(guest1.index + guest1.name)
    print(guest2.index + guest2.name)
    print(guest3.index + guest3.name)
    print(guest4.index + guest4.name)
    print("Please provide your details to the other guests: ")


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
    print()
    setting_lounge()
    time.sleep(A)
else:
    print("I guess you're here now anyway, best wait for the other guests")
    print()
    setting_lounge()
    time.sleep(A)

if lounge.lower().strip() == "c":
    staircase = input("You sneak out to the staircase, up or down?:\n ")
    print(Fore.LIGHTBLUE_EX + art.ARROWS)
    print(Fore.RESET)
else:
    print()

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
    print("On the landing you see a figure skulking on the landing")
    print("1. You follow him, he looks suspicious, and you are curious")
    print("2. You get scared and decide to return to the lounge")
    print("3. You ignore the skulker and continue your own skulking")
    stranger = input("What do you do next, 1, 2 or 3?\n ")
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


def add_guest_details():
    """
    function to add user as guest
    """
    name = input("Enter your name:\n ")
    occupation = input("Enter your occupation:\n ")
    age = input("Enter your age:\n ")
    guest5 = (name, occupation, age)
    print(guest5)


add_guest_details()




print("The guests are mingling, when Jeeves enters with a letter on a tray")
letter = input("Do you want to see what is in the letter? yes/no:\n ")
if letter == "yes":
    time.sleep(B)
    print(Fore.BLACK)
    print(Back.WHITE)
    add_narration(narration.LETTER)
if letter == "no":
    print("I guess that might have been important")
    print("A rock comes through window, with note attached, it reads")
    time.sleep(B)
    print(Fore.BLACK)
    print(Back.WHITE)
    add_narration(narration.LETTER)

time.sleep(A)
print(Fore.WHITE)
print(Back.BLACK)
print("you are in a dangerous dilemma, you need to team up with a buddy")
review = input("Would you like to see details on all or 1 2 3 or 4?\n ")
if review == "all":
    print(vars(guest1))
    print(vars(guest2))
    print(vars(guest3))
    print(vars(guest4))
elif review == "1":
    print(vars(guest1))
elif review == "2":
    print(vars(guest2))
elif review == "3":
    print(vars(guest3))
elif review == "4":
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
    


def luscious():
    """
    The Luscious Experience
    """
    if buddy == "1":
        add_narration(narration.LUSCIOUS)
        time.sleep(B)
        print("You settle in the bedroom, and your nerves are shot")
        print("Your partner has brought some brandy from the lounge")
        brandy = input("She offers you a glass, do you say yes/no?\n")
        if brandy.lower().strip() == "yes":
            print("Well, that should fix the nerves ok")
        elif brandy.lower().strip() == "no":
            print("wise choice, you may need a clear head")
        else:
            print("That is not a valid choice")
            time.sleep(B)

        print("Luscious has no access to wifi, so is not a happy girl")
        print("you are settling in for the stay when you hear loud noises")
        print("It is coming from behind a doorway in the bedroom")
        print("1. Do you go see what's causing the noise")
        print("2. Do you ask Luscious to join you in the investigation")
        print("3. Do you pretend not to hear, and keep listening to Luscious")
        noise = ""
        noise = input("What choice do you pick 1 2 or 3 ?\n ")
        if noise == "1":
            print("Brave choice, it's better to know and be prepared")
            add_narration(narration.SECRET_ROOM)
            time.sleep(B)
        elif noise == "2":
            print("The two of you check out the noise")
            add_narration(narration.SECRET_ROOM)
            time.sleep(B)
        elif noise == "3":
            print("Maybe Luscious ranting will block out that noise")
            print("With any luck it's not a murderer planning an attack")
        else:
            print("Not a valid choice, I guess we'll just wait and see")
            print("What's the worse that can happen...ahem")

        print("You are in the bedroom and have barricaded yourself in")
        print("Luscious has got a phone signal, and is trying to get help")
        print("She calls the police and tell them about the death threat")
        print("You feel better now, that the police are on their way")
      
        print("What do you feel like doing now?\n")
        print("1. You are tired, you take a nap while waiting for the police")
        print("2. You keep alert, clutching your safety item")
        print("3. You've had enough, you escape from this horror house")
        escape = input("What is your choice 1 2 or 3: ")
        if escape == "1":
            print("you deserve a rest, I'm sure you'll sleep soundly")
        elif escape == "2":
            print("Wise choice, no killer is going to get you")
        elif escape == "3":
            print("Who could blame you, you may be broke, but will be alive")
            goodbye = pyfiglet.figlet_format(' Goodbye')
            print(goodbye)
            sys.exit()
        else:
            print("Not a valid choice")
            


luscious()
random_safetyitem_and_survival()


def brad():
    """
    The Brad Experience
    """
    if buddy == "2":
        add_narration(narration.BRAD)
        time.sleep(B)


brad()


def tobias():
    """
    The Tobias Experience
    """
    if buddy == "3":
        add_narration(narration.TOBIAS)
        time.sleep(B)


tobias()


def camilla():
    """
    The Camilla Experience
    """
    if buddy == "4":
        add_narration(narration.CAMILLA)
        time.sleep(B)


camilla()

