def add(new_list):
    total = 0
    for value in new_list:
        number = int(value)
        total += number
    return total

def subtract(new_list):
    total = int(new_list[0])
    for value in new_list[1:]:
        number = int(value)
        total -= number
    return total

def multiply(new_list):
    total = int(new_list[0])
    for value in new_list[1:]:
        number = int(value)
        total *= number
    return total

def divide(new_list):
    total = int(new_list[0])
    for value in new_list[1:]:
        number = int(value)
        total /= number
    return total

def square(i):
    return i*i

def cube(i):
    return i**3

def mod(i, j):
    return i % j

def power(i, j):
    return i**j

