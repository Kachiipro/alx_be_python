def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2   
    elif operation == "divide" and  num2 == 0:
            return "Cannot divide by zero."
    elif operation == "divide":
        return num1 / num2  
    else:
         print("Invalid operation. Please choose (add, subtract, multiply, divide):")

