import random


class CAR:
    doors_count = 5
    fuel_consumption = 10
    fuel_type = 'Gas'

    def __init__(self, fuel=100, is_doors_open=False, color='black'):
        self.fuel = fuel
        self.is_doors_open = is_doors_open
        self.color = color

    @property
    def fuel_prop(self):
        return self._fuel

    def open_doors(self):
        if self.is_doors_open:
            raise Exception('Doors Open')

        self.is_doors_open = True

    def close_doors(self):
        if self.is_doors_open:
            raise Exception('Doors Close')

        self.is_doors_open = False

    def check_fuel(self):
        return self.fuel

    def run_car(self):
        if self.fuel < self.fuel_consumption:
            raise Exception('No fuel')

        self.fuel -= self.fuel_consumption

    def add_fuel(self, value):
        if self.fuel_type == 'Gas':
            value += 2
        elif self.fuel_type == 'Gasoline':
            value += 1
        self.fuel += value

    def repaint(self, new_color):
        if self.color == new_color:
            raise Exception('Equal color')

        self.color = new_color


class BMW(CAR):
    doors_count = 2
    fuel_consumption = 15
    fuel_type = 'Gasoline'

    def __init__(self, fuel=100, is_doors_open=False, color='red'):
        super().__init__(fuel, is_doors_open, color)


class Skoda(CAR):
    doors_count = 5
    fuel_consumption = 8
    fuel_type = 'Diesel'

    def __init__(self, fuel=100, is_doors_open=False, color='white'):
        super().__init__(fuel, is_doors_open, color)


class Reno(CAR):
    doors_count = 5
    fuel_consumption = 9
    fuel_type = 'Gas'

    def __init__(self, fuel=100, is_doors_open=False, color='green'):
        super().__init__(fuel, is_doors_open, color)


def compare_fuel():
    car_bmw = BMW()
    car_skoda = Skoda()

    try:
        car_bmw.run_car()
        car_skoda.run_car()
    except Exception:
        return

    if car_bmw.fuel > car_skoda.fuel:
        return True

    return False


def random_repaint(car: CAR):
    new_color = random.choice(['black', 'white', 'red', 'yellow', 'blue', 'green', 'purple'])

    try:
        car.repaint(new_color)
    except Exception:
        return 'Equal color'

    return car.color


if __name__ == '__main__':
    print(compare_fuel())
    print(random_repaint(car=BMW()))




