'''class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")

my_dog = Dog("Bruno")
my_dog.bark()
# Output: Bruno says Woof!'''

'''class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def intro(self):
    print("Hello, my name is", self.name, "and I am", self.age, "years old.")
    
    rohan = person("Ash", 25)
    rohan.intro()
# Output: Hello, my name is Ash and I am 25 years old.'''

#Create a class Person with:Attributes: name, ageMethod: introduce() that prints: “Hi, I’m [name], [age] years old.”Make two Person objects and call their introduce() method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person1.introduce()
person2.introduce()

    