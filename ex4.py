cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_driven = drivers
cars_not_driven = cars-drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers /cars_driven


print "Total numbers of cars is ",cars
print "Total space in a car is",space_in_a_car
print "Total drivers are ",drivers
print "Total car driven is",cars_driven," and total car not driven is ",cars_not_driven
print "total Carpool capacity is ",carpool_capacity," and average is ",average_passengers_per_car