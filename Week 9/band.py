class Band:
    """A band has many musicians."""

    def __init__(self, name: str):
        """Initialize a Band instance."""
        self.name = name
        self.bands = []

    def __str__(self):
        """Return a string representation of the Band."""
        bands_str = []
        for band in self.bands:
            bands_str.append((str(band)))
        return f"{self.name} ({', '.join(bands_str)})"

    def add(self, band):
        """Add guitars or musicians to a band."""
        self.bands.append(band)

    def play(self):
        """Play bands."""
        output = ""
        for musician in self.bands:
            if musician.instruments:
                output = output + musician.play() + "\n"
            else:
                output = output + musician.name + " needs an instrument!\n"
        return output






