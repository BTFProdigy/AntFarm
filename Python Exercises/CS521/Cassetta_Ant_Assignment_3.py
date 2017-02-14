import random


class Pet:
    def __init__(self):
        pass

    def speak(self):
        pass


class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__()

    def sit(self):
        print('The dog sits...')


class BigDog(Dog, Pet):
    def __init__(self):
        super(BigDog, self).__init__()
        self.description = 'A large, muscular dog.'

    def speak(self):
        print('Woof!')


class SmallDog(Dog, Pet):
    def __init__(self):
        super(SmallDog, self).__init__()
        self.description = 'A tiny, cute dog.'

    def speak(self):
        print('Yip!')


class Cat:
    def __init__(self):
        super(Cat, self).__init__()

    def purr(self):
        print('Purrrr')

    def speak(self):
        print('Meow')


class HouseCat(Cat, Pet):
    def __init__(self):
        super(HouseCat, self).__init__()
        self.description = 'A cat with fluffy, white fur.'


class StrayCat(Cat, Pet):
    def __init__(self):
        super(StrayCat, self).__init__()
        self.description = 'A cat with tousled, striped fur'

petClasses = [BigDog, SmallDog, HouseCat, StrayCat]

numberOfPets = int(input('How many pets shall we pull from the magic hat?: \n'))

for petCount in range(0, numberOfPets):

    pet = petClasses[random.randrange(4)]()

    print('\nPet number, {}'.format(petCount))
    print(pet.description)
    pet.speak()

    if isinstance(pet, Cat):
        pet.purr()
    elif isinstance(pet, Dog):
        pet.sit()
