import csv
from models.city import City


def load_cities(filename):
    cities = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("Detected column headers:", reader.fieldnames)
        for row in reader:
            try:
                country = row["country"]
                city_name = row["city"]
                latitude = row["lat"]
                longitude = row["lng"]
                population = row["population"]
                cities.append(City(country, city_name, longitude, latitude, population))
            except KeyError as e:
                print("Missing column in CSV:", e)
                break
    return cities
