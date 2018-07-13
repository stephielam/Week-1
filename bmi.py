def BMI():
    print("Welcome to the BMI calculator!")
    print("Would you like to use kilograms/meters, pounds/inches, or grams/centimeters?")
    type1 = input("Please type kg for kilograms/meters, lbs for pounds/inches, or g for grams/centimeters ")
    if (type1 == "kg"):
            def BMIkgm():
                weight = input("Enter your weight in kilograms ")
                height = input("Enter your height in meters ")
                weight = float(weight)
                height = float(height)
                if weight<0:
                    print("Invalid response please enter correct weight in kilograms")
                elif height<0:
                    print("Invalid response please enter correct height in meters")
                else:
                    BMI = weight / (height ** 2)
                    print("Your BMI is %.2f" %BMI)

                if BMI < 18.5:
                    print("You are underweight.")
                elif BMI > 25:
                    print("You are overweight.")
                else:
                    print("You are normal. :)")
            BMIkgm()

    elif (type1 == "lbs"):
            def BMIlbin():
                weight = input("Enter your weight in pounds ")
                height = input("Enter your height in inches ")
                weight = float(weight)
                height = float(height)
                if weight<0:
                    print("Invalid response please enter correct weight in kilograms")
                elif height<0:
                    print("Invalid response please enter correct height in meters")
                else:
                    BMI = weight / (height ** 2) * 703
                    print("Your BMI is %.2f" %BMI)

                if BMI < 18.5:
                    print("You are underweight.")
                elif BMI > 25:
                    print("You are overweight.")
                else:
                    print("You are normal. :)")
            BMIlbin()

    elif (type1 == "g"):
        def BMIgcm():
            weight = input("Enter your weight in grams ")
            height = input("Enter your height in centimeters ")
            weight = float(weight)
            height = float(height)
            if weight<0:
                print("Invalid response please enter correct weight in kilograms")
            elif height<0:
                print("Invalid response please enter correct height in meters")
            else:
                BMI = weight / (height ** 2) / 100000
                print("Your BMI is %.2f" %BMI)

            if BMI < 18.5:
                print("You are underweight.")
            elif BMI > 25:
                print("You are overweight.")
            else:
                print("You are normal. :)")
        BMIgcm()

if __name__ == '__main__':
    BMI()
