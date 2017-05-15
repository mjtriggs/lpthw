# Total Cars
cars = 100

# Number of seats in each car
space_in_a_car = 4.0

# Active Drivers
drivers = 30

# Total passengers on the road
passengers = 90

# Cars not used
cars_not_driven = cars - drivers

# Cars used
cars_driven = drivers

# Maximum number of commuters
carpool_capacity = cars_driven * space_in_a_car

# Average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
