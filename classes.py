class CAR:
    doors_count = 5
    color = 'black'
    fuel_consumption = 10

    def __init__(self, fuel=100):
        self.fuel = fuel

    def open_doors(self):
        return True

    def close_doors(self):
        return False

    def check_fuel(self):
        return self.fuel

    def run_car(self):
        if self.fuel < self.fuel_consumption:
            raise Exception('No fuel')

        self.fuel -= self.fuel_consumption

    def add_fuel(self, value):
        self.fuel += value


class BMW(CAR):
    doors_count = 2
    color = 'red'
    fuel_consumption = 15


class Skoda(CAR):
    doors_count = 5
    color = 'white'
    fuel_consumption = 8


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


if __name__ == '__main__':
    print(compare_fuel())
