def greet(name):
    print("Hello,", name)
# This function takes a name as an argument and prints a greeting message.
# if name begins with Miss or Mrs print "Welcome, esteemed Madam!"
name = input("Enter your name: ")
if name.startswith("Miss") or name.startswith("Mrs"):
    print("Welcome, esteemed Madam!")   
elif name.startswith("Sir"):
    print("Welcome, Sir!")
else:
    print("Welcome, dear guest!")
# This code prompts the user for their name and greets them accordingly.
# Call the greet function with the provided name
greet(name)

# function to add to numbers
def add_numbers(a, b):
    return a + b
# This function takes two numbers and returns their sum.
# Example usage of add_numbers function
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = add_numbers(num1, num2)
print("The sum is:", result)

#function return the bigger number
def bigger_number(a, b):
    if a > b:
        return a
    else:
        return b
# This function takes two numbers and returns the bigger one.
# Example usage of bigger_number function
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
bigger = bigger_number(num1, num2)
print("The bigger number is:", bigger)