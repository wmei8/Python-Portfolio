#Init
import random

#Function
a = (random.randint(1,9)) #Determines the range of the #
print("Welcome to NumberGuesser") #Introduction
for i in range(3):
    answer = int(input("Enter Number"))
    if answer == a:
        print("You got it! Congrats! ")
    if a > answer:
        print("Too low")
    if a < answer:
        print("Too High")
    if answer >= 10:
        print("1 to 9 only, you didn't unlock premium yet")
print("The final answer was")
print(a)

#Main
