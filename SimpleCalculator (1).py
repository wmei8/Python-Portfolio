#Simple Calculator

#Init
#Functions
#Adds two number together
#num1 and num2 is variable of the two number they want to do the math in
def add(num1, num2): #Addition
    result = num1 + num2
    print(result)
def subtract(num1, num2): #Subtration
    result = num1 - num2
    print(result)
def multiply(num1, num2):  #Multiplication
    result = num1 * num2
    print(result)
def divide(num1, num2):   #Division
    result = num1 / num2
    print(result)

def SimpleCalculator():  #The entire simple calculator function
    print("Welcome to simple calcuator")
    while True:
        print(" ")
        print(" ")
        print(" ")
        print("Please select an operation: " )
        print("""        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Quit""")
        operation = int(input("(1-5) Option: "))
        if operation == 1:
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            add(int1, int2)
        elif operation == 2:
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            subtract(int1, int2)
        elif operation == 3:
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            multiply(int1, int2)
        elif operation == 4:
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            divide(int1, int2)
        elif operation ==5:
            print(" ")
            print("Thanks for your time in Simple Calculator")
            break


#Main:
SimpleCalculator()
