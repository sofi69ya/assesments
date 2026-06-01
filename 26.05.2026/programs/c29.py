def bodymassindex(height, weight):
    return round((weight / height**2),2)
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weightin kg: "))
print("Welcome to the BMI calculator. ")
bmi = bodymassindex(h, w)
print("Your BMI is: ",bmi)
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5:
    print("You are weight is normal.")
else:
    print("You are obese.")
