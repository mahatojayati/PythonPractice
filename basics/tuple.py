tuple = (1,2,3,3,4,5,6,7,8,9,10)
print(tuple)
# Tuples are immutable, so we cannot modify them like lists.
# However, we can perform some operations like counting and finding the index of an element.
print(tuple.count(3))  # Count occurrences of 3
print(tuple.index(5))  # Find index of 5
print(tuple)

# To modify a tuple, we need to convert it to a list, make changes, and
# then convert it back to a tuple.
temp_list = list(tuple)  # Convert tuple to list
temp_list.append(11)  # Append 11 to the list
print(temp_list)

temp_list.remove(2)  # Remove 2 from the list
print(temp_list)

temp_list.sort()  # Sort the list
print(temp_list)

temp_list.reverse()  # Reverse the list
print(temp_list)

temp_list.insert(2, 12)  # Insert 12 at index 2
print(temp_list)

temp_list.pop()  # Remove the last element
print(temp_list)