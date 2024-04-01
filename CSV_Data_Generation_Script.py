import random
import string
import csv

# Lists of sample data
cities = ["Bengaluru", "Delhi", "Chennai", "Mumbai", "Kolkata", "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Lucknow"]
cuisines = ["South Indian", "North Indian", "Street Food", "West Indian", "Seafood", "Mughlai", "Rajasthani", "Bengali", "Gujarati", "Hyderabadi"]
secondary_cuisines = ["Mughlai", "Awadhi", "Tandoori", "Coastal", "Chaat", None]
price_ranges = ["₹100-₹300", "₹200-₹500", "₹300-₹700", "₹500-₹1000", "₹700-₹1500", "₹1000-₹2000"]
dish_names = ["Masala Dosa", "Butter Chicken", "Filter Coffee", "Chicken Tikka", "Biryani", "Gulab Jamun", "Plain Dosa", "Sambar Vada", "Pav Bhaji", "Prawn Curry", "Solkadi", "Kebabs", "Chole Bhature", "Laal Maas", "Kosha Mangsho", "Dhokla", "Haleem", "Dahi Vada"]

# Function to generate a random restaurant name
def random_restaurant_name():
    name_parts = ["Royal", "Taj", "Dosa", "Spice", "Flavors", "Zaiqa", "Swad", "Rasoi", "Feast", "Relish"]
    name = random.choice(name_parts)
    if random.random() < 0.3:
        name += " " + random.choice(string.ascii_uppercase)
    return name

# Function to generate random restaurant data
def generate_restaurant_data():
    city = random.choice(cities)
    cuisine = random.choice(cuisines)
    secondary_cuisine = random.choice(secondary_cuisines)
    price_range = random.choice(price_ranges)
    dish = random.choice(dish_names)
    price = random.randint(50, 2000)

    return [random_restaurant_name(), f"{city}", cuisine, secondary_cuisine, price_range, dish, price]

# Generate and save random restaurant data in a CSV file
num_restaurants = 15000
filename = "restaurant_data.csv"  # Change the file path to a location where you have write permissions

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Restaurant Name", "Location", "Cuisine", "Secondary Cuisine", "Price Range", "Dish", "Price"])
    
    for _ in range(num_restaurants):
        data = generate_restaurant_data()
        writer.writerow(data)

print(f"Restaurant data saved in {filename}")
