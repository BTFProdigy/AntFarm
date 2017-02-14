import random

class Pet:
    # Create an empty speak method for the child classes to implement
    pass

class Dog(Pet):
    # Create the sit function here
    pass

class BigDog(Dog):
    # Create an __init__ function to set the description
    # Create the speak method here
    pass

# Create the SmallDog class here

# Create the Cat class here

# Create the HouseCat class here

# Create the StrayCat class here

# This line treats class definitions as objects. Isn't that cool?
petClasses = [BigDog, SmallDog, HouseCat, StrayCat]
# Change this line to ask the user to input how many pets to generate
numberOfPets = 0
for petCount in range(0, numberOfPets):
    # This line creates new objects from the stored class definitions!
    pet = petClasses[random.randrange(4)]()
    # Print the info for part 3 of the assignment description here
