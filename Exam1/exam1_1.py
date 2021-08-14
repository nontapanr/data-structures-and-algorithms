print(" *** BMI ***")

wg, hg = input("Enter your weight(kg) and height(m) : ").split()
wg = float(wg)
hg = float(hg)

bmi = wg/(hg*hg)

if bmi < 18.5:
    print("Your status is : Below normal weight.")
elif 18.5 <= bmi < 25:
    print("Your status is : Normal weight.")
elif 25 <= bmi < 30:
    print("Your status is : Overweight.")
elif 30 <= bmi < 35:
    print("Your status is : Case I Obesity.")
elif 35 <= bmi < 40:
    print("Your status is : Case II Obesity.")
elif bmi >= 40:
    print("Your status is : Case III Obesity.")
