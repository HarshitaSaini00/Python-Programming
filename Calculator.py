def calculator():
    print("🧮 Simple Calculator")
    
    try:
        # Input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Choose operation
        print("\nChoose the operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        operation = input("Enter your choice (+, -, *, /): ")

        # Perform operation
        if operation == '+':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("❌ Error: Division by zero is not allowed.")
        else:
            print("❌ Invalid operation selected.")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
