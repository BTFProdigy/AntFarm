'''
Object-Oriented Programming (OOP) with Python
'''

##class Parent:
##    '''
##    a.k.a Base Class or Super Class
##
##    this implicitly inherits from `object`, which defines several methods
##    '''
##
##    class_attribute = 'I belong to the class, not the instance'
##
##    def __init__(self, value):
##        '''
##        Many languages have just one "constructor" method.
##
##        Python splits the constructor role into two methods,
##        both defined on the implicit base class `object`:
##            __new__ is the constructor; it's very rarely overridden
##            __init__ is the initializer; it's almost always overridden
##        '''
##        print('Running `Parent` initializer')
##
##        # Best practice is to initialize all instance attributes in
##        # the __init__, so they are available from the moment the
##        # instance is created. It might surprise someone if they tried
##        # to access the instance attribute and it hadn't yet been
##        # created!
##        self.instance_attribute = value
##
##
##    def parent_method(self):
##        print('Calling `Parent` method')
##
##
##    def get_attribute(self):
##        '''
##        A getter for the instance attribute.
##
##        Many languages have a best practice to only access instance
##        attributes via getter and setter methods. This is NOT a best
##        practice for Python, but I want to show it to you here,
##        because it is common for many languages.
##
##        If you'd like to know more about why this is NOT a best
##        practice for Python, you can read about "properties". That
##        topic is not covered in this course, because it is an
##        intermediate Python-specific topic.
##        '''
##        print('Getting an attribute...')
##        return self.instance_attribute
##
##
##    def set_attribute(self, value):
##        '''
##        A setter for the instance attribute.
##        '''
##        print('Setting an attribute...')
##        self.instance_attribute = value
##
##        # Setters should return None (implicit if there's no return)
##        # to indicate that they've mutated/changed the state of the
##        # object
##
##
##
##class Child(Parent):
##    '''
##    a.k.a Sub Class
##
##    Our inheritance hierarchy is now:
##        Child --[is a]--> Parent --[is a]--> object
##
##    The implicit inheritance from `object` is Python-specific.
##    '''
##
##    def __init__(self, value):
##        super().__init__(value)
##        print('Calling the `Child` initializer')
##
##    def child_method(self):
##        print('Calling the `Child` method')
##
##    def get_attribute(self):
##        '''
##        This overrides/shadows/hides the Parent implementation of
##        get_atrribute.
##        '''
##        print('Override!')
##        return super().get_attribute()
##
##        # alternately, instead of explicitly saying super(), we could
##        # use Parent to dynamically figure out who the base class is.
##        # return Parent.get_attribute(self), however this is not recommended
##        #by PEP8
##
##
##
##if __name__ == '__main__':
##    p = Parent(5)
##    p.parent_method()
##    print(p.get_attribute())
##    p.set_attribute(42)
##    print(p.get_attribute())
##
##    c = Child(15)
##    c.child_method()
##    c.parent_method()
##    print(c.get_attribute())
##    c.set_attribute(190)
##    print(c.get_attribute())

###__doc__ is the document file for the object
##print("Child.__doc__: {}".format(Child.__doc__))
##
###__name__ is the class name
##print("Child.__name__: {}".format(Child.__name__))
##
###__module__ The name of the module the function was defined in, or None if unavailable.
##print("Child.__module__: {}".format(Child.__module__))
##
###Lists a tuple of the base classes of Child
##print("Child.__bases__: {}".format(Child.__bases__))
##
###The namespace supporting arbitrary function attributes.
###
##print("Child.__dict__: {}".format(Child.__dict__))
##
##print(issubclass(Child, Parent))
##print(issubclass(Parent, Child))
##print(isinstance(c, Parent))
##print(isinstance(c, Child))
##
class Car:
    def __init__(self, name):    
        self.name = name
 
    def drive(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'
 
    def stop(self):
        return 'Sportscar breaking!'
 
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'
 
    def stop(self):
        return 'Truck breaking!'
 
 
cars = [Truck('Bananatruck'),
        Truck('Orangetruck'),
        Sportscar('Z3')]
 
for car in cars:
    print(car.name + ': ' + car.drive())
