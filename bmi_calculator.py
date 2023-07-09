# input questions
name = input("Enter your name: ")
weight = float(input("Enter your weight: "))
unit_type = input("Kg or Lb: ")

# conversion for weight
if unit_type.lower() == "kg":
    weight = weight * 2.20462
if unit_type.lower() == "lb":
    weight = weight

# conversion for height
height = float(input("Enter your height: "))

height_type = input("Inches or Centimeters: ")

if height_type.lower() == "centimeters" or height_type.lower() == "cm":
    height = height / 2.54
if height_type.lower() == "inches":
    height = height

# BMI calculation
BMI = (weight * 703) / (height * height)
print("Your BMI is:", BMI)
if BMI > 0:
    if BMI < 18.5:
        print(name, ",you are underweight.")
    elif BMI < 24.9:
        print(name, ",you are normal weight.")
    elif BMI < 29.9:
        print(name, ",you are overweight.")
    elif BMI < 34.9:
        print(name, ",you are obese.")
    elif BMI < 39.9:
        print(name, ",you are severely obese.")
    else:
        print(name, ",you are morbidly obese.")
else:
    print("Enter valid input.")

print("Program complete.")

