from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi with fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}."

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()