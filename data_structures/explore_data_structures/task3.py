# Using Tuples

# createa tuple with favorite movie, song and book
favorites = ("Good Will Hunting", "Lovely", "When All Is Said")
print("Favorite things:", favorites)

# try to change one of the values in the tuple
try:
    favorites[0] = "Inception"
except TypeError as e:
    print("Error:", e)

# print the length of the tuple
print("Length of favorites tuple:", len(favorites))