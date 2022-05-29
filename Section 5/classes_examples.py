class Vehicle:
    def __init__(self, brand, doors, wheels=4):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels

    def car_greeting(self, local_slang):
        print(f'{local_slang}, Im your new car. My name is {self.brand} and I have {self.wheels} wheels')


veh1 = Vehicle('VW', 2)
veh1.car_greeting('Ya')
# override in case we have more wheels
# veh1 = Vehicle('VW', 2, 3)
# print(veh1.wheels)

veh2 = Vehicle('BMW', 4)


# print(veh1.brand)


class Car:
    brand = 'Volvo'


car1 = Car()
print(car1.brand)

car2 = Car()
print(car2.brand)
