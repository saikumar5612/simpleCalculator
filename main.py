# python weight converted program

weight = float(input("enter your weight: "))
unit = input("kilograms or pounds? (k or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight in Pounds is  {weight} {unit}")
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs"
    print(f"your weight in Kilograms is {weight} {unit}")
else:
    print(f"Entered input {unit} is not valid ")

