# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(K or L): ").strip().upper()

if unit == "K":
    result = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(result, 2)} {unit}")
elif unit == "L":
    result = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(result, 2)} {unit}")
else:
    print(f"{unit} is not a valid unit.")