def get_user_input():
    """Stage 1: Input"""
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        return num1, operation, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None
