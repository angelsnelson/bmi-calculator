def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)
