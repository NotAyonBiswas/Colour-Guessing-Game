def error_check(guess): #checks if the input is not from a defined colour palate.
    while True:
        if (str(guess)).capitalize() not in colours:
            guess= input("Please enter a valid colour.: ")
            print()
            continue
        else:
            break
    return guess

def game(guess,comp_guess): #The game unfolds! Takes user and computer input as arg.
    print()
    error_check(guess)  #Takes user input to check if input is valid or not.
    for i in range(4):
        if guess.lower()==comp_guess.lower():
            print("Yay!! You've guessed the colour successfully. The colour is", comp_guess,"\n")
            break
        elif i<=2:
            print("Unh! unh!! Not quite the colour I'm thinking over here.\n")
            guess= input(f"Take a guess, you've {(3-i)} chances left: ")
            print()
            error_check(guess)
            continue
        else:
            print("Bro, better luck next time. Btw, I was thinking about", comp_guess,"\n")
            break
    return guess, comp_guess

while True: #Main menue block
    import random as r
    print("Wellcome to the guessing game. In this game, you have to guess the right colour out of the seven colours that makes up a rainbow, i.e, Violet, Indigo, Blue, Green, Yellow, Orange, and Red. Now, to make this exciting, we can only guess four times. Excited? \nLet's begin!!\n")
    colours=["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
    game(input(f"Take a guess, you've {4} chances left: "), r.choice(colours))
    quit= input("Btw, do you want to QUIT? Press 'y' if yes or 'n' if no: ")
    print()
    if quit.lower()=='y':
        print("You've exited from the game, I'm missing you already :(\n")
        break
    else:
        continue