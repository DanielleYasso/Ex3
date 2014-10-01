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

def doMath():
    while True:
        userInput = raw_input("> ")
        if userInput == "q":
            break

        # separate user input 
        userInput = userInput.split()

        # determine math function to be called and check for errors
        if len(userInput) == 1:
            if userInput[0] in ["+", "-", "*", "/", "pow", "mod", "square", "cube"]:
                print "Oops!  You need to tell us more than just that! Try again."
            else:
                print "I don't understand."

        elif len(userInput) == 2:
            # convert user input values to integers for math
            userInput[1] = int(userInput[1])

            if userInput[0] in ["+", "-", "*", "/", "pow", "mod"]:
                print "Oops! You need to give us 2 numbers! Try again."
            elif userInput[0] == "square":
                print square(userInput[1])
            elif userInput[0] == "cube":
                print cube(userInput[1])
            else:
                print "I don't understand."

        elif len(userInput) == 3:
            # convert user input values to integers for math
            userInput[1], userInput[2] = int(userInput[1]), int(userInput[2])

            if userInput[0] == "+":
                print add(userInput[1], userInput[2])
            elif userInput[0] == "-":
                print subtract(userInput[1], userInput[2])
            elif userInput[0] == "*":
                print multiply(userInput[1], userInput[2])
            elif userInput[0] == "/":
                print divide(userInput[1], userInput[2])
            elif userInput[0] in ["square", "cube"]:
                print "Oops! You gave us too many numbers!  Just give 1. Try again."
            elif userInput[0] == "pow":
                print power(userInput[1], userInput[2])
            elif userInput[0] == "mod":
                print mod(userInput[1], userInput[2])
            else:
                print "I don't understand."
        else:
            print "I don't understand.  You said too much.  Talk less."

def main():

    doMath()


if __name__ == '__main__':
    main()
