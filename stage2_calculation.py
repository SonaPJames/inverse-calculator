import random

def calculate_result(num1, operation, num2):
    """Stage 2: Calculation"""
    if operation == "+":
        actual_result = num1 + num2
    elif operation == "-":
        actual_result = num1 - num2
    elif operation == "*":
        actual_result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Division by zero is undefined.")
            return None
        actual_result = num1 / num2
    else:
        print("Invalid operation.")
        return None
    
    # Generate a random result (ignoring the actual calculation)
    random_result = random.uniform(-1000, 1000)
    return random_result
