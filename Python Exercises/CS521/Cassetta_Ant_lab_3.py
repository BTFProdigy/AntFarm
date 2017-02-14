class Parent(object):
    greeting = "Hi, I'm a parent object"


class ChildA(Parent):
    greeting = "Hi, I'm a child object"


class ChildB(Parent):
    pass


# create instences
pops = Parent()
kidA = ChildA()
kidB = ChildB()

# print
print(pops.greeting)
print(kidA.greeting)
print(kidB.greeting)
