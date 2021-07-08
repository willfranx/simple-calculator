
# The first user input - float converts string into number
# Means that user HAS to put in a number
num1 = float(input("Enter first number: "))

# Next we want to get the operator
op = input("Enter operator: ")

# and the second number
num2 = float(input("Enter second number: "))

# Now we need to define our operator
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
    
# In case user inputs invalid operator
else:
    print("Invalid operator. Please use one of the following:")
    print("+ (addition), - (subtraction), / (division), or * (multiplication)")
