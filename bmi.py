def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    calcbmi = weight/(height*height)
    print("BMI: " + str(calcbmi))

    if calcbmi <18.5:
        print("Underweight")
    elif calcbmi >= 18.5 and calcbmi <=25.0:
        print("Normal Weight")
    else:
        print("Overweight")

calculate_bmi(weight=120, height=1.84)