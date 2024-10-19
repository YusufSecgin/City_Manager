class City:
    def __init__(self, country, name, longitude, latitude, population):
        self.country = country
        self.name = name
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.population = int(float(population))

    def __repr__(self):
        return (
            f"Country: {self.country}, City: {self.name}, "
            f"Longitude: {self.longitude}, Latitude: {self.latitude}, "
            f"Population: {self.population}"
        )
