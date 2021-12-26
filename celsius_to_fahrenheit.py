# program to covert the temperature from celsius to fahrenheit
#!/usr/bin/env python3
# Path: celsius_to_fahrenheit.py

# take the temperature in celsius from the user
celsius = float(input("Enter the temperature in celsius: "))

# conversion factor for celsius to fahrenheit

fahrenheit = (celsius * 9/5) + 32

# print the temperature in celsius and fahrenheit
print("The temperature in celsius is: ", celsius)
print("The temperature in fahrenheit is: ", fahrenheit)
