from taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
print(my_taxi)
my_taxi.drive(40)
print(my_taxi)
print(f"The taxi's current fare {my_taxi.current_fare_distance}.")
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(f"The taxi's current fare {my_taxi.current_fare_distance}.")
