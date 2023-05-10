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
            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)
            print("Result: ", result)
        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error:", e)
        else:
            while True:
                answer = input("Do you want to try again? (y/n): ")
                if answer.lower() == "n":
                    print("Thank you!")
                    return
                elif answer.lower() == "y":
                    break
                else:
                    print("Invalid answer")
                    