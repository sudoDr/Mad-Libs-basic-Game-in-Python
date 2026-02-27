# Convert inputs to floats immediately so we can do math
num1 = float(input("Please enter the first number: "))
operator = input("Please enter the operator: ")
num2 = float(input("Please enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    # Pro-tip: Check if num2 is 0 to avoid a crash!
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Please enter a valid operator")