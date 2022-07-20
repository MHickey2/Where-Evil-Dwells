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
    elif rsvp.lower().strip() == "no":
        print("Well I guess it is instant noodles for you, sad to see you go")
    else:
        print("let's try that again, shall we")
        print("the question is do you accept the invite? yes/no ")   
        #elif rsvp == False:
         #   print("Sorry to see you go")
        #else:
         #   print("That is not a valid response")             
if rsvp  == True:
        print("I knew you'd see sense")
        with open('arrival.txt') as f:
            contents = f.readlines()
            print(contents)