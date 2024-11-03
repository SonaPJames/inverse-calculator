def display_result(num1, operation, num2, result):
    """Stage 3: Output"""
    if result is not None:
        print(f"The random result for {{num1}} {{operation}} {{num2}} is: {{result}}")
    else:
        print("No result to display due to an error.")

def random_calculator():
    num1, operation, num2 = get_user_input()
    if num1 is not None and operation is not None and num2 is not None:
        result = calculate_result(num1, operation, num2)
        display_result(num1, operation, num2, result)

# Run the calculator
random_calculator()
