class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print(f"My {self.make} {self.model} is running")

car1 = Car("Toyota", "Axio")
car1.start_engine()
print(f"Is the Engine running? {car1.is_running}")


car2 = Car("Mercedes", "Coupe")
car2.start_engine()
print(f"Is the Engine running? {car2.is_running}")