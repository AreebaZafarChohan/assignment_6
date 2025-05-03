# Assignment No 6

# 1. Using self
"""
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

"""

class Student:
    
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks
    
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
            
student1 = Student("Areeba", 99)
student1.display()      

print()      

# 2. Using cls
"""
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

"""

class Counter:
    count = 0
    
    def __init__(self) -> None:
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
         print(f"Total objects created: {cls.count}")
         
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
         
obj3.display_count()   

print()      

# 3. Public Variables and Methods
"""
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

"""

class Car:
    def __init__(self, brand) -> None:
        self.brand = brand
    
    
    def start(self):
        print(f"Starting Car")
    
car = Car("Toyota")
print(car.brand)
car.start()            

print()

# 4. Class Variables and Class Methods
"""
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

"""

class Bank:
    
    bank_name = "Islamic Bank"
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def change_name(cls, new_name):
        cls.bank_name = new_name
        print(f"New name of bank is {cls.bank_name}")
        
b1 = Bank()
b2 = Bank()

print(b1.bank_name) 
Bank.change_name("Meezan Bank")
print(b1.bank_name)  
print(b2.bank_name)   
      
print()      

# 5. Static Variables and Static Methods
"""
Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

"""

class MathUtils:
    
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(15,7))
print(MathUtils.add(77,1515))

print()
        

# 6. Constructors and Destructors
"""
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

"""

class Logger:
    
    def __init__(self) -> None:
        print("constructor")
    
    def __del__(self):
        print("destructor")    
        
log1 = Logger()
print("Doing some task...")
del log1 
print("End of program")
     
print()

# 7. Access Modifiers: Public, Private, and Protected
"""
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.

"""

class Employee:
    
    def __init__(self) -> None:
        self.name = "Areeba Zafar"
        self._salary = 100000
        self.__ssn = "123-45-6789"
        
    
    def get_ssn(self):
        return self.__ssn
        
employee = Employee()

print(employee.name)
print(employee._salary)

# Accessing private variable directly (will cause an error)
# print(emp.__ssn)    Not allowed, will raise AttributeError

# Accessing private variable using name mangling (works, but not recommended)
#print(employee._Employee__ssn)  

print(employee.get_ssn())

print()


# 8. The super() Function
"""
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

"""

class Person:
    
    def __init__(self, name) -> None:
        self.name = name
        

class Teacher(Person):
    
    def __init__(self, name, subject) -> None:
        super().__init__(name)   
        self.subject = subject
    
teacher = Teacher("Areeba", "IT")

print(teacher.name)
print(teacher.subject)             

print()

# 9. Abstract Classes and Methods
"""
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

"""

from abc import ABC, abstractmethod
from typing import Any

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    

class Rectangle(Shape):
    
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        
    def area(self):
        return  self.length * self.width   

rec = Rectangle(7,15)
print(f"Area of reactangle is {rec.area()}")

print()

# 10. Instance Methods
"""Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name."""

class Dog:
    
    def __init__(self, name, breed) -> None:
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking!") 

dog = Dog("Tomy", "Golden Retriever")       

dog.bark()

print()    

# 11. Class Methods
"""Assignment:
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added."""

class Book:
    
    total_books = 0
    
    def __init__(self, book_name) -> None:
        self.book_name = book_name
        
    def add_book(self):
        print(f"Book '{self.book_name}' added successfully.")
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")
        
book1 = Book("Python Programming")
book1.add_book()
Book.increment_book_count()

book2 = Book("Machine Learning")
book2.add_book()    
Book.increment_book_count()

print()

# 12. Static Methods
"""Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value."""

class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        fahrenheit = (c * 9/5) + 32
        return fahrenheit

print(TemperatureConverter.celsius_to_fahrenheit(234))   
print(TemperatureConverter.celsius_to_fahrenheit(157))   

print()

# 13. Composition
"""Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class."""

class Engine:
    
    def __init__(self, engine_type) -> None:
        self.engine_type = engine_type
    
    def start_engine(self):
        print(f"{self.engine_type} engine started.")    

class MyCar:
    def __init__(self, car_brand, engine_type) -> None:
        self.car_brand = car_brand
        self.engine_type = Engine(engine_type)
        
    def start_car(self):
        print(f"Starting {self.car_brand} car...") 
        self.engine_type.start_engine()

my_car = MyCar("Toyota", "V8")       
my_car.start_car()    
            
print()


# 14. Aggregation
"""Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it."""

class Employe:
    
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

class Department:
    
    def __init__(self, depart_id, employee: Employe ) -> None:
        self.depart_id = depart_id
        self.employee = employee
        
    def show_details(self):
        print(f"Department ID: {self.depart_id}")
        print(f"Employee Name: {self.employee.name}")
        print(f"Employee ID: {self.employee.id}")
        
emp1 = Employe("Sara Chohan", 157)        
depart1 = Department(201, emp1)
depart1.show_details()
            
print()           


# 15. Method Resolution Order (MRO) and Diamond Inheritance
"""Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO."""


class A:
    def show(self):
        print("A")
        
class B(A):
    def show(self):
        print("B")        

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass


d = D()
d.show()

print()

# print(D.mro())  for looking MRO Order 
# Output will be : [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]



# 16. Function Decorators
"""Assignment:
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()."""

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
        
    return wrapper

@log_function_call
def say_hello():
    print("Hello Everyone!")
    
say_hello()    
        
print()

# 17. Class Decorators
"""Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
"""

def add_greeting(cls):   
    class Wrapped(cls):
        def greet(self):
            return "Hello from Decorator!"
    return Wrapped  
                
        
@add_greeting
class Person2:
    
    def __init__(self) -> None:
        print("Class Person Initialized")
    
person = Person2()
print(person.greet())            
    
print()

# 18. Property Decorators: @property, @setter, and @deleter
"""Assignment:
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it."""

class Product:
    
    def __init__(self, _price) -> None:
        self._price = _price
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        print("Setting new price...")
        self._price =  new_price 
        
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price
        
product1 = Product(715)
print(product1.price)

product1.price = 4343
print(product1._price)

del product1.price

print()


# 19. callable() and __call__()
"""Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function."""

class Multiplier:
    
    def __init__(self, factor) -> None:
        self.factor = factor
        
    def __call__(self, value):
        return self.factor * value

multiply_by_7  = Multiplier(7) 
print(callable(multiply_by_7))

result = multiply_by_7(157)
print(result)

print()       

# 20. Creating a Custom Exception
"""Assignment:
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except."""

class InvalidAgeError(Exception):
    pass

def check_age(age):
    try:
        if age >= 18:
            print("Valid")
        else:
            raise InvalidAgeError("Age must be 18 or older.")
    except InvalidAgeError as e:
        print(f"Error: {e}")

check_age(17)
check_age(18)
check_age(19) 

print()                

# 21. Make a Custom Class Iterable
"""Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0."""


class Countdown:
    def __init__(self, start_num) -> None:
        self.start_num = start_num
        
    def __iter__(self):
        self.current = self.start_num
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

for num in Countdown(7):
    print(num)        
            
print()            
            