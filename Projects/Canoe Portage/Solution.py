# Convert rods to other units and calculate walking time
# Constants
METERS_PER_ROD = 5.0292
FEET_PER_METER = 1 / 0.3048
MILES_PER_METER = 1 / 1609.34
FURLONGS_PER_ROD = 1 / 40
WALKING_SPEED_MPH = 3.1

def conversion(rod):
    meters = rod * METERS_PER_ROD
    feet = meters * FEET_PER_METER
    miles = meters * MILES_PER_METER
    furlongs = rod * FURLONGS_PER_ROD
    time = (miles / WALKING_SPEED_MPH) * 60  

    print(f"You input {rod} rods.",
          f"Meters: {meters}",
          f"Feet: {feet}",
          f"Miles: {miles:.3f}",
          f"Furlongs: {furlongs}",
          f"Time: {time:.3f} minutes", sep="\n")

rods = float(input("Enter the number of rods: "))
conversion(rods)