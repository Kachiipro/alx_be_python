# This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division).

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation( + , - , * , / ):")

match operation:

    case "+":
        sum = num1 + num2
        print(f"The result is {sum}.")
    case "-":
        difference = num1 - num2
        print(f"The result is {difference}.")
    case "*":
        product = num1 + num2
        print(f"The result is {product}.")
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            quotient = num1 / num2
            print(f"The result is {quotient}")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")
