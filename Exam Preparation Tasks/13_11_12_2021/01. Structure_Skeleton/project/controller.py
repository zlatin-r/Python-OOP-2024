from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if next(filter(lambda car: car.model == model, self.cars), None):
            raise Exception(f"Car {model} is already created!")

        if self._is_car_type_valid(car_type):
            new_car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
            new_car.speed_limit = speed_limit

            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self._check_if_driver_exists(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self._check_if_race_exists(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._check_if_driver_exists(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type in self.VALID_CAR_TYPES.keys():
            car = self._find_available_car(car_type)

            if driver.car:
                car.is_taken = True
                old_car = driver.car
                old_car.is_taken = False
                driver.car = car
                return f"Driver {driver.name} changed his car from {old_car.model} to {driver.car.model}."

            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._check_if_race_exists(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self._check_if_driver_exists(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if self._check_if_driver_is_already_in_race(driver, race):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._check_if_race_exists(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_cars = sorted(race.drivers, key=lambda d: -d.car.speed_limit)
        result = []
        for driver in sorted_cars[0:3]:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)

    # Helping methods:

    def _is_car_type_valid(self, car_type: str):
        return car_type in self.VALID_CAR_TYPES

    def _find_available_car(self, car_type: str):
        for c in range(len(self.cars) - 1, -1, -1):
            if type(self.cars[c]).__name__ == car_type:
                if not self.cars[c].is_taken:
                    return self.cars[c]
        raise Exception(f"Car {car_type} could not be found!")

    def _check_if_driver_exists(self, driver_name: str):
        return next(filter(lambda d: d.name == driver_name, self.drivers), None)

    def _check_if_race_exists(self, race_name: str):
        return next(filter(lambda r: r.name == race_name, self.races), None)

    def _check_if_driver_is_already_in_race(self, driver: Driver, race: Race):
        result = [d for d in race.drivers if d.name == driver.name]
        return len(result) > 0
