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
    
# Assuming City and CityDB classes are already defined and 'Cities.csv' is available in the same directory

# Instantiate CityDB and load the real Cities.csv data
city_db = CityDB()
city_db.load_cities('Cities.csv')

# Test each function and print results
print("Testing each function with real Cities.csv data:\n")

# Test 1: Average temperature of all cities
print("Average temperature of all cities:")
print(city_db.calculate_avg_temp())  # Expected output based on your actual data

# Test 2: Cities in Italy
print("\nCities in Italy:")
city_db.get_cities_by_country("Italy")  # Expected output: all cities in Italy from the CSV file

# Test 3: Average temperature in Italy
print("\nAverage temperature in Italy:")
print(city_db.calculate_avg_temp_by_country("Italy"))  # Expected: Average temperature of cities in Italy

# Test 4: Max temperature in Italy
print("\nMax temperature in Italy:")
print(city_db.calculate_max_temp_by_country("Italy"))  # Expected: Maximum temperature among Italian cities

# Test 5: Min temperature in Italy
print("\nMin temperature in Italy:")
print(city_db.calculate_min_temp_by_country("Italy"))  # Expected: Minimum temperature among Italian cities

# Test 6: Average temperature in Sweden
print("\nAverage temperature in Sweden:")
print(city_db.calculate_avg_temp_by_country("Sweden"))  # Expected: Average temperature of cities in Sweden

# Test 7: Max temperature in Sweden
print("\nMax temperature in Sweden:")
print(city_db.calculate_max_temp_by_country("Sweden"))  # Expected: Maximum temperature among Swedish cities

# Test 8: Min temperature in Sweden
print("\nMin temperature in Sweden:")
print(city_db.calculate_min_temp_by_country("Sweden"))  # Expected: Minimum temperature among Swedish cities
