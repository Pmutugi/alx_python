def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Key exists, replace the value
        a_dictionary[key] = value
    else:
        # Key doesn't exist, add a new key-value pair
        a_dictionary[key] = value
        
# def print_sorted_dictionary(my_dict):
#     """ Print sorted dictionary """
#     keys = sorted(my_dict.keys())
#     for k in keys:
#         print("{}: {}".format(k, my_dict[k]))

# a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
# new_dict = update_dictionary(a_dictionary, 'language', "Python")
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)

# print("--")
# print("--")

# new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)
        
