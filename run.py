"""
Text Based Adventure Game based on the old horror movie genre, set in a creepy
house and the player is coming as a benefactor, and then there is the matter
of a warning, whereby someone in the house means to kill them and they have
to survive by choosing a safe route throughout the game and their fate will
be determined by their game play
"""

import os
import sys
import time
import random

import colorama
import pyfiglet
from colorama import Back, Fore, Style

import art
import narration
from classification import (guest1, guest2, guest3, guest4, item1, item2,
                            item3, item4, item5, killer, random_item)

colorama.init()

# time sleep duration options
A = 2.5
B = 1.5
C = .08
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
        time.sleep(0.030)


def clear():
    """_This clears the screen_
    """
    command = 'clear'
    os.system(command)


def random_buddy():
    """
    random buddy selection, in case player does not select themselves.
    """
    buddylist = [guest1.index, guest2.index, guest3.index, guest4.index]
    randombuddy = random.choice(buddylist)
    return randombuddy


random_buddy()


def goodbye():
    """_This displays leaving message_
    """
    print(Fore.RED)
    print(Back.BLACK)
    bye = pyfiglet.figlet_format(' Bye for Now!')
    print(bye)
    print(Fore.RESET)
    sys.exit()


def options_for_player():
    """_allows user to leave or instructions on
         how to start the game again_
    """
    options = input("print L to leave the game\n")
    if options.lower().strip() == "l":
        print((Fore.BLUE) + "OK, Thanks for Playing!\n")
        goodbye()
    else:
        print("Use button above to restart Game")
        goodbye()


def main():
    """_main function, the players intro screen for game_
    """
    print(Fore.RED)
    print(Style.BRIGHT)    
    print(Fore.RED + art.BANNER)
    while True:
        response = input("Want to play a Game? yes/no\n ").lower().strip()
        print(Fore.RESET)
        if response not in {"yes", "no"}:
            print("Invalid input")
            continue
        if response == "yes":            
            print("welcome to the Game, let's hope you make it out alive!\n")
            time.sleep(B)
            start_game = True
            break
        elif response == "no":           
            print("understandable, sorry to see you go")
            start_game = False
            goodbye()

        if start_game is True:
            time.sleep(C)


main()


def show_instructions():
    """_function, to show instructions to the player_
    """
    while True:
        print(Fore.RED)
        print(Style.BRIGHT)
        instructions = input("See Instructions yes/no\n ").lower().strip()
        print(Fore.RESET)
        if instructions not in {"yes", "no"}:
            print("Invalid input")
            continue
        if instructions == "yes":
            print(Back.WHITE)
            add_narration((Fore.BLACK) + narration.INSTRUCTIONS)
            print(Fore.RESET)
            print(Back.RESET)
            time.sleep(A)
            break
        elif instructions == "no":
            print(Fore.RESET)
            print("No problem, it\'s easy to understand anyway")
            time.sleep(A)
            break


show_instructions()


def show_intro():
    """
    _function to show intro to the user_
    """
    time.sleep(B)
    print(Back.BLACK)
    print(Fore.LIGHTBLUE_EX + art.HOUSE)
    print(Fore.RESET)
    add_narration(narration.INTRO)
    time.sleep(C)


show_intro()


def accept_invite():
    """_user accepts or declines invite to House in Game_
    """
    while True:
        print(Fore.RED)
        print(Style.BRIGHT)
        rsvp_accepted = input("Accept the invite? yes/no?\n ").lower().strip()
        print(Fore.RESET)
        if rsvp_accepted not in {"yes", "no"}:
            print("Invalid input")
            continue
        if rsvp_accepted == "yes":
            print("Great, I see a Hot-Tub and Big Screen TV in your future")
            rsvp_accepted = "yes"
            time.sleep(A)
            print(Fore.LIGHTGREEN_EX + art.DOOR)
            print(Fore.RESET)
            add_narration(narration.ARRIVAL)
            time.sleep(A)
            break
        elif rsvp_accepted == "no":
            print("Well I guess it is instant noodles for you")
            rsvp_accepted = "no"
            goodbye()


accept_invite()


def you_die():
    """_Final Message if you die in game_
    """
    print("\n")
    print("Bad Luck, you die")
    print(Back.BLACK)
    print(Fore.LIGHTRED_EX + art.DEATH)
    print(Fore.RESET)
    sys.exit()


def add_player_details():
    """_Function to add player to the game,
    and checks if the name is acceptable_
    """
    while True:
        minlen = 3
        name = input("Enter your name:\n ").lower().strip()
        # name can't be a number
        if not name.isalpha():
            print((Fore.RED) + "Your name must only have digits")
            print(Fore.RESET)
            continue
        # name can't be shorter than minlen
        if len(name) < minlen:
            print((Fore.RED) + "minimum length must be at least 3")
            print(Fore.RESET)
            continue
        # name field can't be left blank
        if name == " ":
            print((Fore.RED) + "You can\'t leave name blank")
            print(Fore.RESET)
            continue
        else:
            print(Fore.RESET)
            print(Fore.BLUE)
            print(Style.BRIGHT)
            print("Welcome to Harland Manor " + (name.capitalize()) + "!")
            print(Fore.RESET)
            break


def setting_lounge():
    """_lounge setting function, entry to gameplay_
    """
    time.sleep(B)
    print("\n")
    print("You are in the lounge now and the other guests have arrived")
    print("There are four guests, they introuduce themselves as:\n")
    print(guest1.index + " " + guest1.name)
    print(guest2.index + " " + guest2.name)
    print(guest3.index + " " + guest3.name)
    print(guest4.index + " " + guest4.name)
    print("\n")
    print("Please provide your details to the other guests:\n")
    print("Just need your first name, thanks")
    add_player_details()


print(Fore.LIGHTWHITE_EX + art.DRINK)
print(Fore.RESET)
print("You are now in the lounge, you can... ")
print("A. Make a start on the booze and work your way through the spirits")
print("B. Fill your pockets with canopies and the smoked salmon entrees")
print("C. Decide to explore a little, when will you get this change again")
print("D. Wait for the other guests to arrive")
while True:
    print(Fore.RED)
    print(Style.BRIGHT)
    lounge_action = input("Your choice A, B, C or D?\n ").lower().strip()
    if lounge_action not in {"a", "b", "c", "d"}:
        print("Invalid input")
        continue
    if lounge_action == "a":
        print(Fore.RESET)
        print("Remember moderation is key, let's wait for the other guests")
        setting_lounge()
        time.sleep(A)
        break
    elif lounge_action == "b":
        print(Fore.RESET)
        print("Leave some food for the other guests, let's wait for them")
        setting_lounge()
        time.sleep(A)
        break
    elif lounge_action == "c":
        print(Fore.RESET)
        print("Great choice, take a canopy for the road, and start exploring")
        time.sleep(A)
        break
    elif lounge_action == "d":
        print(Fore.RESET)
        print("What no food or drink, let's wait for the other guests")
        print()
        setting_lounge()
        time.sleep(A)
        break

if lounge_action == "c":
    while True:
        print(Fore.RED)
        print(Style.BRIGHT)
        staircase = input("At the staircase now, up/down?\n ").lower().strip()
        if staircase not in {"up", "down"}:
            print("Invalid input")
            continue
        print(Fore.RESET)
        print(Fore.LIGHTBLUE_EX + art.ARROWS)
        print(Fore.RESET)
        if staircase == "down":
            print("You are going down a creepy staircase to the cellar")
            print("When you reach the bottom, you can see 3 doors...")
            print("1. A battered door, it that laughter you hear?")
            print("2. A pristine door, with soothing music inside")
            print("3. A solid oak door, with a tapping sound from within")
            while True:
                print(Fore.RED)
                print(Style.BRIGHT)
                doorchoice = input("Explore which door, 1, 2 or 3?\n").strip()
                print(Fore.RESET)
                time.sleep(B)
                if doorchoice not in {"1", "2", "3"}:
                    print("Invalid input")
                    continue
                if doorchoice == "1":
                    print("you enter, you see a caged bird laughing, weird..")
                    print("You feel cold and hungry again, back to the lounge")
                    setting_lounge()
                    break
                elif doorchoice == "2":
                    print("oh, no, you'been caught by Jeeves meditating")
                    print("He is furious and sends you back to the lounge")
                    setting_lounge()
                    break
                elif doorchoice == "3":
                    print("You enter, and are caught by an evil wrongdoer")
                    print("alas the adventure is over, better luck next time")
                    you_die()
            break

        if staircase == "up":
            print(Fore.RESET)
            print("You are going up the stairs to the bedroom area")
            print("On the landing you see a person skulking")
            print("1. You follow him, he looks suspicious")
            print("2. You get scared and decide to return to the lounge")
            print("3. You ignore the skulker and continue skulking")
            while True:
                print(Fore.RED)
                print(Style.BRIGHT)
                stranger = input("What do you do next, 1, 2 or 3?\n ").strip()
                if stranger not in {"1", "2", "3"}:
                    print("Invalid input")
                    print(Fore.RESET)
                    continue
                if stranger == "1":
                    print(Fore.RESET)
                    print("You stalk the stalker, like a ninja")
                    print("right until, he turns and puts you in a headlock")
                    print("The Stalker caught you, better luck next time")
                    you_die()
                elif stranger == "2":
                    print(Fore.RESET)
                    print("Good chooice, they maybe running out of the food")
                    print("You have a hankering for a pig in a blanket")
                    print("Back to the lounge you go")
                    setting_lounge()
                    break
                elif stranger == "3":
                    print(Fore.RESET)
                    print("There's too many skulkers for your liking!")
                    print("Time to end the skulking, and get back to the food")
                    setting_lounge()
                    break
            break


print("\n")
print("You are mingling, when Jeeves enters with a letter on a tray")
print("This looks ominous, Jeeves offers to show you the details...")
while True:
    print(Fore.RED)
    print(Style.BRIGHT)
    letter = input("Want to read the letter? yes/no\n").lower().strip()
    if letter not in {"yes", "no"}:
        print("Invalid input")
        continue
    if letter == "yes":
        time.sleep(C)
        print(Fore.BLACK)
        print(Back.WHITE)
        add_narration(narration.LETTER)
        print(Fore.RESET)
        print("\n")
        break
    elif letter == "no":
        print(Fore.RESET)
        print("I guess that might have been important")
        print("A rock comes through window, with note attached, it reads:")
        time.sleep(C)
        print(Fore.BLACK)
        print(Back.WHITE)
        add_narration(narration.LETTER)
        print("\n")
        break


def show_information(guest1):
    """_show format for guest details_
    """
    print('Name of Guest: ' + guest1.name + '\nOccupation: ' +
          guest1.occupation + '\nAge: ' + str(guest1.age) +
          '\nGood Quality: ' + guest1.good_quality +
          '\nBad Quality: ' + guest1.bad_quality)


time.sleep(A)
print(Fore.WHITE)
print(Back.BLACK)
print("you are in a dangerous dilemma, you need to team up with a buddy")

while True:
    print(Fore.RED)
    print(Style.BRIGHT)
    review = input("See details on 'all' or 1, 2, 3, or 4?\n ").lower().strip()
    if review not in {"all", "1", "2", "3", "4"}:
        print("Invalid input")
        continue
    print(Fore.RESET)
    if review == "all":
        print("\n")
        show_information(guest1)
        print("-------------------")
        show_information(guest2)
        print("-------------------")
        show_information(guest3)
        print("-------------------")
        show_information(guest4)
        print("-------------------")
        break
    elif review == "1":
        show_information(guest1)
        break
    elif review == "2":
        show_information(guest2)
        break
    elif review == "3":
        show_information(guest3)
        break
    elif review == "4":
        show_information(guest4)
        break

print(Fore.RED)
print(Style.BRIGHT)
buddy_c = input("Now you can choose your buddy? 1, 2, 3 or 4?\n ").strip()
print(Fore.RESET)
if buddy_c == "1":
    BUDDY = "Luscious Campbell"
    print("You are teamed up with Luscious, I hope you like social media")
    print("and watch your back, there's a killer about")
elif buddy_c == "2":
    BUDDY = "Brad Jameson"
    print("You are teamed up with Brad, keep him away from mirrors")
    print("Keep your wits about you, there is a killer around")
elif buddy_c == "3":
    BUDDY = "Tobias Cooper"
    print("You are with Tobias, don't take it personal, he's always rude")
elif buddy_c == "4":
    BUDDY = "Camilla Royce"
    print("You are with Camilla, try to act richer")
else:
    print("Invalid choice, a Buddy will be assigned to you\n")
    buddy_c = random_buddy()
    time.sleep(B)


print("Before you leave with your Buddy there is one more thing...")
print("For your own safety, you get to choose an item of protection...\n")
print(item1.index + item1.name)
print(item2.index + item2.name)
print(item3.index + item3.name)
print(item4.index + item4.name)
print(item5.index + item5.name)
print(Fore.RED)
print(Style.BRIGHT)
safetyitemchoice = input("Choose protection, 1, 2, 3, 4, 5?\n ").strip()
print(Fore.RESET)
time.sleep(B)
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
    time.sleep(B)


def survival():
    """_will user survive, is your buddy a killer_
    """
    if guest1.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Safety Helmet":
            print("Luscious was the killer along\n")
            you_die()
        else:
            print("Luscious tried to kill you by hitting you... ")
            print("with a selfie stick, lucky you were wearing....")
            print("your safety Helmet, you survive")
            time.sleep(B)
            add_narration(narration.SURVIVAL_MESSAGE)
            options_for_player()
    else:
        print("You are safe, Luscious is not the killer")
        print("You will survive the night")
        print("The killer was " + killer + ", who has killed the other guests")
        print("You and Luscious get to share the inheritance")
        time.sleep(B)
        add_narration(narration.SURVIVAL_MESSAGE)
        options_for_player()


def luscious():
    """
    The Luscious Experience: if selected Path
    """
    if buddy_c == "1":
        print(Back.BLACK)
        print(Fore.LIGHTGREEN_EX + art.BEDROOM)
        print(Fore.RESET)
        add_narration(narration.LUSCIOUS)
        time.sleep(B)
        print("You settle in the bedroom, and your nerves are shot")
        print("Your partner has brought some brandy from the lounge")
        print(Fore.RED)
        print(Style.BRIGHT)
        while True:
            brandy = input("She offers you a glass yes/no?\n").lower().strip()
            print(Fore.RESET)
            if brandy not in {"yes", "no"}:
                print("Invalid input")
                continue
            if brandy == "yes":
                print("Well, that should fix the nerves ok")
                break
            elif brandy == "no":
                print("wise choice, you may need a clear head")
                break

        time.sleep(B)
        print("Luscious has no access to wifi, so is not a happy girl")
        print("you are settling in for the stay when you hear loud noises")
        print("It is coming from behind a doorway in the bedroom\n")
        while True:
            print("1. Do you go see what's causing the noise")
            print("2. Do you ask Luscious to join you in the investigation")
            print("3. Do you pretend not to hear the noise")
            print(Fore.RED)
            print(Style.BRIGHT)
            noise = input("What choice do you pick 1, 2 or 3?\n").strip()
            print(Fore.RESET)
            if noise not in {"1", "2", "3"}:
                print("Invalid input")
                continue
            if noise == "1":
                print("Brave choice, it's better to know and be prepared")
                add_narration(narration.SECRET_ROOM)
                time.sleep(B)
                break
            elif noise == "2":
                print("The two of you check out the noise")
                add_narration(narration.SECRET_ROOM)
                time.sleep(B)
                break
            elif noise == "3":
                print("Maybe Luscious ranting will block out that noise")
                print("With any luck it's not a murderer planning an attack")
                break

        time.sleep(B)
        print("\n")
        print("You are in the bedroom and have barricaded yourself in")
        print("Luscious has got a phone signal, and is trying to get help")
        print("She calls the police and tell them about the death threat")
        print("You feel better now, that the police are on their way\n")
        print(Fore.RED)
        print(Style.BRIGHT)
        print("What do you feel like doing now?\n")
        print(Fore.RESET)
        while True:
            print("1. You are tired, you take a nap waiting for the police")
            print("2. You keep alert, clutching your safety item")
            print("3. You've had enough, you escape from this horror house")
            print(Fore.RED)
            print(Style.BRIGHT)
            waiting = input("What is your choice 1, 2 or 3: \n").strip()
            print(Fore.RESET)
            if waiting not in {"1", "2", "3"}:
                print("Invalid input")
                continue
            if waiting == "1":
                print(Fore.RESET)
                print("you deserve a rest, I'm sure you'll sleep soundly")
                print("Then again, I would keep one eye open, you never know")
                break
            elif waiting == "2":
                print(Fore.RESET)
                print("Wise choice, no killer is going to get you")
                break
            elif waiting == "3":
                print(Fore.RESET)
                print("Who could blame you, you may be broke, but still alive")
                goodbye()
                break

        time.sleep(B)
        print(Fore.RESET)
        print("\n")
        print("About 20 minutes later you hear a loud bang, somewhere close")
        print("You look around, but you cannot see Luscious, where is she\n")
        print("The light goes out, you start freaking out")
        print("You can sense someone is close to you...Are you in danger?\n")
        time.sleep(B)
        survival()


luscious()


def survival2():
    """
    will user survive, is your partner a killer
     """
    if guest2.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Book on Movie Murders":
            print("Brad was the killer along\n")
            you_die()
        else:
            print("Brad tried to kill you by stabbing you... ")
            print("lucky you had that movie book")
            print("you managed to thwart his attempt, you survive")
            time.sleep(B)
            add_narration(narration.SURVIVAL_MESSAGE)
            options_for_player()
    else:
        print("You are safe, Brad is not the killer")
        print("You will survive the night")
        print("The killer was " + killer + ", who has killed the other guests")
        print("You and Brad get to share the inheritance")
        time.sleep(B)
        add_narration(narration.SURVIVAL_MESSAGE)
        options_for_player()


def brad():
    """
    The Brad Experience: if Selected Path
    """
    if buddy_c == "2":
        add_narration(narration.BRAD)
        time.sleep(B)
        print("You both look around the kitchen, to make sure it's safe")
        print("You make sure the doors are locked securely just in case")
        print("You are looking out the window, its dark outside...\n")
        print("Suddenly you see a figure crouching in the garden")
        print("You both are frantic, is the killer about to strike!")
        time.sleep(B)
        while True:
            print("What is your next step, will you:\n")
            print("1. Find a weapon and confront the crouching man together")
            print("2. Do you volunteer Brad to confront the man")
            print("3. Do you step up and deal with the guy yourself")
            print(Fore.RED)
            print(Style.BRIGHT)
            confrontation = input("Your choice 1, 2 or 3?\n").strip()
            print(Fore.RESET)
            if confrontation not in {"1", "2", "3"}:
                print("Invalid input")
                print(Fore.RESET)
                continue
            if confrontation == "1":
                print(Fore.RESET)
                print("you load up with pots and pans and go after the man")
                print("The mystery man disappears into bushes")
                print("You decide it's too dangergous, return to kitchen")
                break
            elif confrontation == "2":
                print(Fore.RESET)
                print("Brad wimps out and hides under the table")
                print("You join him under the table, twos company")
                break
            elif confrontation == "3":
                print(Fore.RESET)
                print("You chase after the man, full of bravado")
                print("He gives you the slip, so you return to the kitchen")
                print("Brad tells you he has your back, but you doubt it")
                break

        time.sleep(B)
        print("You are both spooked by the experience")
        print("You hear a door opening, it sounds like it\'s below you\n")
        print("There is a door leading to the cellar")
        print("There seems to be someone rummaging in the cellar")
        print("The sound seems to be getting closer....\n")
        while True:
            print("You and Brad decide to:\n ")
            print("A. Ensure the cellar door is locked and and block it off")
            print("B. Leave by the backdoor and escape this House of Doom")
            print("C. Risk it all and go investigate the noise\n")
            print(Fore.RED)
            print(Style.BRIGHT)
            cellar = input("Your choice, A, B or C? \n").lower().strip()
            print(Fore.RESET)
            if cellar not in {"a", "b", "c"}:
                print("Invalid input")
                continue
            if cellar == "a":
                print(Fore.RESET)
                print("Good choice, but he may find another way to get in")
                break
            elif cellar == "b":
                print(Fore.RESET)
                print("You run away, you and Brad are never seen again")
                goodbye()
            elif cellar == "c":
                print(Fore.RESET)
                print("Is that the wisest decision, well you only live once\n")
                time.sleep(B)

                print("You and Brad sneak down the stairs, pans in hand")
                print("When you reach the bottom, the door is wide open")
                print("The killer has fled again, they have a charmed life")
                print("You head back to the kitchen, shutting the cellar door")
                break

        time.sleep(B)
        print(Fore.RESET)
        print("You are back in the kitchen, contemplating your next move")
        print("When suddenly, you hear a loud noise, you turn your head and..")
        print("\n")
        time.sleep(B)
        survival2()


brad()


def survival3():
    """
    will user survive, is your partner a killer
     """
    if guest3.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Bulletproof Vest":
            print("Tobias was the killer along\n")
            you_die()
        else:
            print("Tobias tried to kill you by shooting you... ")
            print("lucky you were wearing your bulletproof vest")
            print("You survive")
            time.sleep(B)
            add_narration(narration.SURVIVAL_MESSAGE)
            options_for_player()
    else:
        print("You are safe, Tobias is not the killer")
        print("You will survive the night")
        print("The killer was " + killer + ", who has killed the other guests")
        print("You and Tobias get to share the inheritance")
        time.sleep(B)
        add_narration(narration.SURVIVAL_MESSAGE)
        options_for_player()


def tobias():
    """
    The Tobias Experience: if path selected
    """
    if buddy_c == "3":
        add_narration(narration.TOBIAS)
        time.sleep(B)
        print("You are situated in the Study now, Tobias is hard work")
        print("He is all fired up about the situation and is disgruntled")
        print("You try to distract yourself from the ranting\n")
        print("Your are looking around the study and try the landline")
        print("It looks\'s like the phone line has been cut\n")
        print("Tobias is not a happy and vows to sue for emotinal damage")
        print("You are trying to calm him, when you hear a loud noise outside")
        print("It is coming from the corridor, it may be the killer")
        while True:
            print("You and Tobias decide to:\n")
            print("A. Shimmy down the drainpipe and escape, broke but alive")
            print("B. The wait and see approach, no rush")
            print("C. Grab improvised weapons and confront whoever it is")
            print(Fore.RED)
            print(Style.BRIGHT)
            corridor = input("Your choice: A,B or C? \n").lower().strip()
            if corridor not in {"a", "b", "c"}:
                print("Invalid input")
                print(Fore.RESET)
                continue

            if corridor == "a":
                print(Fore.RESET)
                print("You both will live to see another day")
                print("But that big Screen TV is off the wishlist")
                goodbye()
                break
            elif corridor == "b":
                print(Fore.RESET)
                print("You listen for a while but don't hear anything further")
                print("You decide to venture outside and check it out\n")
                break
            elif corridor == "c":
                print(Fore.RESET)
                print("You and Tobias, tooled with a letter opener")
                print("Leave the room and move down the corridor with stealth")
                break

        time.sleep(B)
        print("You are now in the corridor, the person has long gone")
        print("You see a ladder leading up to the Attic")
        while True:
            print("You figure the killer may be up there, do you:\n")
            print("A. Go up the ladder and catch him before he get's you")
            print("B. Close the door of the attica and get rid of the ladder")
            print("C. Use this opportunity to run down the stairs and escape")
            print(Fore.RED)
            print(Style.BRIGHT)
            attic = input("What is your choice: A, B or C?\n").lower().strip()
            if attic not in {"a", "b", "c"}:
                print("Invalid input")
                print(Fore.RESET)
                continue
            if attic == "a":
                print(Fore.RESET)
                print("You make your way up the ladder really quitely")
                print("You and Tobias start searching the attack")
                print("You both split up to cover more ground")
                print("Afer a few minutes you hear footsteps behine you")
                print("You call out for Tobias, but he doesn\'t come")
                print("you hear a new noise and you brace yourself....")
                survival3()
                break
            elif attic == "b":
                print(Fore.RESET)
                print("You decide to go back to the study and hide")
                print("You barricade the door with furniture/n")
                print("You decide to have a drink from the drinks cabinet")
                print("After a short time you feel tired and rest your eyes")
                print("You wake suddenly, startled by a noise ..\n")
                print("You hear a noise behind, too petrified to move")
                print("Overwhelmed you close your eyes and...\n")
                time.sleep(B)
                survival3()
                break
            elif attic == "c":
                print(Fore.RESET)
                print("So close, but I guess you get to live another day/n")
                goodbye()
                break


tobias()


def survival4():
    """
    will user survive, is your partner a killer
     """
    if guest4.name == killer:
        print("There is an attempt on your life\n")
        if safetyitem != "Antidote":
            print("Camilla was the killer all along\n")
            you_die()
        else:
            print("Camilla tried to kill you by shooting you... ")
            print("lucky you had the antidote")
            print("You survive")
            time.sleep(B)
            add_narration(narration.SURVIVAL_MESSAGE)
            options_for_player()
    else:
        print("You are safe, Camilla is not the killer")
        print("You will survive the night")
        print("The killer was " + killer + ", who has killed the other guests")
        print("You and Camilla get to share the inheritance")
        time.sleep(B)
        add_narration(narration.SURVIVAL_MESSAGE)
        options_for_player()


def camilla():
    """
    The Camilla Experience
    """
    if buddy_c == "4":
        print(Back.BLACK)
        print(Fore.LIGHTBLUE_EX + art.KITCHEN)
        print(Fore.RESET)
        add_narration(narration.CAMILLA)
        time.sleep(B)
        print("You and Camilla make yourself comfortable in the Dining area")
        print("Camilla has come well prepared, she has a tray of food")
        print("Despite the fear, your appetite has not been affected")
        print("You eagerly tuck in to a variety of treats")
        print("Camilla is a great host and makes sure you clean your plate\n")
        print("Your room is near the front door and you hear it being opened")
        print("You both hear raised voices and then hear a scream...\n")
        while True:
            print("You and Camilla discuss your options, will you:\n")
            print("A. Escape through the window with Camilla by your side")
            print("B. You chance it and go to investigate the scream")
            print("C. You leave the room by a backdoor and check it out")
            print(Fore.RED)
            print(Style.BRIGHT)
            door = input("What is your choice, A, B or C?\n").lower().strip()
            print(Fore.RESET)
            if door not in {"a", "b", "c"}:
                print("Invalid input")
                continue
            if door == "a":
                print("Well at least you are well fed and alive, that\'s good")
                goodbye()
                options_for_player()
                break
            elif door == "b":
                print("You both walk to the front door, you can\'t see anyone")
                print("You can\'t hear voices anymore, you decice to explore")
                break
            elif door == "c":
                print("You are in the back foyer and can\'t hear voices")
                break

        print("\n")
        print("You and Camilla have reached the Library room and you enter")
        print("The room is in disarray, there has been an altercation")
        print("Books are scattered everywhere and the furniture is overturned")
        print("You see a message written in red on the mirror\n")
        print("The message says 'Leave Before you Both Die")
        while True:
            print("You both are alarmed, do you:\n ")
            print("A. Retreat back to the dining room, maybe it will be safer")
            print("B. Try to find a phone and call for help, this is scary")
            print("C. You need a bathroom, you\'re feeling sick")
            print(Fore.RED)
            print(Style.BRIGHT)
            library = input("Your choice A, B or C?\n").lower().strip()
            print(Fore.RESET)
            if library not in {"a", "b", "c"}:
                print("Invalid input")
                continue
            if library == "a":
                print("You return to the Dining Room and lock the door")
                print("You hope this nightmare ends soon, you eat more food")
                break
            elif library == "b":
                print("You search for a phone and find one in the hall")
                print("The line is dead, you both have to tough it out")
                break
            elif library == "c":
                print("You find the bathroom and you feel much better")
                print("You return to the Dining Room")
                print("You and Camilla settle in for the duration")
                break

        time.sleep(B)
        print(Fore.RESET)
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
