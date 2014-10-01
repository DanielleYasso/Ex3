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
    userInput = raw_input("> ")

    # separate user input 
    userInput = userInput.split()

    if userInput[0] == "+":
        print "plus"
    elif userInput[0] == "-":
        pass
    elif userInput[0] == "*":
        pass
    elif userInput[0] == "/":
        pass
    elif userInput[0] == "square":
        pass
    elif userInput[0] == "cube":
        pass
    elif userInput[0] == "pow":
        pass
    elif userInput[0] == "mod":
        pass
    elif userInput[0] == "q":
        return


if __name__ == '__main__':
    main()
