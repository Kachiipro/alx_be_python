# Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

monthly_income = int(input("Enter your monthly income:"))
total_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - total_expenses
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${annual_savings}")