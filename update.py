import json
import sys

filename = sys.argv[1]
version = sys.argv[2]
# Data to add to the JSON file
data_to_add = {
    "v" + version : "v" + version + ".js"
}

# Load the existing data from the JSON file, if it exists
try:
    with open(filename, "r") as file:
        existing_data = json.load(file)
except FileNotFoundError:
    existing_data = {}

# Update the existing data with the new data
existing_data.update(data_to_add)

# Write the updated data back to the JSON file
with open(filename, "w") as file:
    json.dump(existing_data, file, indent=4)

print("Data added to", filename, "successfully.")
