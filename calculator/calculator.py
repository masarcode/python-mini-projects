import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

def scientific_calc():
    print("Options: +, -, *, /, sqrt, log, sin, cos, quit")

    while True:
        choice = input("\Enter operation: ").lower()

        if choice == 'quit': 
            print("Exiting calculator.")
            break
        try: 
            if choice in ['sqrt', 'log', 'sin', 'cos']:
                num = float(input("Enter number: "))
                if choice == 'sqrt': print(math.sqrt(num))
                elif choice == 'log': print(math.log10(num))
                elif choice == 'sin': print(math.sin(math.radians(num)))
                elif choice == 'cos': print(math.cos(math.radians(num)))

            elif choice in ['+', '-', '*', '/']:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))

                if choice == '+': print(add(num1, num2))
                elif choice == '-': print(subtract(num1, num2))
                elif choice == '*': print(multiply(num1, num2))
                elif choice == '/': print(divide(num1, num2))
            else:
                print("Invalid input")

        except ValueError:
            print("Please enter valid numbers.")
        except ZeroDivisionError: 
            print("Cannot divide by zero.")

scientific_calc()
