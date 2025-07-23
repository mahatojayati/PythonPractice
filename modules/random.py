'''import random as ran
import math as meh
number = ran.randint(1,10)
print("Rolling a dice...")
if(number >=5):
    print(":)")
    print("The dice roll is:", number)
elif(number <= 4):
    print(":(")
    print("The dice roll is:", number)
elif(number >= 7):
    print("Unexpected outcome")  '''  

# This code snippet is intended to demonstrate the use of a random number generator
import math as meh
sq = meh.sqrt(15)
print("The square root of 15 is:", sq)
pow = meh.pow(2, 3)
print("2 raised to the power of 3 is:", pow)

import random as ran
songs = ["All of Me", "Shape of You", "Someone Like You", "Rolling in the Deep"]
print("Randomly selected song:", ran.choice(songs))
