def update_dictionary(a_dictionary, key, value):
    # Update the value if the key already exists
    # Otherwise, add a new key/value pair
    a_dictionary[key] = value

# Example usage:
my_dictionary = {'a': 1, 'b': 2, 'c': 3}

# Updating existing key 'b'
update_dictionary(my_dictionary, 'b', 10)

# Adding a new key 'd'
update_dictionary(my_dictionary, 'd', 4)

# Display the updated dictionary
print(my_dictionary)