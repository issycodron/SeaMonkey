import os
from seamonkey import Tank, DAYS_BEFORE_INTERACTION
import shutil


####################
OUTPUT_DIR = "output"
shutil.rmtree(OUTPUT_DIR)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


my_tank = Tank("My Crevice", 0.1, 0.4)
my_tank.feed_monkeys(1000)
print(my_tank)

days_since_interaction = DAYS_BEFORE_INTERACTION 

while my_tank.n_monkeys > 0 or my_tank.n_days < 10:
    if days_since_interaction >= DAYS_BEFORE_INTERACTION:
        input_food = input("How many food pieces do you want to give the monkeys?: ")
        input_food = int(input_food)
        my_tank.feed_monkeys(input_food)
        days_since_interaction = 0
    my_tank.evolve()
    print(my_tank)
    days_since_interaction += 1

    #in future can get users to decide what sort of interaction to have - eg feed, clean, ignore
