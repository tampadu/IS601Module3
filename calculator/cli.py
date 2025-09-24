from calculator.operations import add, subtract, multiply, divide

def getNumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    print("Welcome to the IS601 Command Line Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    
    while True:
        operation = input("Enter operation (or 'quit' to exit): ").strip().lower()
        if operation == "quit":
            print("Goodbye!")
            break
        
        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            continue
        
        a = getNumber("Enter first number: ")
        b = getNumber("Enter second number: ")

        try:
            result = {
                "add": add,
                "subtract": subtract,
                "multiply": multiply,
                "divide": divide
            }[operation](a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
