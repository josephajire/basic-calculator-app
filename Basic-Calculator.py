# Welcome Message
print("Welcome to this basic calculator developed by Joseph Ajireloja")

# Accept the first number from the user and convert it to float
# If the input from the user is not a number, show error message
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print(" Error: You are to enter a valid number for the first input.")
    exit()

# Ask the user for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Accept the second number from the user and convert it to float
# If the input from the user is not a number, show error message
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print(" Error: You are to enter a valid number for the second input.")
    exit()

# Initialize result variable to None
result = None

# Perform the operation based on the inputs from user 
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print(" Error: Division by zero is not allowed.")
else:
    print(" Error: Invalid operation! You are to enter + or - or * or / as the operation.")


# Print the result if valid operation was performed
if result is not None:
    print(f"{num1} {operation} {num2} = {result}")
