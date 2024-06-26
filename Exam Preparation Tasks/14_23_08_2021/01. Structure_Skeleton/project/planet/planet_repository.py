from typing import List
from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets: List = [Planet]

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        return next(filter(lambda planet: planet.name == name, self.planets), None)
