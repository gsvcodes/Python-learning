def main():
    print ("Welcome to the BMI Calculator!")
    height = float(input("What is your height in inches? "))
    weight = float(input("What is your weight in pounds? "))
    bmi = round((weight * 703) / (height ** 2), 2)
    print ("Your BMI is: ", bmi)
    if bmi < 18.5:
        print ("You are underweight")
    elif bmi >= 18.5 and bmi < 25:
        print ("You are normal weight")
    elif bmi >= 25 and bmi <30:
        print ("You are overweight")
    elif bmi >= 30:
        print ("You are obese")
    else:
        print ("Invalid input, please try again.")
        return()
main()
