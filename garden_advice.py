
# Determine advice based on the season
def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


# Determine advice based on the plant type
def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Collect user input and display the gardening advice
def main():
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()

    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    print(advice)


# Run the main application
if __name__ == "__main__":
    main()
