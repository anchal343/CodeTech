def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Welcome to the simple calculator!")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of division is: {divide(num1, num2)}")
            break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

if __name__ == "__main__":
    calculator()
