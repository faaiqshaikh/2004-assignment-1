def add_key(dictionary, key, value):
    """Adds a key-value pair to a dictionary."""
    dictionary[key] = value
    print(f"Key '{key}' added successfully.")

def remove_key(dictionary, key):
    """Removes a key-value pair from a dictionary."""
    if key in dictionary:
        del dictionary[key]
        print(f"Key '{key}' removed successfully.")
    else:
        print(f"Key '{key}' not found.")

def update_value(dictionary, key, value):
    """Updates the value of a key in a dictionary."""
    if key in dictionary:
        dictionary[key] = value
        print(f"Value of key '{key}' updated successfully.")
    else:
        print(f"Key '{key}' not found.")

def get_value(dictionary, key):
    """Retrieves the value associated with a key from a dictionary."""
    if key in dictionary:
        return dictionary[key]
    else:
        return None

# Example usage
my_dictionary = {}

add_key(my_dictionary, "name", "John")
add_key(my_dictionary, "age", 25)

print(get_value(my_dictionary, "name"))  # Output: John

update_value(my_dictionary, "age", 30)
print(get_value(my_dictionary, "age"))  # Output: 30

remove_key(my_dictionary, "name")
print(get_value(my_dictionary, "name"))  # Output: None
