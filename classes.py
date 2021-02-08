class CAR(object):
    def __init__(self, doors_count=5, color='black', fuel=100, fuel_consumption=10):
        self.doors_count = doors_count
        self.color = color
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def open_doors(self):
        return True

    def close_doors(self):
        return False

    def check_fuel(self):
        return self.fuel

    def run_car(self):
        if self.fuel > self.fuel_consumption:
            return self.fuel - self.fuel_consumption
        raise Exception('No fuel')

    def add_fuel(self, value):
        return value + self.fuel


class BMW(CAR):
    def __init__(self, doors_count, color, fuel, fuel_consumption):
        super().__init__(doors_count, color, fuel, fuel_consumption)


class Skoda(CAR):
    def __init__(self, doors_count, color, fuel, fuel_consumption):
        super().__init__(doors_count, color, fuel, fuel_consumption)


def compare_fuel():
    car_BMV = BMW(2, 'red', 10, 15)
    car_Skoda = Skoda(5, 'white', 100, 8)
    if isinstance(car_BMV.run_car(), int) and isinstance(car_Skoda.run_car(), int):
        if car_BMV.run_car() > car_Skoda.run_car():
            return True
        return False
    raise Exception('No fuel')


if __name__ == '__main__':
    print(compare_fuel())

