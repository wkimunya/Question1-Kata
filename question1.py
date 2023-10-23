# Ask the user for their name, age, and weight in pounds
name = input("What is your name? ")
age = input("How old are you? ")
weight_pounds = float(input("What is your weight in pounds? "))

# Convert weight from pounds to kilograms
weight_kilograms = weight_pounds * 0.453592

# example on how to print the information including weight in kilograms
print(f"Hello {name}, you are {age} years old, and your weight is {weight_kilograms} kilograms.")
