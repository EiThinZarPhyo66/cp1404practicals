from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)
    good_car.drive(40)
    bad_car.drive(80)
    print(good_car)
    print(bad_car)


main()