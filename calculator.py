# Simple Python Calculator
# Author: Geoffrey Kikumu Kakai 
# PLP Academy – Intro to Python Assignment
# Description: A beginner-friendly calculator that performs basic arithmetic operations.

def calculator():
    print("Welcome! This is a basic calculator built by Geoffrey.")

    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Prompt user for the operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform the chosen operation
    if operation == "+":
        result = num1 + num2
        symbol = "+"
    elif operation == "-":
        result = num1 - num2
        symbol = "-"
    elif operation == "*":
        result = num1 * num2
        symbol = "*"
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        symbol = "/"
    else:
        print("Invalid operation. Please choose from +, -, *, or /.")
        return

    # Output the result
    print(f"{num1} {symbol} {num2} = {result}")

# Run the calculator
calculator()
