print("Welcome to SimpleCalculator!")

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("SimpleCalculator can only perform the following operations: (-, +, /, *)\nType 'q' to quit the program. ");
    operation = input("Enter the operation:  ")

    if operation == "q":
        break
    elif operation == "/" and num2 == 0:
        print("Cannot divide by zero. ")
        print("Thank you for using SimpleCalculator :) ")
        exit()
    elif operation == "+":
        print(f"Result: {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1 * num2}")
    elif operation == "/":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid operation")

print("Thank you for using SimpleCalculator :) ")
