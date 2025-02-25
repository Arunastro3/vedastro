import vedastro

# Example: Get planetary positions for a given date
date = "2025-02-25"
location = {"latitude": 37.7749, "longitude": -122.4194}  # Example: San Francisco

# Assuming Vedastro has a function to get planetary positions
planet_positions = vedastro.get_planetary_positions(date, location)

print("Planetary Positions on", date)
for planet, position in planet_positions.items():
    print(f"{planet}: {position}")

