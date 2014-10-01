import arithmetic

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
                print arithmetic.square(userInput[1])
            elif userInput[0] == "cube":
                print arithmetic.cube(userInput[1])
            else:
                print "I don't understand."

        elif len(userInput) == 3:
            # convert user input values to integers for math
            userInput[1], userInput[2] = int(userInput[1]), int(userInput[2])

            if userInput[0] == "+":
                print arithmetic.add(userInput[1], userInput[2])
            elif userInput[0] == "-":
                print arithmetic.subtract(userInput[1], userInput[2])
            elif userInput[0] == "*":
                print arithmetic.multiply(userInput[1], userInput[2])
            elif userInput[0] == "/":
                print arithmetic.divide(userInput[1], userInput[2])
            elif userInput[0] in ["square", "cube"]:
                print "Oops! You gave us too many numbers!  Just give 1. Try again."
            elif userInput[0] == "pow":
                print arithmetic.power(userInput[1], userInput[2])
            elif userInput[0] == "mod":
                print arithmetic.mod(userInput[1], userInput[2])
            else:
                print "I don't understand."
        else:
            print "I don't understand.  You said too much.  Talk less."

def main():

    doMath()


if __name__ == '__main__':
    main()
