"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

def square(i):
    return i*i

def cube(i):
    return i**3

def mod(i, j):
    return i % j

def power(i, j):
    return i**j

def main():

    while True:
        userInput = raw_input("> ")
        if userInput == "q":
            break

        # separate user input 
        userInput = userInput.split()
        
        # convert user input values to integers for math
        userInput[1] = int(userInput[1])
        if len(userInput) == 3:
            userInput[2] = int(userInput[2])

        # determine math function to be called
        if userInput[0] == "+":
            print add(userInput[1], userInput[2])
        elif userInput[0] == "-":
            print subtract(userInput[1], userInput[2])
        elif userInput[0] == "*":
            print multiply(userInput[1], userInput[2])
        elif userInput[0] == "/":
            print divide(userInput[1], userInput[2])
        elif userInput[0] == "square":
            print square(userInput[1])
        elif userInput[0] == "cube":
            print cube(userInput[1])
        elif userInput[0] == "pow":
            print power(userInput[1], userInput[2])
        elif userInput[0] == "mod":
            print mod(userInput[1], userInput[2])
        else:
            print "I don't understand."


if __name__ == '__main__':
    main()
