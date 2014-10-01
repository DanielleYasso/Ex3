import arithmetic

def do_math():
    while True:
        user_input = raw_input("> ").strip()
        if user_input == "q":
            break

        # separate user input 
        input_list = user_input.split()

        # determine math function to be called and check for errors
        if len(input_list) == 1:
            if input_list[0] in ["+", "-", "*", "/", "pow", "mod", "square", "cube"]:
                print "Oops!  You need to tell us more than just that! Try again."
            else:
                print "I don't understand."

        elif len(input_list) == 2:
            # convert user input values to integers for math
            second = int(input_list[1])

            if input_list[0] in ["+", "-", "*", "/", "pow", "mod"]:
                print "Oops! You need to give us 2 numbers! Try again."
            elif input_list[0] == "square":
                print arithmetic.square(second)
            elif input_list[0] == "cube":
                print arithmetic.cube(second)
            else:
                print "I don't understand."

        elif len(input_list) == 3:
            # convert user input values to integers for math
            second, third = int(input_list[1]), int(input_list[2])

            if input_list[0] == "+":
                print arithmetic.add(second, third)
            elif input_list[0] == "-":
                print arithmetic.subtract(second, third)
            elif input_list[0] == "*":
                print arithmetic.multiply(second, third)
            elif input_list[0] == "/":
                print arithmetic.divide(second, third)
            elif input_list[0] in ["square", "cube"]:
                print "Oops! You gave us too many numbers!  Just give 1. Try again."
            elif input_list[0] == "pow":
                print arithmetic.power(second, third)
            elif input_list[0] == "mod":
                print arithmetic.mod(second, third)
            else:
                print "I don't understand."
        else:
            print "I don't understand.  You said too much.  Talk less."

def main():

    do_math()


if __name__ == '__main__':
    main()
