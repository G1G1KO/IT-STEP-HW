''' 1)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __str__(self):
        return f"{(self.x, self.y)}"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return (new_x, new_y)
    


v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v1)
print(v2)
print(v3)
'''




''' 2)
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


    def __eq__(self, other):
        return self.name == other.name and self.author == other.author
    

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  
print(book1 == book3) 
'''





''' 3)
class Car:
    def __new__(cls, *args, **kwargs):
        print("1. გაეშვა __new__ -- მეხსიერებაში გამოიყო ადგილი ობიექტისთვის")
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year 


    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, new_brand):
        if not isinstance(new_brand, str):
            raise TypeError("Error, The Brand Must Be a String")
        self.__brand = new_brand.strip()



    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_model):
        if not isinstance(new_model, str):
            raise TypeError("Error, The Model Must Be a String")
        self.__model = new_model.strip()



    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, new_year):
        if not isinstance(new_year, int):
            raise TypeError("Error, The Year Must Be An Integer")
        self.__year = new_year


    def __str__(self):
        return f"Car Info: {self.__brand}, {self.__model}, {self.__year}"





c1 = Car("BWM", "M3", 1998)
print(c1)

print(c1.brand)

c1.year = 2026
print(c1)

print(c1.year)
'''