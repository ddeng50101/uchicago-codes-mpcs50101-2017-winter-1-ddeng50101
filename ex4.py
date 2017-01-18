cars = 100
# defnining the value of cars
space_in_a_car = 4.0
# defining space_in_a_car
drivers = 30
#defining drivers
passengers = 90
cars_not_driven = cars - drivers
#defining car_not_driven related to two predefined variables
cars_driven = drivers
#these two are logically equivalent
carpool_capacity = cars_driven *space_in_a_car
#defining carpool capacity related to two predefined variables
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers avalable"
print "There will be ", cars_not_driven, "empaty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to car pool today."
print "We need to put about", average_passengers_per_car, "in each car."
