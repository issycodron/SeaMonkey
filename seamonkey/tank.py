import random
import math
from .settings import DEATH_PROBABILITY, EGG_PROBABILITY, HATCH_PROBABILITY, FILE_PATH
####################

class Tank(object):
    def __init__(self, name, width, depth, height):
        self.name = name
        self.volume = width * depth * height
        self.n_days = 0
        self.n_eggs = 100
        self.n_monkeys = 0
        with open(FILE_PATH, 'w') as file:
            file.write("days,monkeys,eggs\n")
        

    def __str__(self):
        return f"{self.name}: {self.n_monkeys} monkeys after {self.n_days} days"
    
    def evolve(self):
        self._kill_monkeys()
        self._hatch_eggs()
        self._new_eggs()
        self.n_days += 1
        self._write_to_file()

    def _kill_monkeys(self):
        n_dead = 0
        for i in range(self.n_monkeys):
            r = random.random()
            if r < DEATH_PROBABILITY:
                n_dead += 1 
        self.n_monkeys -= min(n_dead, self.n_monkeys)

    def _new_eggs(self):
        n_pairs = math.floor(self.n_monkeys/2)
        for i in range(n_pairs):
            r = random.random()
            if r < EGG_PROBABILITY:
                self.n_eggs += 1

    def _hatch_eggs(self):
        n_hatched = 0
        for i in range(self.n_eggs):
            r = random.random()
            if r < HATCH_PROBABILITY:
                n_hatched += 1
        self.n_eggs -= n_hatched
        self.n_monkeys += n_hatched


    def _write_to_file(self):
        string_to_write = f"{self.n_days}, {self.n_monkeys}, {self.n_eggs}\n"
        with open(FILE_PATH, 'a') as file:
            file.write(string_to_write)