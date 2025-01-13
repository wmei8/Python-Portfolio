#1/7/2025
#Rock Paper Scissors

#Init
import random
wins = 0
losses = 0
ties = 0

#Function
def game():   #This the function that runs the entire game
    #Step 5
    global wins
    global losses
    global ties
    #Step 4: Loop
    while True:
     #Step 1 Obtain the Player's move
        print("Welcome to Rock, Paper, Scissors")
        move = input("What move would you like to play?")
        move = move.lower()
    #Step 2: Generate the computer's move
        move2 = random.randint(1,3)
        if move2 == 1:
            move2 = "rock"
            print("The computer's move is rock!")
        if move2 == 2:
            move2 = "scissor"
            print("The computer's move is scissor")
        if move2 == 3:
            move2 = "paper"
            print("The computer's move is paper")
         #Step 3: The outcome
        if move == "rock" and move2 == "scissor":
            print("Player win!")
            wins = wins + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "rock" and move2 == "rock":
            print("Tied!")
            ties = ties + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "rock" and move2 == "paper":
            print("Computer win!")
            losses = losses + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "scissor" and move2 == "paper":
            print("Player win!")
            wins = wins + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "scissor" and move2 == "scissor":
            print("Tied!")
            ties = ties + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "scissor" and move2 == "rock":
            print("Computer win!")
            losses = losses + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "paper" and move2 == "rock":
            print("Player win!")
            wins = wins + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "paper" and move2 == "paper":
            print("Tied!")
            ties = ties + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        if move == "paper" and move2 == "scissor":
            print("Computer win!")
            losses = losses + 1
            print("wins " + str(wins))
            print("losses " + str(losses))
            print("ties " + str(ties))
        playagain = input("Do you want to keep playing?")
        if playagain.lower() == "yes":
            print("restarting....")
        else:
            print("Thanks for playing")
            break

#Main:
game()
