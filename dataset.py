import csv


data_file = ('life-expectancy.csv')
def find_min_max_life_expectancy(data_file):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    
    csv_reader = csv.reader(data_file)

    for row in csv_reader:
            year = float(row[0])
            country = float(row[1])
            life_expectancy = float(row[2])

    with open('life-expectancy.csv') as data_file:
        for line in life_expectancy:
            parts = line.strip().split(',')  # Assuming comma-separated values

            if len(parts) >= 2:
                life_expectancy = float(parts[2])

                if life_expectancy < min_life_expectancy:
                    min_life_expectancy = life_expectancy

                if life_expectancy > max_life_expectancy:
                    max_life_expectancy = life_expectancy

    return min_life_expectancy, max_life_expectancy


# Usage example
data_file = 'life-expectancy.csv'  
min_value, max_value = find_min_max_life_expectancy(data_file)

print(f"Lowest life expectancy: {min_value}")
print(f"Highest life expectancy: {max_value}")