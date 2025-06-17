# Functions with Variable Arguments

def make_sandwich(*ingredients):
    """
    Create a sandwich with the given ingredients.
    """
    if not ingredients:
        return "You need to provide at least one ingredient for the sandwich."
    
    return f"Your sandwich has {' and '.join(ingredients)}."

# Test the function with different numbers of ingredients
print(make_sandwich("ham", "cheese", "lettuce"))
print(make_sandwich("peanut butter", "jelly"))
print(make_sandwich("turkey", "avocado", "tomato", "spinach"))
print(make_sandwich())  # No ingredients provided