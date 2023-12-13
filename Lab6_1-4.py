class Car:
    def __init__(self, brand, color, engine_volume):
        self.brand = brand
        self.color = color
        self.engine_volume = engine_volume

    def drive_forward(self):
        print("Drive forward")

    def drive_backward(self):
        print("Drive backward")

car = Car("Toyota", "blue", 2.0)
car.drive_forward()
car.drive_backward()

class CarWithTurn(Car):
    def turn_left(self):
        print("Turn left")

    def turn_right(self):
        print("Turn right")

car_with_turn = CarWithTurn("Honda", "red", 1.5)
car_with_turn.turn_left()
car_with_turn.turn_right()

class Airplane:
    def __init__(self, model):
        self.model = model

    def take_off(self):
        print("Take off")

airplane = Airplane("Boeing 747")
airplane.take_off()

class HybridVehicle(CarWithTurn, Airplane):
    pass

hybrid_vehicle = HybridVehicle("Hybrid Model")
hybrid_vehicle.drive_forward()
hybrid_vehicle.turn_left()
hybrid_vehicle.take_off()

