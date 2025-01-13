#Multiplication Quiz Project

#Init
import random
correct = 5

#Function
def quiz(): #This function is the entire thing
    for i in range(5): #Allows the player to play 5 times
        global correct
        print("Welcome to multpication quiz!")
        level = input("Please select your difficulty level! Easy, Medium, Hard") #Determines difficulty level
        level = level.lower() #When player types EASY, the code can read.
        if level == "easy":
            integer1 = random.randint(1, 10)
            integer2 = random.randint(1, 10)
            answer = input("What is the answer of " + str(integer1) + " * " + str(integer2))
            solution = integer1*integer2
            if int(answer) == solution:
                print("Correct")
            else:
                print("Wrong")
                correct = correct - 1
        if level == "medium":
            integer3 = random.randint(10, 100)
            integer4 = random.randint(10, 100)
            answer2 = input("What is the answer of " + str(integer3) + " * " + str(integer4))
            solution2 = integer3*integer4
            if int(answer2) == solution2:
                print("Correct")
            else:
                print("Wrong")
                correct = correct - 1
        if level == "hard":
            integer5 = random.randint(100, 1000)
            integer6 = random.randint(100, 1000)
            answer3 = input("What is the answer of " + str(integer5) + " * " + str(integer6))
            solution3 = integer5*integer6
            if int(answer3) == solution3:
                print("Correct")
            else:
                print("Wrong")
                correct = correct - 1
    print("You got " + str(correct) + " out of 5 question correct!")



quiz()





#Main
