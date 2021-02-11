import random


class CAR:
    doors_count = 5
    fuel_consumption = 10

    def __init__(self, fuel=100, is_doors_open=False, color='black'):
        self.fuel = fuel
        self.is_doors_open = is_doors_open
        self.color = color

    @property
    def _fuel(self):
        return self.fuel

    def open_doors(self):
        if self.is_doors_open == True:
            raise Exception('Doors Open')

        self.is_doors_open = True

    def close_doors(self):
        if self.is_doors_open == False:
            raise Exception('Doors Close')

        self.is_doors_open = False

    def check_fuel(self):
        return self.fuel

    def run_car(self):
        if self.fuel < self.fuel_consumption:
            raise Exception('No fuel')

        self.fuel -= self.fuel_consumption

    def add_fuel(self, value):
        self.fuel += value

    def repaint(self, new_color):
        if self.color == new_color:
            raise Exception('Equal color')

        self.color = new_color


class BMW(CAR):
    doors_count = 2
    fuel_consumption = 15

    def __init__(self, fuel=100, is_doors_open=False, color='red'):
        super().__init__(fuel, is_doors_open, color)


class Skoda(CAR):
    doors_count = 5
    fuel_consumption = 8

    def __init__(self, fuel=100, is_doors_open=False, color='white'):
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


def random_repaint():
    car_bmw = BMW()
    new_color = random.choice(['black', 'white', 'red', 'yellow', 'blue', 'green', 'purple'])

    try:
        car_bmw.repaint(new_color)
    except Exception:
        return 'Equal color'

    return car_bmw.color


if __name__ == '__main__':
    print(compare_fuel())
    print(random_repaint())

