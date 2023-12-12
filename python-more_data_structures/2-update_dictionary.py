def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
def print_sorted_dictionary(my_dict):
   
    keys = sorted(my_dict)
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))
