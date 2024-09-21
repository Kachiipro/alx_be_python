# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input.
weather = input("What's the weather like today? (sunny/rainy/cold):")
weather_input = weather.lower()
sunny = "Wear a t-shirt and sunglasses"
rainy = "Don't forget your umbrella and a raincoat"
cold = "Make sure to wear a warm coat and a scarf"

if weather_input == "sunny":
    print(sunny)
elif weather_input == "rainy":
    print(rainy)
elif weather_input == "cold":
    print(cold)
else:
    print("Sorry, I don't have recommendations for this weather.")
