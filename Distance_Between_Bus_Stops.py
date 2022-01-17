# Start and Destination
# The Sphinx= 0
# The Princess of Hope = 1
# Baba Chandrakup =3
# Hammerhead = 4

distance=[1,2,3,4]
start=0
destination=3

start, destination = min(start, destination), max(start, destination)
clock_dist = sum(distance[start:destination])
anti_clock_dist = sum(distance[:start]) + sum(distance[destination:])
min= min(clock_dist, anti_clock_dist)


print("Distance between " + str(start) + " and " + str(destination) + " is "  + str(clock_dist) + " or " + str(anti_clock_dist) + " minimum is " + str(min))


