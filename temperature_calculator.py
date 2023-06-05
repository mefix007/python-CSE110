print()
print('Welcome to Mefix Wind_chill calcultor \nfollow the promptings and enter the accurate data')
print()
def calculate_wind_chill(temperature, wind_speed):
    # Convert temperature to Fahrenheit if provided in Celsius
    if temperature < 50:
        temperature = temperature * (9/5) + 32

    # Calculate wind chill using the formula
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16
    return wind_chill


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


def display_wind_chill():
    temperature_input = input("Enter the temperature: ")
    temperature_unit = input("Enter the temperature unit (Celsius or Fahrenheit (C/F)): ")

    # Convert temperature to Fahrenheit if provided in Celsius
    if temperature_unit.lower() == "celsius":
        temperature = convert_celsius_to_fahrenheit(float(temperature_input))
    else:
        temperature = float(temperature_input)

    # Loop through wind speeds from 5 to 60 in increments of 5
    wind_speeds = range(5, 61, 5)
    for wind_speed in wind_speeds:
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At {wind_speed} mph, the wind chill is: {wind_chill:.2f}")


# Call the main function to display the wind chills
display_wind_chill()
print()
print("Thank you using mefix wind_chill calculator")
print()