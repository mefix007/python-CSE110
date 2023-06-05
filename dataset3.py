import csv
data_file = ('life-expectancy.csv')

with open("life-expectancy.csv") as data_file:
    reader= csv.reader(data_file)
    jump_row = next(data_file)
    year = []
    
    user_input= input('enter the year of choice: ')
    year_list = []
    life_expectancy = []
    year_with_highest_life_expectancy = [0]
    year_with_lowest_life_expectancy =[1000]

    for row in reader:
        if user_input.lower() == row[2].lower():
            life_expectancy = float(row[3])
            year_list.append(life_expectancy)

        if  life_expectancy > year_with_highest_life_expectancy:
            year_with_highest_life_expectancy = life_expectancy

        if  life_expectancy < year_with_lowest_life_expectancy:
            year_with_lowest_life_expectancy = life_expectancy

    average_year_life_expectancy = sum(year_with_highest_life_expectancy) / len(year_list)

       

print(f"{user_input}'s lowest life expectancy: {year_with_lowest_life_expectancy}")
print(f"{user_input}'s highest life expectancy: {year_with_highest_life_expectancy}")
print(f"{user_input}'s average life expectancy: {average_year_life_expectancy}")