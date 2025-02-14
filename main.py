from cgitb import reset

num1 = float(input("Enter the first  number: "))
operator = input("enter an operator (+ - * / ): ")
num2 = float(input("enter the second number: "))

if operator == "+":
    result = num1+num2
    print(f"result is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"result is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"result is {round(result)}")
elif operator == "/":
    result = num1 / num2
    print(f"result is {round(result, 3)}")
else:
    print("please chose an operator: ")
