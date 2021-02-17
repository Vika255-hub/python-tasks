import random


class CAR:
    doors_count = 5
    fuel_consumption = 10
    fuel_type = 'Gas'

    def __init__(self, fuel=100, color='black'):
        self._fuel = fuel
        self.color = color
        self.is_doors_open = False

    @property
    def fuel(self):
        return self._fuel

    def open_doors(self):
        if self.is_doors_open:
            raise Exception('Doors Open')

        self.is_doors_open = True

    def close_doors(self):
        if not self.is_doors_open:
            raise Exception('Doors Close')

        self.is_doors_open = False

    def check_fuel(self):
        return self.fuel

    def run_car(self):
        if self.fuel < self.fuel_consumption:
            raise Exception('No fuel')

        self._fuel -= self.fuel_consumption

    def add_fuel(self, value):
        if self.fuel_type == 'Gas':
            value += 2
        elif self.fuel_type == 'Gasoline':
            value += 1
        self._fuel += value

    def repaint(self, new_color):
        if self.color == new_color:
            raise Exception('Equal color')

        self.color = new_color


class BMW(CAR):
    doors_count = 2
    fuel_consumption = 15
    fuel_type = 'Gasoline'

    def __init__(self, fuel=100, color='red'):
        super().__init__(fuel, color)


class Skoda(CAR):
    doors_count = 5
    fuel_consumption = 8
    fuel_type = 'Diesel'

    def __init__(self, fuel=100, color='white'):
        super().__init__(fuel, color)


class Reno(CAR):
    doors_count = 5
    fuel_consumption = 9

    def __init__(self, fuel=100, color='green'):
        super().__init__(fuel, color)


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
    new_color = random.choice(
        ['black', 'white', 'red', 'yellow', 'blue', 'green', 'purple']
    )

    try:
        car.repaint(new_color)
    except Exception:
        pass

    return car.color


if __name__ == '__main__':
    print(compare_fuel())
    print(random_repaint(car=BMW()))




