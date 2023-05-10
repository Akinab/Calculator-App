def details ():
    Description = "Simple App Calculator"
    Date = "05-10-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def calculator():
    while True:
        try:
            print("Please choose a math operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")