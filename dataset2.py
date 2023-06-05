import csv
data_file = ('life-expectancy.csv')

def find_min_max_life_expectancy(file_path):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_country = ''
    max_country = ''
    min_year = ''
    max_year = ''

    with open(data_file, 'r') as life_expectancy:
        csv_reader = csv.reader(data_file)
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            year = row[0]
            country = row[1]
            life_expectancy = float(row[2])

            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_country = country
                min_year = year

            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_country = country
                max_year = year

    return min_year, min_country, max_year, max_country


def find_average_life_expectancy(file_path, year):
    total_life_expectancy = 0
    num_countries = 0

    with open(file_path, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            if row[0] == year:
                life_expectancy = float(row[2])
                total_life_expectancy += life_expectancy
                num_countries += 1

    if num_countries > 0:
        average_life_expectancy = total_life_expectancy / num_countries
        return average_life_expectancy
    else:
        return None


def find_min_max_life_expectancy_for_year(file_path, year):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_country = ''
    max_country = ''

    with open(file_path, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            if row[0] == year:
                country = (row[1])
                life_expectancy = float(row[2])

                if life_expectancy < min_life_expectancy:
                    min_life_expectancy = life_expectancy
                    min_country = country

                if life_expectancy > max_life_expectancy:
                    max_life_expectancy = life_expectancy
                    max_country = country

    return min_country, max_country


# Step 1: Open file dialog to select "life-expectancy.csv"
file_path = open('life-expectancy.csv')

if file_path:
    # Step 2: Find the year and country with the lowest and highest life expectancy
    min_year, min_country, max_year, max_country = find_min_max_life_expectancy(file_path)
    print("Lowest life expectancy:")
    print("Year:", min_year)
    print("Country:", min_country)
    print()
    print("Highest life expectancy:")