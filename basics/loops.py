import random
for i in range(5):
    print("This is iteration number", i)
# This code uses a for loop to print the iteration number from 0 to 4.
# Using a for loop to iterate through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
# This code uses a for loop to iterate through a list of fruits and print each fruit.
dict = {"apple": 1, "banana": 2, "cherry": 3}
for key, value in dict.items():
    print("Key:", key, "Value:", value)
# This code uses a for loop to iterate through a dictionary and print each key-value pair.
tup = ("apple", "banana", "cherry")
for item in tup:
    if item == "banana":
        print("Found banana!")
        continue
    if item == "cherry":
        print("Found cherry!")
        break
# This code uses a for loop to iterate through a tuple, checks for specific items, and
# prints messages accordingly. It continues to the next iteration if "banana" is found,
# and breaks the loop if "cherry" is found.
for item in range(1, 6):
    item = random.randint(1, 5)
    print("Random item:", item)
    print("Item:", item)
    while item < 3:
        print("Item is less than 3:", item)
        item += 1
    else:
        print("Item is now 3 or more:", item)
# This code uses a for loop to iterate through a range of numbers and a while loop to
# check if the item is less than 3. It prints messages accordingly and increments the item
# until it is 3 or more. The else block executes after the while loop completes. 
movie_list = ["Titanic", "Avatar", "Inception"]
for movie in movie_list:
    print("Movie title:",movie, end="")