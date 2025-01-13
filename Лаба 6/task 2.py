class Vehicle:

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def get_info(self):
        return f'Марка машины: {self.make}; модель машины: {self.model}'

class Car(Vehicle):

    def __init__(self, make: str, model: str, fuel_type: str):
        super().__init__(make,model)
        self.fuel_type = fuel_type

    def get_info(self):
        return super().get_info() + f" ;тип топлива: {self.fuel_type}"
MyCar = Car("Lada", "Turbo space", "Древесный уголь")
print(MyCar.get_info())
