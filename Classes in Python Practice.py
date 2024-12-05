#***********************************************************************************************************************
#Muhammed Mozzam Hasnan
#FA24-BBD-103

#Question1*********************************************************************** 
#Create a class Person with attributes name, age, and city.
print("Class Person")
class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city 
person = Person("Mozzam", 19, "Lahore")
print(person.name, person.age , person.city)

#Question2************************************************************************
#Create a class Car with attributes make, model, and year.
print("\nClass Car")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
car_info = Car("Ferrari", "Laferrari", 2000)
print(car_info.make, car_info.model ,car_info.year)

#Question3************************************************************************
#Create a class Circle with attributes radius and methods to calculate area and circumference.
print("\nClass Circle")
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * (self.radius ** 2) 
        self.circumference = 2 * 3.14159 * self.radius
circle1 = Circle(10)  
print("Area:", circle1.area)  
print("Circumference:", circle1.circumference)

#Question4************************************************************************
#Create a class Rectangle with attributes length and width and methods to calculate area and perimeter.
print("\nClass Rectangle")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width  
        self.perimeter = 2 * (self.length + self.width)  
rectangle = Rectangle(5, 3)  
print("Area:", rectangle.area)  
print("Perimeter:", rectangle.perimeter)

#Question5***********************************************************************
#Create a class Student with attributes name, roll_number, and marks. Implement a method to calculate the average marks.
print("\nClass Student")
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name                
        self.marks = marks              
        self.average_marks = sum(self.marks) / len(self.marks) if self.marks else 0  
student1 = Student("Alice", 101, [83, 85, 76, 69, 75])  
print("Average Marks:", student1.average_marks)  

#Question6***********************************************************************
#Create a class Book with attributes title, author, and publication_year.
print("\nClass Book")
class Book:
    def __init__(self,title,author,publication_year):
        print ("Details of the book are:")
        self.title=title
        self.author=author
        self.publication_year=publication_year
book1=Book("The Alchemist","Paulo Coelho",1988)
print()
print(f"The name of the book is {book1.title}.\nIts author name is {book1.author}.\nIt is published in the year {book1.publication_year}.")

#Question7*************************************************************************
#Create a class Employee with attributes name, salary, and designation.
print("\nClass Employee")
class Employee:
    def __init__(self, name, salary, designation):
        self.name=name
        self.salary=salary
        self.designation=designation
E1=Employee("Mozzam",99999,"Data Scientist")
print(f"{E1.name} is a {E1.designation} and earns {E1.salary}")

#Question8***************************************************************************
#Create a class Bank with attributes name, account_number, and balance. Implement methods to deposit and withdraw money.
print("\nClass Bank")
class Bank:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    def deposit(self,ammount):
        if ammount ==0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance+=ammount
            print(f"Deposited ammount ={ammount}\nNew balance = {self.balance}")

    def withdraw(self,fig):
        if fig>0:
            if fig<self.balance:
                self.balance-=fig
                print(f"Withdrew ${fig}. \nNew balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
             print("Withdrawal amount must be greater than zero.")

bank1=Bank("HBL",123456788988,5000000)
print(f"The name of the customer's bank is {bank1.name}.\nHis account number is {bank1.account_number}.\nThe balance in his account is {bank1.balance}")
print()
bank1.deposit(50000)
print()
bank1.withdraw(100000)
#************************************************************************************************************************