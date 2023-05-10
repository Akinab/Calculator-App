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
            choice = int(input("Enter your choice (1-4): "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError("Invalid choice")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))