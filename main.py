from django.db.models.expressions import result

num1 = float(input("Enter first number : "))
operator = input("chose operator (+, -, *, /): ")
num2  = float(input("Enter a second number: "))

if operator == "+":
    result = num1 + num2
    print(f"the result is {result}")
elif operator == "-":
    result = num1 - num2
    print(f" the result is {result}")
elif operator == "*":
    result = num1 * num2
    print(f" the result is {result}")
elif operator == "/":
    result = num1/num2
    print(f" the result is {result}")
else:
    print(f"Enter a valid input")
