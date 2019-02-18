
class cat:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog object
mitzi = cat("Mitzi", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    mitzi.name, mitzi.age, mikey.name, mikey.age))

# Is Mitzi a mammal?
if mitzi.species == "female":
    print("{0} is a {1}!".format(mitzi.name, mitzi.species))

# Is Mikey a mammal?
if mikey.species == "mail":
    print("{0} is a {1}!".format(mikey.name, mikey.species))
