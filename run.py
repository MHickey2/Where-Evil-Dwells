"""
Text Based Adventure Game
"""
import os
import re
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
global player


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


def clear():
    """_This clears the screen_
    """
    command = 'clear'
    os.system(command)


def options_for_player():
    options = input("S to start again, or L to leave s/l:\n")
    if options.lower().strip() == "s":
        main()
    if options.lower().strip() == "l":
        print("OK no problem\n")
        bye = pyfiglet.figlet_format(' Bye for \n Now!')
        print(bye)
        sys.exit()


def main():
    """_main function_
    """
    print(Fore.RED)
    print(Style.BRIGHT)
    print(Back.BLACK)
    word = pyfiglet.figlet_format(' WHERE  EVIL  DWELLS ')
    print(word)
    print(Fore.RED)
    print(Style.BRIGHT)
    response = input("Would you like to have an encounter with Evil?\n ")
    print(Fore.RESET)
    if response.lower().strip() == "yes":
        print("welcome to the Game, let's hope you make it out alive!")
        time.sleep(C)
        START = True
    elif response.lower().strip() == "no":
        print("understandable, sorry to see you go")
        START = False
        print("Are you sure I can't tempt you")
        options_for_player()
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
    print(Back.BLACK)
    print(Fore.LIGHTBLUE_EX + art.HOUSE)
    print(Fore.RESET)
    add_narration(narration.INTRO)
    time.sleep(C)


show_intro()


def accept_invite():
    """_user accepts or declines invite_
    """
    print(Fore.RED)
    print(Style.BRIGHT)
    RSVP = input("the question is do you accept the invite? yes/no?\n ")
    print(Fore.RESET)
    if RSVP.lower().strip() == "yes":
        print("Great, I see a Hot-Tub and Big Screen TV in your future")
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
        print("Let's try that again, shall we")
        print(Fore.RED)
        print(Style.BRIGHT)
        rsvp2 = input("Do you accept the invite? yes/no?\n ")
        print(Fore.RESET)
        if rsvp2 == "yes":
            print("Great choice, welcome!")
            time.sleep(A)
            print(Fore.LIGHTGREEN_EX + art.DOOR)
            print(Fore.RESET)
            add_narration(narration.ARRIVAL)
            time.sleep(A)
        elif rsvp2 == "no":
            print("Sorry to see you go")
            sys.exit()
        else:
            print("That is not a valid response")
            sys.exit()


accept_invite()


def add_player_details():
    """
    function to add player to the game
    """
    name = input("Enter your name:\n ")
    PLAYER = (name)
    # validating_name(name)
    if name == "":
        name = "Stranger"

    print("Welcome to Harland Manor " + name + "!")

"""
def validating_name(name):
   
    regex_name = re.compile(/^[A-Za-z]+$/, re.IGNORECASE)
    res = regex_name.search(name)
    # If match is found, the string is valid
    if res: 
        print("Valid")          
    # If match is not found, string is invalid
    else:
        print("Invalid")
        add_player_details()
"""

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
    print("Please provide your details to the other guests:")
    add_player_details()
    

print(Fore.LIGHTWHITE_EX + art.DRINK)
print(Fore.RESET)
print("You are now in the lounge, you can... ")
print("A. Make a start on the booze and work your way through the spirits")
print("B. Fill your pockets with canopies and the smoked salmon entrees")
print("C. Decide to explore a little, when you will get this change again")
print("D. Wait for the other guests to arrive")
print(Fore.RED)
print(Style.BRIGHT)
lounge = input("What is your pick A, B, C or D?\n ")
print(Fore.RESET)
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
    print(Fore.RED)
    print(Style.BRIGHT)
    staircase = input("You sneak out to the staircase, up or down?:\n ")
    print(Fore.RESET)
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
    print(Fore.RED)
    print(Style.BRIGHT)
    doorchoice = input("Which door do you pick to explore, 1, 2 or 3?\n ")
    print(Fore.RESET)
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
        print("Not a valid choice, but I suggest...")
        print("It's not worth the risk, get back to the lounge")


if staircase.lower().strip() == "up":
    print("You are going up the stairs to the bedroom area")
    print("On the landing you see a figure skulking on the landing")
    print("1. You follow him, he looks suspicious, and you are curious")
    print("2. You get scared and decide to return to the lounge")
    print("3. You ignore the skulker and continue your own skulking")
    print(Fore.RED)
    print(Style.BRIGHT)
    stranger = input("What do you do next, 1, 2 or 3?\n ")
    print(Fore.RESET)
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


print("You are mingling, when Jeeves enters with a letter on a tray")
print(Fore.RED)
print(Style.BRIGHT)
letter = input("Do you want to see what is in the letter? yes/no:\n ")
print(Fore.RESET)
if letter == "yes":
    time.sleep(C)
    print(Fore.BLACK)
    print(Back.WHITE)
    add_narration(narration.LETTER)
elif letter == "no":
    print("I guess that might have been important")
    print("A rock comes through window, with note attached, it reads")
    time.sleep(C)
    print(Fore.BLACK)
    print(Back.WHITE)
    add_narration(narration.LETTER)
else:
    print("Not a valid answer, but I\'ll help you out")
    print("You need to know this...")
    print(Fore.BLACK)
    print(Back.WHITE)
    add_narration(narration.LETTER)


def show_information(guest1):
    print('Name of Guest: ' + guest1.name + '\nOccupation: '
          + guest1.occupation + '\nAge: ' + str(guest1.age) +
          '\nGood Quality: ' + guest1.good_quality +
          '\nBad Quality: ' + guest1.bad_quality)


time.sleep(A)
print(Fore.WHITE)
print(Back.BLACK)
print("you are in a dangerous dilemma, you need to team up with a buddy")
print(Fore.RED)
print(Style.BRIGHT)
review = input("Would you like to see details on all or 1 2 3 or 4?\n ")
print(Fore.RESET)
if review == "all":
    print("\n")
    show_information(guest1)
    print("---------------")
    show_information(guest2)
    print("---------------")
    show_information(guest3)
    print("---------------")
    show_information(guest4)

elif review == "1":
    show_information(guest1)
elif review == "2":
    show_information(guest2)
elif review == "3":
    show_information(guest3)
elif review == "4":
    show_information(guest4)
else:
    print("not valid answer, but you can choose a Buddy anyway")
print(Fore.RED)
print(Style.BRIGHT)
buddychoice = input("Now you can choose your buddy? 1, 2, 3 or 4?\n ")
print(Fore.RESET)
if buddychoice == "1":
    buddy = "Luscious Campbell"
    print("You are teamed up with Luscious, I hope you like social media")
    print("and watch your back, there's a killer about")
elif buddychoice == "2":
    buddy = "Brad Jameson"
    print("You are teamed up with Brad, keep him away from mirrors")
    print("Keep your wits about you, there is a killer around")
elif buddychoice == "3":
    buddy = "Tobias Cooper"
    print("You are with Tobias, don't take it personal, he's always rude")
elif buddychoice == "4":
    buddy = "Camilla Royce"
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
print(Fore.RED)
print(Style.BRIGHT)
safetyitemchoice = input("What is your chosen protection, 1, 2, 3, 4, 5?\n ")
print(Fore.RESET)
if safetyitemchoice == "1":
    safetyitem = "Safety Helmet"
    print("You have selected a Safety Helmet")
    print("You never know when it will come in handy")
elif safetyitemchoice == "2":
    safetytem = "Bulletproof Vest"
    print("You have selected a Bulletproof Vest")
    print("The best offence is a good defense")
elif safetyitemchoice == "3":
    safetyitem = "Antidote"
    print("You have selected some Antidote")
    print("It will make sense at some point")
elif safetyitemchoice == "4":
    safetyitem = "Gun"
    print("You have selected a Gun")
    print("Have gun will travel, you can never be too sure")
elif safetyitemchoice == "5":
    safetyitem = "Book on Movie Murders"
    print("You have selected a Book on movie Murders")
    print("Read up well, it may just save your life")
else:
    print("You will be allocated a random choice of protection")
    safetyitem = random_item()


def survival():
    """
    will user survice, is your partner a killer
    """
    global killer
    global safetyitem

    if guest1.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Safety Helmet":
            print("Luscious was the killer along\n")
            print("Bad Luck, you die")
            print(Back.BLACK)
            print(Fore.LIGHTRED_EX + art.DEATH)
            print(Fore.RESET)
        else:
            print("Luscious tried to kill you by hitting you... ")
            print("with a selfie stick, lucky you were wearing....")
            print("your safety Helmet, you survive")
    else:
        print("You are safe, Luscious is not the killer")
        print("You will survive the night")


def luscious():
    """
    The Luscious Experience
    """
    if buddychoice == "1":
        print(Back.BLACK)
        print(Fore.LIGHTGREEN_EX + art.BEDROOM)
        print(Fore.RESET)
        add_narration(narration.LUSCIOUS)
        time.sleep(B)
        print("You settle in the bedroom, and your nerves are shot")
        print("Your partner has brought some brandy from the lounge")
        print(Fore.RED)
        print(Style.BRIGHT)
        brandy = input("She offers you a glass, do you say yes/no?\n")
        print(Fore.RESET)
        if brandy.lower().strip() == "yes":
            print("Well, that should fix the nerves ok")
        elif brandy.lower().strip() == "no":
            print("wise choice, you may need a clear head")
        else:
            print("That is not a valid choice, let's skip the drink")
            time.sleep(B)

        print("Luscious has no access to wifi, so is not a happy girl")
        print("you are settling in for the stay when you hear loud noises")
        print("It is coming from behind a doorway in the bedroom")
        print("1. Do you go see what's causing the noise")
        print("2. Do you ask Luscious to join you in the investigation")
        print("3. Do you pretend not to hear, and keep listening to Luscious")
        noise = ""
        print(Fore.RED)
        print(Style.BRIGHT)
        noise = input("What choice do you pick 1 2 or 3 ?\n ")
        print(Fore.RESET)
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

        time.sleep(B)
        print("\n")
        print("You are in the bedroom and have barricaded yourself in")
        print("Luscious has got a phone signal, and is trying to get help")
        print("She calls the police and tell them about the death threat")
        print("You feel better now, that the police are on their way")
        print("\n")
        print(Fore.RED)
        print(Style.BRIGHT)
        print("What do you feel like doing now?\n")
        print(Fore.RESET)
        print("1. You are tired, you take a nap while waiting for the police")
        print("2. You keep alert, clutching your safety item")
        print("3. You've had enough, you escape from this horror house")
        print(Fore.RED)
        print(Style.BRIGHT)
        escape = input("What is your choice 1 2 or 3: ")
        print(Fore.RESET)
        if escape == "1":
            print("you deserve a rest, I'm sure you'll sleep soundly")
            print("Then again, I would keep one eye open, you never know")
        elif escape == "2":
            print("Wise choice, no killer is going to get you")
        elif escape == "3":
            print("Who could blame you, you may be broke, but will be alive")
            options()            
        else:
            print("Not a valid choice, but its ok, you should wait here")

        time.sleep(B)
        print("\n")
        print("About 20 minutes later you hear a loud bang, somewhere close")
        print("You look around, but you cannot see Luscious, where is she")
        print("The light goes out, you start freaking out")
        print("You can sense someone is close to you...Are you in danger?")
        time.sleep(B)
        survival()


luscious()


def survival2():
    """
    will user survice, is your partner a killer
     """
    global killer
    global safetyitem

    if guest2.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Book on Movie Murders":
            print("Brad was the killer along\n")
            print("Bad Luck, you die")
            print(Back.BLACK)
            print(Fore.LIGHTRED_EX + art.DEATH)
            print(Fore.RESET)
        else:
            print("Brad tried to kill you by stabbing you... ")
            print("lucky you were wearing whatever")
            print(", you survive")
    else:
        print("You are safe, Brad is not the killer")
        print("You will survive the night")


def brad():
    """
    The Brad Experience
    """
    if buddychoice == "2":
        add_narration(narration.BRAD)
        time.sleep(B)
        print("You both look around the kitchen, to make sure it's safe")
        print("You make sure the doors are locked securely just in case")
        print("You are looking out the window, its dark outside...")
        print("Suddenly you see a figure crouching in the garden")
        print("You both are frantic, is the killer about to strike!")
        print(Fore.RED)
        print(Style.BRIGHT)
        print("What is your next step, will you:\n")
        print(Fore.RESET)
        print("1. Find a weapon and confront the crouching man together")
        print("2. Do you volunteer Brad to confront the man")
        print("3. Do you step up and deal with the guy yourself")
        print(Fore.RED)
        print(Style.BRIGHT)
        confrontation = input("What is your choice 1 2 or 3? ")
        print(Fore.RESET)
        if confrontation.lower().strip() == "1":
            print("you load up with pots and pans and go after the man")
            print("The mystery man disappears into bushes")
            print("You decide it's too dangergous, so you return to kitchen")
        elif confrontation.lower().strip() == "2":
            print("Brad wimps out and hides under the table")
            print("You join him under the table, twos company")
        elif confrontation.lower().strip() == "3":
            print("You chase after the man, full of bravado")
            print("He gives you the slip, so you return to the kitchen")
            print("Brad tells you he has your back, but you doubt it")
        else:
            print("That is not a valid choice")
            print("I guess you could wait here and hope he goes away")
            time.sleep(B)

        print("You are both spooked by the experience")
        print("You hear a door opening, it souds like it\'s coming from below")
        print("There is a door leading to the cellar")
        print("There seems to be someone rummaging in the cellar")
        print("The sound seems to be getting closer")
        print("You and Brad decide to: ")
        print("A. Ensure the cellar door is locked and and block it off")
        print("B. Leave by the backdoor and escape this House of Doom")
        print("C. Risk it all and go investigate the noise")
        cellar = input("What is your choice, A, B or C: ")
        if cellar == "a":
            print("Good choice, but he may find another way to get in")
        elif cellar == "b":
            print("You run away, you and Brad are never seen again")
            options_for_player()
        elif cellar == "c":
            print("Is that the wisest decision, well you only live once")
            print("\n")
            time.sleep(B)
            print("You and Brad sneak down the stairs, pots and pans in hand")
            print("When you reach the bottom, the outside door is wide open")
            print("The killer has fled again, they have a charmed life")
            print("You head back to the kitchen, shutting the cellar door")
        else:
            print("Not a valid answer")
            print("You could just sit here, and hope he wont find you\n")

        time.sleep(B)

        print("You are back in the kitchen, contemplating your next move")
        print("When suddenly, you hear a loud noise, you turn your head and..")
        time.sleep(B)
        survival2()


brad()


def survival3():
    """
    will user survice, is your partner a killer
     """
    global killer
    global safetyitem

    if guest3.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Bulletproof Vest":
            print("Tobias was the killer along\n")
            print("Bad Luck, you die")
            print(Back.BLACK)
            print(Fore.LIGHTRED_EX + art.DEATH)
            print(Fore.RESET)
        else:
            print("Tobias tried to kill you by shooting you... ")
            print("lucky you were wearing your bulletproof vest")
            print("You survive")
    else:
        print("You are safe, Tobias is not the killer")
        print("You will survive the night")


def tobias():
    """
    The Tobias Experience
    """
    if buddychoice == "3":
        add_narration(narration.TOBIAS)
        time.sleep(B)
        print("You are situated in the Study now, Tobias is hard work")
        print("He is all fired up about the situation and is disgruntled")
        print("You try to distract yourself from the ranting")
        print("\n")
        print("Your are looking around the study and try the landline")
        print("It looks\'s like the phone line has been cut")
        print("Tobias is not a happy and vows to sue for emotinal damage")
        print("You are trying to calm him, when you hear a loud noise outside")
        print("It is coming from the corridor, it may be the killer")
        print("You and Tobias decide to:")
        print("A. Shimmy down the drainpipe and escape, broke but alive")
        print("B. The wait and see approach, no rush")
        print("C. Grab improvised weapons and confront whoever it is")
        print(Fore.RED)
        print(Style.BRIGHT)
        CORRIDOR = input(":What is your course of action: a,b or C: \n")
        print(Fore.RESET)
        if CORRIDOR.lower().strip() == "a":
            print("But that big Screen TV is history")
            options_for_player()
        elif CORRIDOR.lower().strip() == "b":
            print("You listen for a while but don't hear anything further")
            print("You decide to venture outside and check it out")
        elif CORRIDOR.lower().strip() == "c":
            print("You and Tobias, tooled with a letter opener and Stapler")
            print("Leave the room and move down the corridor with stealth")
        else:
            print("Not a valid answer, you should leave the study anyway")
            print("Maybe you can find somewher safer to hide")

        time.sleep(B)

        print("You are now in the corridor, the person has long gone")
        print("You see a ladder leading up to the Attack")
        print("You figure the killer may be up there do you:")
        print("A. Go up the ladder and catch him before he get's you")
        print("B. Close the door of the attack and get rid of the ladder")
        print("C. Use this opportunity to run down the stairs and escape")
        print(Fore.RED)
        print(Style.BRIGHT)
        ATTIC = input(":What is your course of action: a,b or C: \n")
        print(Fore.RESET)
        if ATTIC.lower().strip() == "a":
            print("You make your way up the ladder really quitely")
            print("You and Tobias start searching the attack")
            print("You both split up to cover more ground")
            print("Afer a few minutes you hear footsteps behine you")
            print("You call out for Tobias, but he doesn\'t come")
            print("you hear a new noise and you brace yourself....")
            survival3()
        elif ATTIC.lower().strip() == "b":
            print("You decide to go back to the study and hide")
            print("You barricade the door with furniture")
            print("You decide to have a drink from the drinks cabinet")
            print("After a short time you feel tired and rest your eyes")
            print("You wake suddenly, startled by a noise inside the room")
            print("You hear a noise behind you but are too petrified to move")
            print("Overwhelmed you close your eyes and...")
            survival3()
        elif ATTIC.lower().strip() == "c":
            print("So close, but I guess you get to live another day")
            options_for_player()
        else:
            print("Not a valid answer, but let\'s check if you survive anyway")
            survival3()


tobias()


def survival4():
    """
    will user survice, is your partner a killer
     """
    global killer
    global safetyitem

    if guest4.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Antidote":
            print("Camilla was the killer all along\n")
            print("Bad Luck, you die")
            print(Back.BLACK)
            print(Fore.LIGHTRED_EX + art.DEATH)
            print(Fore.RESET)
        else:
            print("Camilla tried to kill you by shooting you... ")
            print("lucky you had the antidote")
            print("You survive")
    else:
        print("You are safe, Camilla is not the killer")
        print("You will survive the night")



def camilla():
    """
    The Camilla Experience
    """
    if buddychoice == "4":
        print(Back.BLACK)
        print(Fore.LIGHTBLUE_EX + art.KITCHEN)
        print(Fore.RESET)
        add_narration(narration.CAMILLA)
        time.sleep(B)
        print("You and Camilla make yourself comfortable in the Dining area")
        print("Camilla has come well prepared, she has a tray of food")
        print("Despite the fear, your appetite has not been affected")
        print("You eagerly tuck in to a variety of treats")
        print("Camilla is a great host and makes sure you clean your plate")
        print("\n")
        print("Your room is near the front door and you hear it being opened")
        print("You both here raised voices and then hear a scream")
        print("You and Camilla discuss your options, will you:")
        print("A. Escape through the window with Camilla by your side")
        print("B. You chance it and open the door to investigate the scream")
        print("C. You leave the room by a backdoor and check it out")
        print(Fore.RED)
        print(Style.BRIGHT)
        DOOR = input("What is your choice, A, B or C: \n")
        print(Fore.RESET)
        if DOOR.lower().strip() == "a":
            print("Well at least you are well fed and alive, that\'s good")
            options_for_player()
        elif DOOR.lower().strip() == "b":
            print("You both walk to the front door, you can\'t see anyone")
            print("You can\'t hear voices anymore, you decice to look around")
        elif DOOR.lower().strip() == "c":
            print("You are in the back foyer and have left the voices behind")
        else:
            print("Not a valid answer, you should check out the library")
            print("I think that scream came from there")

        print("\n")
        print("You and Camilla have reached the Library room and you enter")
        print("The room is in disarray, there has been an altercation")
        print("Books are scattered everywhere and the furniture is overturned")
        print("You see a message written in red on the mirror")
        print("The message says 'Leave Before you Both Die")
        print("You both are alarmed, do you: ")
        print("A. Retreat back to the dining room, maybe it will be safer")
        print("B. Try to find a phone and call for help, this is scary")
        print("C. You need a bathroom, you\'re feeling sick")
        print(Fore.RED)
        print(Style.BRIGHT)
        LIBRARY = input("What is your choice a, b or c: \n")
        print(Fore.RESET)
        if LIBRARY.lower().strip() == "a":
            print("You return to the Dining Room and lock the door")
            print("You hope this nightmare ends soon, you eat some more food")
        elif LIBRARY.lower().strip() == "b":
            print("You search for a phone and find one in the hall")
            print("The line is dead, I guess you both have to tough it out")
        elif LIBRARY.lower().strip() == "c":
            print("You find the bathroom and you feel much better")
            print("You return to the Dining Room")
            print("You and Camilla settle in for the duration")
        else:
            print("That is not a valid answer, better stay in the Dining Room")

        time.sleep(B)

        print("You have gorged yourself with the rest of the food")
        print("You are really spooked and you both need to unwind")
        print("You are not feeling well, you must have ate too much")
        print("Camilla is smoking out the window and you begin to nap")
        print("You don't know how long you have nodded off when...")
        print("You wake with a sense of foreboding, you are in danger")
        print("You try to shake the feeling, but it\'s useless")
        print("You know the killer may have you in their sight...")
        survival4()


camilla()