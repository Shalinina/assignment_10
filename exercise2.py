import random
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance_traveled = 0

    def drive(self):
        self.distance_traveled += self.speed

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.randint(-5, 5)
            car.drive()

    def print_status(self):
        print(f"{'Car Name':<15} {'Speed':<10} {'Distance Traveled':<20}")
        for car in self.cars:
            print(f"{car.name:<15} {car.speed:<10} {car.distance_traveled:<20}")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False
cars = [Car(f"Car {i+1}", random.randint(100, 200)) for i in range(10)]
grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)

hour_counter = 0
while not grand_demolition_derby.race_finished():
    grand_demolition_derby.hour_passes()
    hour_counter += 1
    if hour_counter % 10 == 0:
        print(f"\nRace Status after {hour_counter} hours:")
        grand_demolition_derby.print_status()

print("\nRace Finished!")
print("Final Race Status:")
