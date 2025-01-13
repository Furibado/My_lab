class Circle:

    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        return(f'Радиус круга = {self.radius}')

    def set_radius(self, new_radius):
        self.radius = new_radius

square = Circle(3)
print(square.get_radius())
new_radius = int(input('Введите новый радиус '))
square.set_radius(new_radius)
print(square.get_radius())