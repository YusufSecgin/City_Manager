import folium
import os


class Map:
    def __init__(self):
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def find_city(self, city_name):
        for city in self.cities:
            if city.name.lower() == city_name.lower():
                return city
        return None

    def display_city_info(self, city_name):
        city = self.find_city(city_name)
        if city:
            print("\nCity Information:")
            print(city)
        else:
            print("\nCity not found.")
        print("\n")

    def generate_city_map(self, city_name):
        city = self.find_city(city_name)
        if city:
            map = folium.Map(location=[city.latitude, city.longitude], zoom_start=12)
            folium.Marker(
                [city.latitude, city.longitude],
                tooltip=f"{city.name}",
                popup=f"Population: {city.population}",
            ).add_to(map)
            map_file_path = (
                f'./src/assets/{city.name.replace(" ", "_").lower()}_map.html'
            )
            map.save(map_file_path)
            return map_file_path
        else:
            return None

    def display_most_crowded(self, n):
        sorted_cities = sorted(
            self.cities, key=lambda city: city.population, reverse=True
        )
        print(f"\nTop {n} Most Crowded Cities:")
        for i, city in enumerate(sorted_cities[:n]):
            print(f"{i+1}. {city.name} - Population: {city.population}")
        print("\n")

    def display_least_crowded(self, n):
        sorted_cities = sorted(self.cities, key=lambda city: city.population)
        print(f"\nTop {n} Least Crowded Cities:")
        for i, city in enumerate(sorted_cities[:n]):
            print(f"{i+1}. {city.name} - Population: {city.population}")
        print("\n")

    def display_all_cities(self):
        print("\nAll Cities:")
        for city in self.cities:
            print(f"{city}")
        print("\n")

    def sort_cities_by_population(self, order):
        if order.upper() == "A":
            sorted_cities = sorted(self.cities, key=lambda city: city.population)
        else:
            sorted_cities = sorted(
                self.cities, key=lambda city: city.population, reverse=True
            )
        print("\nSorted Cities by Population:")
        for i, city in enumerate(sorted_cities):
            print(f"{i+1}. {city.name} - Population: {city.population}")
        print("\n")
