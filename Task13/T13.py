''' 1)
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year if 1886 <= year <= 2026 else None

    def car_info(self):
        if self.year is None:
            print("Error, Wong Year")
        else:
            print(f"Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}")



c1 = Car("BWM", "C-class", 2024)
c1.car_info()
'''


''' 2)
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year if 1886 <= year <= 2026 else None


    def car_info(self):
        if self.year is None:
            print("Error, Wrong Year")
        else:
            print(f"Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}")


    def age_of_car(self):
        from datetime import datetime
        curret_year = datetime.now().year
        car_age = curret_year - self.year  
        print(f"{self.brand} {self.model} Is {car_age} Years old")


c1 = Car("Audi", "RX-7", 1990)
c1.car_info()
c1.age_of_car()
'''



''' 3)
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year if 1886 <= year <= 2026 else None


    def car_info(self):
        if self.year is None:
            print("Error, Wrong Year")
        else:
            print(f"Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}")


    def age_of_car(self):
        from datetime import datetime
        curret_year = datetime.now().year
        car_age = curret_year - self.year  
        print(f"{self.brand} {self.model} Is {car_age} Years old")



class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)

        self.battery_life = battery_life 


    def battery_info(self):
        if self.battery_life is None:
            print("Error, Wrong Battery Life Out Of Range")
        else:
            print(f"ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს")



c1 = ElectricCar("Opel", "Corsa", 2019, 24)
c1.car_info()
c1.battery_info()
''' 



''' 4)
class Car:

    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year if 1886 <= year <= 2026 else None
        Car.number_of_cars += 1


        print(Car.number_of_cars)



c1 = Car("a","b",55)
c2 = Car("x", "y", 45)
c3 = Car("ad", "qe", 13)
'''





''' 5)
class Car:

    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year if 1886 <= year <= 2026 else None
        Car.number_of_cars += 1

        

    @classmethod
    def total_car(cls):
        print(f"Amount Of Cars: {cls.number_of_cars}")




c1 = Car("BMW", "M5", 2020)
c2 = Car("Tesla", "Model 3", 2026)
c3 = Car("Audi", "RS6", 2024)

Car.total_car()
'''