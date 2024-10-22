def forecast(*args):
    weathers = {
    "Sunny": [],
    "Cloudy": [],
    "Rainy": []

    }

    for location, weather in args:
        weathers[weather].append(location)

    result = ''

    for weather, locations in weathers.items():
        for location in sorted(locations):
            result += f"{location} - {weather}\n"

    return result.strip()


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

