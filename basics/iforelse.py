import random
is_raining = False
# This variable indicates whether it is raining or not.

if is_raining:
    print("Take an umbrella!")
else:
    print("Wear sunglasses!")
# This code checks if it is raining and prints a message accordingly.
# check is number is positive or negative or zero
number = random.randint(-10, 10)

if number > 0:
    print("The number is positive.", number)
elif number < 0:
    print("The number is negative.", number)
else:
    print("The number is zero.", number)
# This code checks if a number is positive, negative, or zero and prints a message accordingly
# code to check if you can drive based on age
age = random.randint(15, 30)
if age >= 18:
    print("You can drive.", age)
else:
    print("You cannot drive yet.", age)
# This code checks if a person is old enough to drive based on their age and prints a message accordingly.
