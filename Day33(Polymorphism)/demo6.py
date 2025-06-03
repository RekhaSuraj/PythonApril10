class Vehicle:

    def speed(self):
        print('vehicle speed is 100kmph')


class Truck(Vehicle):

    def speed(self):
        print('Truck speed is 75kmph')


class Car(Vehicle):

    def speed(self):
        print('Car speed is 150kmph')


obj_Car = Car()
obj_Car.speed()
# Car speed is 150kmph

obj_Truck = Truck()
obj_Truck.speed()
# Truck speed is 75kmph


# A base class: Vehicle with a method speed().
# Two derived classes: Truck and Car, both overriding the speed() method.
# This is runtime polymorphism:
# The method speed() behaves differently depending on the object calling it (Truck, Car, or Vehicle).
# Method calls are resolved at runtime — that's why it’s called dynamic method dispatch
