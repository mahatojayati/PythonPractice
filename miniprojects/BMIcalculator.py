# A BMI calculator that calculates the BMI based on user input.
# It also provides a classification based on the BMI value.
def person_details(age, height, weight):
    bmi = weight / (height ** 2)
    print("Your BMI is:" + str(round(bmi, 2)))
    
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
    return bmi
def main():
    print("Welcome to the BMI Calculator!")
    
    try:
        age = int(input("Enter your age: "))
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        
        if height <= 0 or weight <= 0:
            print("Height and weight must be positive numbers.")
            return
        
        person_details(age, height, weight)
    except ValueError:
        print("Invalid input. Please enter numeric values for age, height, and weight.")
if __name__ == "__main__":
    main()
# This code defines a simple BMI calculator that takes user input for age, height, and weight
