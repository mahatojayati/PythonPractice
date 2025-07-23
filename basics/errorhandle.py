try:
    age = int(input("Enter your age: "))
    print("you'll be",age+1,"in next year!")
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# Example of handling a KeyError
try:
    Novels = {1: "The Great Gatsby",
              2: "To Kill a Mockingbird",
              3: "1984",
              4: "Pride and Prejudice",
              5: "The Catcher in the Rye",}
    print(Novels[6])  # This will raise a KeyError
except KeyError:
    print("KeyError: The key you are trying to access does not exist in the dictionary.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# Example of handling a TypeError
try:
    result = "string" + 5  # This will raise a TypeError
except TypeError:
    print("TypeError: You cannot concatenate a string and an integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# Example of handling an IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise an IndexError
except IndexError:
    print("IndexError: The index you are trying to access is out of range.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# Example of handling a ZeroDivisionError
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("ZeroDivisionError: You cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# Example of handling a FileNotFoundError

    