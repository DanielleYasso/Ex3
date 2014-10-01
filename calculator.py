import arithmetic

def do_math():
    while True:
        user_input = raw_input("> ").strip()
        if user_input == "q":
            break

        # separate user input 
        input_list = user_input.split()

        # determine math function to be called and check for errors
        if len(input_list) == 1 or len(input_list) == 2:
            if input_list[0] in ["+", "-", "*", "/", "pow", "mod"]:
                print "Oops! You need to give us more numbers! Try again."
            elif len(input_list) == 1 and input_list[0] in ["square", "cube"]:
                print "Oops!  You need to give us 1  number! Try again."
            elif len(input_list) == 2 and input_list[0] in ["square", "cube"]:
                # convert user input values to integers for math
                second = int(input_list[1])
                if  input_list[0] == "square":
                    print arithmetic.square(second)
                elif input_list[0] == "cube":
                    print arithmetic.cube(second)
            else:
                print "I don't understand what math operation you want me to do. Try again."

        elif len(input_list) >= 3:
            # convert user input values to integers for math
            second, third = int(input_list[1]), int(input_list[2])

            if input_list[0] == "+":
                print arithmetic.add(input_list[1:])
            elif input_list[0] == "-":
                print arithmetic.subtract(input_list[1:])
            elif input_list[0] == "*":
                print arithmetic.multiply(input_list[1:])
            elif input_list[0] == "/":
                print arithmetic.divide(input_list[1:])
            elif input_list[0] in ["square", "cube"]:
                print "Oops! You gave us too many numbers!  Just give 1. Try again."
            elif input_list[0] in ["pow", "mod"]:
                # error check for too many numbers
                if len(input_list) == 3:
                    if input_list[0] == "pow":
                        print arithmetic.power(second, third)
                    elif input_list[0] == "mod":
                        print arithmetic.mod(second, third)
                else:
                    print "Oops! You gave us too many numbers!  Just give 2. Try again."
            else:
                print "I don't understand what kind of math you want me to do."
        else:
            print "I don't understand.  You said too much.  Talk less."

def main():

    do_math()


if __name__ == '__main__':
    main()
