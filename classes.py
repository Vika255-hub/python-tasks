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

    def get_property(self):
        car_property = {
            'fuel_type': self.fuel_type, 'doors_count': self.doors_count,
            'is_doors_open': self.is_doors_open, 'fuel': self._fuel, 'fuel_consumption': self.fuel_consumption
        }
        return car_property


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


def random_repaint(car: CAR):
    new_color = random.choice(
        ['black', 'white', 'red', 'yellow', 'blue', 'green', 'purple']
    )

    try:
        car.repaint(new_color)
    except Exception:
        pass

    return car.color


def compare_count_fuel():

    try:

        def run_c(car: CAR):
            run_count = 2
            while run_count > 0:
                car.run_car()
                run_count = run_count - 1
            return car.fuel

    except Exception:
        return

    if run_c(car=BMW()) > run_c(car=Reno()) and run_c(car=Reno()) < run_c(car=Skoda()):
        return 'Reno has the least fuel'
    elif run_c(car=Reno()) > run_c(car=BMW()) and run_c(car=BMW()) < run_c(car=Skoda()):
        return 'BMW has the least fuel'
    return 'Skoda has the least fuel'


def get_open_doors_and_property():
    car_bmw = BMW()
    car_skoda = Skoda()
    car_reno = Reno()

#    rand_car = random.choice(car_bmw, car_skoda, car_reno)
#    rand_car. open_doors

    return f'BMW: {car_bmw.get_property()}' '\n' f'Skoda: {car_skoda.get_property()}' \
           '\n' f'Reno: {car_reno.get_property()}'


if __name__ == '__main__':
    print(random_repaint(car=BMW()))
    print(compare_count_fuel())
    print(get_open_doors_and_property())


