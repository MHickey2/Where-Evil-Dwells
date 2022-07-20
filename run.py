import pyfiglet
word = pyfiglet.figlet_format(" WHERE  EVIL   DWELLS")
print(word)
response = input("Would you like to have an encounter with Evil?")
if response.lower().strip() == "yes":
    print("welcome to the Game, let's hope you make it")
    start = True
elif response.lower().strip() == "no":
    print("understandable, sorry to see you go")
else:
    print("That is not a valid response")
if start == True:
    print("You are invited to a reading of a Will at Harland Manor")
    print("an old house steeped in mystery..")
    print("With a long history of murder and debauchery")
    print("it is in relation to your great uncle Raymon DeCharles")
    print("It is a frightening prospect, but you really need the money")
        
rsvp = input("the question is do you accept the invite? yes/no")
if rsvp.lower().strip() == "yes":
    print("Great, I see a hottub and Big Screen TV in your future")
    rsvp = True
    with open('arrival.txt') as f:
        contents = f.readlines()
    print(contents)
elif rsvp.lower().strip() == "no":
    print("Well I guess it is instant noodles for you, sad to see you go")
    rsvp = False
else:
    print("let's try that again, shall we")
    print("the question is do you accept the invite? yes/no ")
    if rsvp == False:
        print("Sorry to see you go")
    else:
        print("That is not a valid response")
rsvp = True
if rsvp  == True:
    print("I knew you'd see sense")
    if rsvp == False:
        print("Sorry to see you go")
print("do you?...")
print("A. Make a start on the booze and work your way through to the spirits")
print("B. Fill your pockets with canopies and hog the smoked salmon entrees")
print("C. Decide to explore a little, when you will get this change again")
print("D. Wait for the other guests to arrive")
lounge = input("What is your pick,  A, B, C or D?")
if lounge == "A":
    print("A. Remember moderation is key, let's wait for the other guests")
elif lounge == "B":
    print("B. Leave some food for the other guests, let's wait for them")
elif lounge == "C":
    print("C. Great choice, take a canopy for the road, the adventure begins")
elif lounge == "D":
    print("D. What no food or drink, let's wait for the other guests")
else:
    print("I guess you're here now anyway, best wait for the other guests")