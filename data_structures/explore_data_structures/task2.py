# Exploring dictionaries in Python

# create a dictionary with some initial data
info = {"name": "Arinjay", "age": 20, "city": "Boston"}

# add a new key-value pair to the dictionary for favorite color
info.update({"favorite_color": "blue"})

# update the city key with a new value
info["city"] = "New York"

# print all the keys and values using a for loop
print("Keys: ", ", ".join(key for key in info.keys()))
print("Values: ", ", ".join(str(value) for value in info.values()))
