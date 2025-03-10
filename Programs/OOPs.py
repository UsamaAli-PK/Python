
class Battery:
    def battery_info(self):
        return "Battery is 100% charged"

class Engine:
    def engine_info(self):
        return "Engine is running at 100% capacity"

#Base class 
class Car:
    total_car = 0  # Class-level variable to track the number of car objects created

    # Constructor to initialize name, model, and year 
    def __init__(self, name, model, year):
        self.name = name        
        self.__model = model    # Private attribute 
        Car.total_car += 1      
        
        # Private attribute (encapsulation), the year is made private
        self.__year = year     

    # Getter method to access the private year attribute
    def get_year(self):
        return self.__year

    # Property method for accessing the model of the car
    @property
    def model(self):
        return self.__model

   
    def full_name(self):
        return f"{self.name}, {self.__model}, {self.__year}"

    
    def fuel_type(self):
        return "Petrol or Diesel"

    # Static method that provides general driving advice
    @staticmethod
    def Instruction():
        return "Drive Carefully"

#a subclass ElectricCar that inherits from Car
class ElectricCar(Car):
    # Constructor
    def __init__(self, name, model, year, battery_size):

        # Call the constructor of the parent class (Car) using super()
        super().__init__(name, model, year)
        
        self.battery_size = battery_size  # Additional attribute specific to ElectricCar

    # Overriding the fuel_type method to specify Electric Charge for ElectricCar
    def fuel_type(self):
        return "Electric Charge"

# Define a class ElectricCarTwo that inherits from Car, Battery, and Engine (Multiple Inheritance)
class ElectricCarTwo(Car, Battery, Engine):
    pass



#----------------------------------------------------------------

# Example usage of the ElectricCar subclass
My_ElectricCar = ElectricCar("Tesla", "Model S", 2023, "200KWh")

# Accessing attributes and methods from ElectricCar object
print(My_ElectricCar.name) 
print(My_ElectricCar.model)

# Using the getter method to access the private year attribute
print(My_ElectricCar.get_year())  

# Accessing the battery size, a specific attribute of ElectricCar
print(My_ElectricCar.battery_size)

print("\n----------------------------------------------------------------\n")

# Calling the inherited method to get the full name of the electric car
print(My_ElectricCar.full_name())

print("\n----------------------------------------------------------------\n")

# Checking if My_ElectricCar is an instance of Car and ElectricCar
print(isinstance(My_ElectricCar, Car))  
print(isinstance(My_ElectricCar, ElectricCar))  

print("\n----------------------------------------------------------------\n")

# Calling the overridden fuel_type method for ElectricCar
print(My_ElectricCar.fuel_type())  

print("\n----------------------------------------------------------------\n")

# Printing the total number of Car objects created
print("Total number of cars created:", Car.total_car)

print("\n----------------------------------------------------------------\n")

# Calling the static method Instruction from the Car class
print(Car.Instruction())  

print("\n----------------------------------------------------------------\n")

# Example usage of ElectricCarTwo (Multiple Inheritance)
My_ElectricCar2 = ElectricCarTwo("Nexon", "S model", 2021)
print(My_ElectricCar2.full_name())
print(My_ElectricCar2.engine_info())  
print(My_ElectricCar2.battery_info()) 
