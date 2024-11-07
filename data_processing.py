import csv, os

class City:
    def __init__(self, city_name, country, temperature):
        self.city_name = city_name
        self.country = country
        self.temperature = float(temperature)

class CityDB:
    def __init__(self):
        self.cities = []
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def load_cities(self, file):
        with open(os.path.join(self.__location__, file)) as f:
            rows = csv.DictReader(f)
            for row in rows:
                city = City(row['city'], row['country'], row['temperature'])
                self.cities.append(city)

    def calculate_avg_temp(self):
        temps = [city.temperature for city in self.cities]
        return sum(temps)/len(temps)
    
    def get_cities_by_country(self, country):
        for city in self.cities:
            if city.country == country:
                print(city.city_name)
    
    def calculate_avg_temp_by_country(self, country):
        temps = []
        for city in self.cities:
            if city.country == country:
                temps.append(city.temperature)
        return sum(temps) / len(temps) if temps else None

    def calculate_max_temp_by_country(self, country):
        temps = []
        for city in self.cities:
            if city.country == country:
                temps.append(city.temperature)
        return max(temps) if temps else None
    
    def calculate_min_temp_by_country(self, country):
        temps = []
        for city in self.cities:
            if city.country == country:
                temps.append(city.temperature)
        return min(temps) if temps else None
    
# Instantiate the CityDatabase and load the data
city_db = CityDatabase()
city_db.load_cities('Cities.csv')

# Print the average temperature of all cities
print("The average temperature of all the cities:")
average_temp_all = city_db.calculate_average_temperature()
print(f"{average_temp_all:.2f}°C\n" if average_temp_all is not None else "No data available\n")

# Print all cities in Italy
country_name = 'Italy'
italy_cities = city_db.get_cities_by_country(country_name)
print(f"All the cities in {country_name}: {italy_cities}\n")

# Print the average temperature for all cities in Italy
average_temp_italy = city_db.calculate_average_temperature_by_country(country_name)
print(f"The average temperature of all the cities in {country_name}:")
print(f"{average_temp_italy:.2f}°C\n" if average_temp_italy is not None else "No data available\n")

# Print the max temperature for all cities in Italy
max_temp_italy = city_db.calculate_max_temperature_by_country(country_name)
print(f"The max temperature of all the cities in {country_name}:")
print(f"{max_temp_italy:.2f}°C\n" if max_temp_italy is not None else "No data available\n")

# Print the min temperature for all cities in Italy
min_temp_italy = city_db.calculate_min_temperature_by_country(country_name)
print(f"The min temperature of all the cities in {country_name}:")
print(f"{min_temp_italy:.2f}°C\n" if min_temp_italy is not None else "No data available\n")

# Additional calculations for Sweden
sweden_name = 'Sweden'
average_temp_sweden = city_db.calculate_average_temperature_by_country(sweden_name)
print(f"The average temperature of all the cities in {sweden_name}:")
print(f"{average_temp_sweden:.2f}°C\n" if average_temp_sweden is not None else "No data available\n")

max_temp_sweden = city_db.calculate_max_temperature_by_country(sweden_name)
print(f"The max temperature of all the cities in {sweden_name}:")
print(f"{max_temp_sweden:.2f}°C\n" if max_temp_sweden is not None else "No data available\n")

min_temp_sweden = city_db.calculate_min_temperature_by_country(sweden_name)
print(f"The min temperature of all the cities in {sweden_name}:")
print(f"{min_temp_sweden:.2f}°C\n" if min_temp_sweden is not None else "No data available\n")