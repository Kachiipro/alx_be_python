FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
     global FAHRENHEIT_TO_CELSIUS_FACTOR
     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
     global CELSIUS_TO_FAHRENHEIT_FACTOR
     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = int(input("Enter the temperature to convert:"))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C" :
     celsius = temperature
     result = convert_to_fahrenheit(celsius)
     print(f"{celsius}°C is {result}°F")
elif unit == "F" :
     fahrenheit = temperature
     result = convert_to_celsius(fahrenheit)
     print(f"{fahrenheit}°F is {result}°C")
else:
     print(f"{temperature}°{unit} Invalid temperature. Please enter a numeric value.")
     