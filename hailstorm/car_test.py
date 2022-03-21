from car import Car

my_car = Car("VW", "YELLOW", 75)
print(my_car)

my_car.paint_with("BLUE")
print(my_car)

my_ferrari = Car("FERRARI", "RED", 550)
print(my_ferrari)

tuning_successful = my_ferrari.apply_tuning_kit()
print("Tuning successful " + str(tuning_successful) + " : " + str(my_ferrari))

tuning_successful = my_ferrari.apply_tuning_kit()
print("Tuning successful " + str(tuning_successful) + " : " + str(my_ferrari))

print(Car.generate_info())

print (my_car.generate_info())

print (my_car.object_method())

toms_car = Car("Audi", "BLUE", 275)
jims_car = Car("Audi", "BLUE", 275)

print (toms_car == jims_car)

print (toms_car is jims_car)

