def get_weather(temp):
    if temp > 21:
        return "hot"
    elif temp == 21:
        return "neutral"
    else:
        return "cold"
