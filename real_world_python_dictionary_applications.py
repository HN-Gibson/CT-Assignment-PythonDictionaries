# Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions

# Problem Statement: Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# - Add a new category called "Beverages" with at least two items.
restaurant_menu ["Beverages"] = {"Wine":12.99, "Beer":5.99}
# - Update the price of "Steak" to 17.99.
restaurant_menu ["Main Course"]["Steak"] = 17.99
# - Remove "Bruschetta" from "Starters". 
restaurant_menu["Starters"].pop("Bruschetta")

# looped through the dictionary to provide a more legible print out, but curious how to get the key-value pairs in the nested dictionary to print without the brackets...?
for category, items in restaurant_menu.items():
    print(category, items)