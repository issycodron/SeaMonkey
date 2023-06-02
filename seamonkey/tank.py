import random
import math
from .settings import DEATH_PROBABILITY, EGG_PROBABILITY, HATCH_PROBABILITY, FILE_PATH, PIXELSPERMETER
import numpy as np
from PIL import Image
####################

class Tank(object):
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.n_days = 0
        self.n_eggs = 100
        self.n_monkeys = 0
        self.food = 0
        with open(FILE_PATH, 'w') as file:
            file.write("days,monkeys,eggs,food\n")

        

    def __str__(self):
        return f"{self.name}: {self.n_monkeys} monkeys after {self.n_days} days"
    
    def evolve(self):
        self._hatch_eggs()
        self._new_eggs()
        self._monkeys_starving()
        self._monkeys_eating()
        self._kill_monkeys()
        self.n_days += 1
        self._write_to_file()
        self._image()

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

    def feed_monkeys(self, food):
        self.food += food

    def _monkeys_eating(self):
        self.food -= self.n_monkeys
        if self.food < 0:
            self.food = 0

    def _monkeys_starving(self):
        if self.food < self.n_monkeys:
            self.n_monkeys = self.food


    def _write_to_file(self):
        string_to_write = f"{self.n_days}, {self.n_monkeys}, {self.n_eggs}, {self.food}\n"
        with open(FILE_PATH, 'a') as file:
            file.write(string_to_write)

    def _image(self):
        width_in_pixels = int(self.width*PIXELSPERMETER)
        height_in_pixels = int(self.height*PIXELSPERMETER)
        image_array = np.zeros((height_in_pixels, width_in_pixels, 3), dtype=np.uint8)
        image_array[:, :, 0] = 176
        image_array[:, :, 1] = 224
        image_array[:, :, 2] = 230

        for i in range(self.n_monkeys):
            x = random.randint(0, width_in_pixels-1)
            y = random.randint(0, height_in_pixels-1)
            image_array[y, x, 0] = 255
            image_array[y, x, 1] = 0
            image_array[y, x, 2] = 0

        image = Image.fromarray(image_array)

        image.save(f'output/seamonkey_{self.n_days:0>6}.png')