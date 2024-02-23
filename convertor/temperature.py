def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return int(fahrenheit)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return int(celsius)