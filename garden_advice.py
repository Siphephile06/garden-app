# Input values for the season and plant type.
seasons = input("Enter Season: ")
plant_types = input("Enter type of plant: ")


# Determine advice based on the season
def which_season(season):
    advice = ""
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"
    print(advice)
    return advice


# Determine advice based on the plant type
def which_plant_type(plant_type):
    advice = ""
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."
    print(advice)
    return advice


# Call the functions
which_season(seasons)
which_plant_type(plant_types)
