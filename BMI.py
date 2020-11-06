height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_squared = float(height)**2
weight_calc = int(weight)
bmi = weight_calc / height_squared

print("Your BMI is "+str(bmi))