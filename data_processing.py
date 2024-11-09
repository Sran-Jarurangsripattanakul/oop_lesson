class TableDB:
    def __init__(self):
        self.tables = []

    def add(self, table):
        index = self.find_table(table)
        if index == -1:
            self.tables.append(table)
        else:
            print(f"Table {table.name} already exists in the database.")

    def find_table(self, table_name):
        for table in self.tables:
            if table.name == table_name:
                return table
        return -1

class Table:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def filter_data(self, condition):
        return [item for item in self.data if condition(item)]

    def aggregate_data(self, key, func):
        values = [float(item[key]) for item in self.data]
        return func(values)

    def __str__(self):
        return f"DataTable: {self.name} with {len(self.data)} records."

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))
# Let's write code to

cities_table = Table("cities", cities)
countries_table = Table("countries", countries)

# Initialize the database
database = TableDB()
database.add(cities_table)
database.add(countries_table)

# Filter cities by country
italian_cities = cities_table.filter_data(lambda city: city['country'] == 'Italy')
swedish_cities = cities_table.filter_data(lambda city: city["country"] == "Sweden")

# Create new Table for Italian and Swedish cities
italian_city_table = Table("ItalianCities", italian_cities)
swedish_city_table = Table("SwedishCities", swedish_cities)

database.add(italian_city_table)
database.add(swedish_city_table)

# Calculate and display average temperature in Italian cities
avg_temp_italy = italian_city_table.aggregate_data("temperature", lambda x: sum(x)/len(x))
print(f"Average temperature in Italian cities: {avg_temp_italy}")

# Calculate and display average temperature in Swedish cities
avg_temp_sweden = swedish_city_table.aggregate_data("temperature", lambda x: sum(x)/len(x))
print(f"Average temperature in Swedish cities: {avg_temp_sweden}")

# Calculate and display the minimum temperature in Italian cities
min_temp_italy = italian_city_table.aggregate_data("temperature", lambda x: min(x))
print(f"Minimum temperature in Italian cities: {min_temp_italy}")

# Calculate and display the maximum temperature in Swedish cities
max_temp_sweden = swedish_city_table.aggregate_data("temperature", lambda x: max(x))
print(f"Maximum temperature in Swedish cities: {max_temp_sweden}")

# Find the maximum and minimum latitude across all cities
max_latitude = cities_table.aggregate_data("latitude", lambda x: max(x))
min_latitude = cities_table.aggregate_data("latitude", lambda x: min(x))

print(f"Maximum latitude across all cities: {max_latitude}")
print(f"Minimum latitude across all cities: {min_latitude}")
