def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiplication(x, y):
    return x*y

if __name__ == "__main__":
    print("Simple Calculator App")
    
    try:
        num1 = int(input("Enter the first number: "))
        operation = input("Enter operation (+ for addition, - for subtraction, * for multiplication): ")
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit(1)

    

    if operation == "+":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = multiplication(num1, num2)
        print(f"{num1} * {num2} = {result}")    
    else:
        print("Invalid operation. Please enter + for addition or - for subtraction.")