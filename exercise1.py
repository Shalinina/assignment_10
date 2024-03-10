class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, floor):
        if floor < self.bottom or floor > self.top:
            print("Invalid floor!")
            return
        print(f"Elevator is moving from floor {self.current_floor} to floor {floor}.")
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()
        print("Elevator has arrived at floor", self.current_floor)

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1

        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor == self.bottom:
            print("Already at the bottom floor.")
        else:
            self.current_floor -= 1

elevator = Elevator(1, 10)

while True:
        print("\nCurrent Floor:", elevator.current_floor)
        floor_num = int(input("Enter the floor number you want to go (1-10): "))
        elevator.go_to_floor(floor_num)
