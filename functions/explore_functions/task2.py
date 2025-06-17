# Using default parameters

def describe_pet(pet_name: str, animal_type: str = "dog"):
    """Display information about a pet."""
    print(f"I have a {animal_type} named {pet_name}.")
    
# Test the function
describe_pet("Buddy")
describe_pet("Whiskers", "cat")