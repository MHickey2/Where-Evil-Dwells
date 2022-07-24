import time
import pyfiglet

A = 2
B = 0.2
C = 0.08

word = pyfiglet.figlet_format(" WHERE  EVIL   DWELLS")
print(word)
response = input("Would you like to have an encounter with Evil? ")
if response.lower().strip() == "yes":
    print("welcome to the Game, let's hope you make it")
    start = True
elif response.lower().strip() == "no":
    print("understandable, sorry to see you go")
    start = False
else:
    print("That is not a valid response")
    start = False
if start is True:
    time.sleep(A)
    print("You are invited to a reading of a Will at Harland Manor")
    print("an old house steeped in mystery..")
    print("With a long history of murder and debauchery")
    print("It is in relation to your great uncle Raymon DeCharles")
    print("It is a frightening prospect, but you really need the money")
    rsvp = input("the question is do you accept the invite? yes/no ")
if rsvp.lower().strip() == "yes":
    print("Great, I see a hot-tub and Big Screen TV in your future")
    rsvp = True
    with open('arrival.txt') as f:
        contents = f.read()
    print(contents)
elif rsvp.lower().strip() == "no":
    print("Well I guess it is instant noodles for you")
    rsvp = False
else:
    print("let's try that again, shall we")
    print("the question is do you accept the invite? yes/no ")
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
def path1():
    print("A. Remember moderation is key, let's wait for the other guests")
    time.sleep(A)
def path2():
    print("B. Leave some food for the other guests, let's wait for them")
    time.sleep(A)
def path3():
    print("C. Great choice, take a canopy for the road, the adventure begins")
    time.sleep(A)
def path4():
    print("D. What no food or drink, let's wait for the other guests")
    time.sleep(A)
print("You are now in the lounge, so what's the plan?")
print("A. Make a start on the booze and work your way through the spirits")
print("B. Fill your pockets with canopies and the smoked salmon entrees")
print("C. Decide to explore a little, when you will get this change again")
print("D. Wait for the other guests to arrive")
lounge = input("What is your pick,  A, B, C or D? ")
if lounge == "A":
    path1()
elif lounge == "B":
    path2()
elif lounge == "C":
    path3()
elif lounge == "D":
    path4()
else:
    print("I guess you're here now anyway, best wait for the other guests")
staircase = input("You sneak out and get to the staircase, up or down?/n ")
if staircase == "down":
    print("you are going down a creepy dark staircase to the cellar")
    print("1. A battered door, it that maniacal laughter you hear?")
    print("2. A pristine door in mint codition, with soothing music within")
    print("3. A solid oak door, with a stange tapping sound from within")
doorchoice = input("Which door do you pick to explore, 1, 2 or 3? ")
if doorchoice == "1":
    print(" you enter the room..only to see a caged macaw laughing")
    print("Feels cold down here and am hungry again, back to the lounge")
elif doorchoice == "2":
    print(" oh, no, you'been caught by Jeeves, doing his meditation")
    print("He is furious and sends you back to the lounge, see you there")
elif doorchoice == "3":
    print("You enter the room, and are caught by an evil wrongdoer")
    print("alas the adventure has ended for you, better luck next time")
else:
    print("You're right it's not work the risk, get back tot he lounge")
    print("I'll help you decide, let's go down, no worries")
if staircase == "up":
    print("You are going up to the bedroom area, it's well lit")
    print("At the top of the stairs you see a figure skulking on the landing")
print("1. You follow him, he looks suspicious, and you are curious")
print("2. You get scared and decide to return to the lounge")
print("3. You ignore the skulking person and continue skulking")
stranger = input("What do you do next, 1,2 or 3? ")
if stranger == "1":
    print("You stalk the stalker, like a ninja")
    print("right until, he turns around and puts you in a headlock")
    print("Sorry the Stalker caught you, better luck next time")
elif stranger == "2":
    print(" Good chooice, they may be finishing off the food right now")
    print("You have a hankering for a pig in a blanket")
elif stranger == "3":
    print("There's one too maney skulkers in this house for your liking!")
else:
    print("Is that rancheros I smell, I'm in the mood for a ranchero!")