def get_weather(temp):
    if temp > 20:
        return "hot"
    else:
        print("Temperature is below or equal to 20 degrees.")
        return "cold"


print(get_weather(19))
