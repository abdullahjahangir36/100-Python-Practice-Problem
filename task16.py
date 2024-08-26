def determine_weather(temperature, humidity):
    if temperature >= 30:
        if humidity >= 90:
            return "Hot and Humid"
        else:
            return "Hot"
    else:
        if humidity >= 90:
            return "Cool and Humid"
        else:
            return "Cool"

# Input from the user
try:
    temperature = float(input("Enter the temperature in °C: "))
    humidity = float(input("Enter the humidity in %: "))

    # Determine the weather
    weather = determine_weather(temperature, humidity)
    print(f"The weather is: {weather}")

except ValueError:
    print("Please enter valid numerical values for temperature and humidity.")
