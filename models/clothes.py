from services import current_weather_api


def what_to_wear():
    clothes = current_weather_api.weather_temperature().split()[0]
    clothes_num = float(clothes)
    if clothes_num >= 22:
        return "Kratki rukavi i lagane hlaće"
    elif 12 <= clothes_num < 22:
        return "Lagana jakna i srednje debele hlaće"
    elif 0 <= clothes_num < 12:
        return "Zimska jakna i debele hlaće"
    else:
        return "Zimska jakna, kapa, šal i debele hlaće."
