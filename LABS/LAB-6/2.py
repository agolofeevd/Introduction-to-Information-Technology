class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Бренд: {self.make}, Модель: {self.model}"

class Car(Vehicle):
        def __init__(self, make, model, fuel_type):
            super().__init__(make, model)
            self.fuel_type = fuel_type

        def get_info(self):
            base_info = super().get_info()
            return f"{base_info}, Тип двигателя: {self.fuel_type}"


vehicle = Vehicle("Lada", "Niva")

car1 = Car("BMW", "520i", "бензин")
car2 = Car("Tesla", "Model S", "электро")

print("Базовый класс Vehicle:")
print(vehicle.get_info())
print(car1.get_info())
print(car2.get_info())
