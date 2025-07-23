hobbies = ["reading", "gaming", "hiking", "cooking"]
print(hobbies)
hobbies.append("painting")
print(hobbies)
hobbies.remove("gaming")
print(hobbies)
hobbies.sort()
print(hobbies)
hobbies.reverse()
print(hobbies)
hobbies.insert(2, "photography")
print(hobbies)
hobbies.pop()
print(hobbies)
hobbies.clear()
print(hobbies)
hobbies.extend(["traveling", "writing"])
print(hobbies)

fruits = ["apples", "bananas", "cherries"]
for i in range(len(fruits)):
    fruits[i] = fruits[i].isalpha()
print(fruits)