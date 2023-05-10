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