from seamonkey import Tank

####################



my_tank = Tank("My Crevice", 10, 10, 10)
print(my_tank)

while my_tank.n_monkeys > 0 or my_tank.n_days < 10:
    my_tank.evolve()
    print(my_tank)


