def calculate_bmi(height, weight): 
    print("Height = " + str(height) + " m")
    print("Weight = " + str(weight) + " kg")

    #calculating bmi 
    bmi = weight / (height * height)
    #displaying calculated bmi
    print("BMI = " + str(bmi))

    #bmi < 18.5 is underweight
    #bmi between 18.5 & 25.0 is normal weight
    #bmi >25.0 is overweight 
    if bmi < 18.5: 
        print("underweight:(")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("normal weight:)")
        return 0
    else:
        print("overweight:(")
        return 1

calculate_bmi(weight=57, height=1.73)
